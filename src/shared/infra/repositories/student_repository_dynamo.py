from typing import List, Tuple

from boto3.dynamodb.conditions import Key, Attr

from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.student import Student
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.repositories.student_repository_interface import IStudentRepository
from src.shared.environments import Environments
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.dtos.selfie_dynamo_dto import SelfieDynamoDTO
from src.shared.infra.dtos.student_dynamo_dto import StudentDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class StudentRepositoryDynamo(IStudentRepository):
    dynamo: DynamoDatasource

    @staticmethod
    def partition_key_format(ra):
        return f"student#{ra}"

    @staticmethod
    def selfie_sort_key_format(ra, idSelfie):
        return f"selfie#{ra}#{idSelfie}"

    def __init__(self):
        self.dynamo = DynamoDatasource(endpoint_url=Environments.get_envs().endpoint_url,
                                       dynamo_table_name=Environments.get_envs().dynamo_table_name,
                                       region=Environments.get_envs().region,
                                       partition_key=Environments.get_envs().dynamo_partition_key,
                                       sort_key=Environments.get_envs().dynamo_sort_key)

    def get_student(self, ra: str) -> Student:
        student = self.dynamo.get_item(partition_key=self.partition_key_format(ra), sort_key=ra)

        if "Item" not in student:
            raise NoItemsFound("ra")

        student_dto = StudentDynamoDTO.from_dynamo(student['Item'])
        return student_dto.to_entity()

    def update_student(self, ra: str, new_name: str = None, new_email: str = None) -> Student:
        update_item = {}

        if new_name:
            update_item['name'] = new_name
        if new_email:
            update_item['email'] = new_email
        if ra:
            update_item['ra'] = ra
        if not update_item:
            raise NoItemsFound("ra")

        self.dynamo.update_item(partition_key=self.partition_key_format(ra), sort_key=ra, update_dict=update_item)

        return self.get_student(ra)

    def delete_student(self, ra: str) -> Student:
        resp = self.dynamo.delete_item(partition_key=self.partition_key_format(ra), sort_key=ra)

        if "Attributes" not in resp:
            raise NoItemsFound("ra")

        student_dto = StudentDynamoDTO.from_dynamo(resp['Attributes'])
        return student_dto.to_entity()

    def create_student(self, student: Student) -> Student:
        student_dto = StudentDynamoDTO.from_entity(student)
        self.dynamo.put_item(partition_key=self.partition_key_format(student.ra), sort_key=student.ra,
                             item=student_dto.to_dynamo())

    def get_selfies_by_ra(self, ra: str) -> Tuple[List[Selfie], Student]:

        query_string = Key(self.dynamo.partition_key).eq(self.partition_key_format(ra))

        resp = self.dynamo.query(key_condition_expression=query_string, Select='ALL_ATTRIBUTES')

        if resp['Count'] == 0:
            raise NoItemsFound("ra")

        student_data = resp['Items'].pop(0)
        try:
            student = StudentDynamoDTO.from_dynamo(student_data).to_entity() # the sort key choice makes the student to be the first element
        except Exception as err:
            raise Exception(f"Error while trying to get student data from dynamo: {err}")

        try:
            selfies = [SelfieDynamoDTO.from_dynamo(item, student_data).to_entity() for item in resp['Items']]
        except Exception as err:
            raise Exception(f"Error while trying to get selfies data from dynamo: {err}")



        return selfies, student

    def get_selfie(self, ra: str, idSelfie: int) -> Selfie:
        selfie_response = self.dynamo.get_item(partition_key=self.partition_key_format(ra),
                                               sort_key=self.selfie_sort_key_format(ra, idSelfie))
        student_response = self.dynamo.get_item(partition_key=self.partition_key_format(ra), sort_key=ra)
        dynamo_dto = SelfieDynamoDTO.from_dynamo(selfie_response['Item'], student_response['Item'])

        return dynamo_dto.to_entity()

    def delete_selfie(self, ra: str, idSelfie: int) -> Tuple[Selfie, Student]:

        resp = self.dynamo.delete_item(partition_key=self.partition_key_format(ra),
                                sort_key=self.selfie_sort_key_format(ra, idSelfie))

        if "Attributes" not in resp:
            raise NoItemsFound("ra|idSelfie")

        selfie = SelfieDynamoDTO.from_dynamo(resp['Attributes'], StudentDynamoDTO.from_entity(self.get_student(ra)).to_dynamo()).to_entity()

        return selfie, selfie.student

    def create_selfie(self, selfie: Selfie) -> Selfie:
        selfie_dto = SelfieDynamoDTO.from_entity(selfie)
        item = selfie_dto.to_dynamo()
        resp = self.dynamo.put_item(partition_key=self.partition_key_format(selfie.student.ra),
                             sort_key=self.selfie_sort_key_format(selfie.student.ra, selfie.idSelfie), item=item,
                             is_decimal=True)

        return selfie #todo fix that


    def update_selfie(self, ra: str, idSelfie: int, new_state: STATE = None,
                      new_rejectionReasons: REJECTION_REASON = None, new_rejectionDescription: str = None) -> Selfie:
        pass #todo implement and fix interface attributes (list[REJECTION_REASON])])

    def get_all_selfies(self) -> List[Selfie]:
        all_items = self.dynamo.get_all_items()

        students = {}
        selfies = []

        for item in all_items['Items']:
            if item['entity'] == 'student':
                students[item['ra']] = item
            elif item['entity'] == 'selfie':
                ra = item['SK'].split('#')[1]
                selfies.append(SelfieDynamoDTO.from_dynamo(item, students[ra]).to_entity())
            else:
                raise Exception(f"Unknown entity type: {item['entity']}")



        return selfies



    def check_student_has_approved_selfie(self, ra: str) -> bool:
        selfies, _ = self.get_selfies_by_ra(ra)
        for selfie in selfies:
            if selfie.state == STATE.APPROVED:
                return True
        return False

    def get_all_students(self) -> List[Student]:
        all_students = self.dynamo.scan_items(filter_expression=Attr('entity').eq('student'))

        return [StudentDynamoDTO.from_dynamo(item).to_entity() for item in all_students['Items']]
