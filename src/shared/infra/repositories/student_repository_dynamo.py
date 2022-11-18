from typing import List, Tuple

from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.student import Student
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.repositories.student_repository_interface import IStudentRepository
from src.shared.environments import Environments
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
                                       dynamo_table_name=Environments.get_envs().dynamo_table_name, region=Environments.get_envs().region,
                                       partition_key=Environments.get_envs().dynamo_partition_key,
                                       sort_key=Environments.get_envs().dynamo_sort_key)

    def get_student(self, ra: str) -> Student:
        student = self.dynamo.get_item(partition_key=self.partition_key_format(ra), sort_key=ra)
        student_dto = StudentDynamoDTO.from_dynamo(student['Item'])
        return student_dto.to_entity()


    def update_student(self, ra: str, new_name: str = None, new_email: str = None) -> Student:
        pass

    def delete_student(self, ra: str) -> Student:
        pass

    def create_student(self, student: Student) -> Student:
        student_dto = StudentDynamoDTO.from_entity(student)
        self.dynamo.put_item(partition_key=self.partition_key_format(student.ra), sort_key=student.ra, item=student_dto.to_dynamo())


    def get_selfies_by_ra(self, ra: str) -> Tuple[List[Selfie], Student]:
        pass

    def get_selfie(self, ra: str, idSelfie: int) -> Selfie:
        selfie_response = self.dynamo.get_item(partition_key=self.partition_key_format(ra), sort_key=self.selfie_sort_key_format(ra, idSelfie))
        student_response = self.dynamo.get_item(partition_key=self.partition_key_format(ra), sort_key=ra)
        dynamo_dto = SelfieDynamoDTO.from_dynamo(selfie_response['Item'], student_response['Item'])

        return dynamo_dto.to_entity()

    def delete_selfie(self, ra: str, idSelfie: int) -> Tuple[Selfie, Student]:
        pass

    def create_selfie(self, selfie: Selfie) -> Selfie:
        selfie_dto = SelfieDynamoDTO.from_entity(selfie)
        item = selfie_dto.to_dynamo()
        self.dynamo.put_item(partition_key=self.partition_key_format(selfie.student.ra), sort_key=self.selfie_sort_key_format(selfie.student.ra, selfie.idSelfie), item=item, is_decimal=True)

    def update_selfie(self, ra: str, idSelfie: int, new_state: STATE = None,
                      new_rejectionReasons: REJECTION_REASON = None, new_rejectionDescription: str = None) -> Selfie:
        pass

    def get_all_selfies(self) -> List[Selfie]:
        pass

    def check_student_has_approved_selfie(self, ra: str) -> bool:
        pass

    def get_all_students(self) -> List[Student]:
        pass
