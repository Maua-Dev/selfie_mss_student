from datetime import datetime
from decimal import Decimal

from src.shared.domain.entities.student import Student
from src.shared.infra.dtos.selfie_dynamo_dto import SelfieDynamoDTO
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock


class Test_SelfieDynamoDTO:

    def test_from_dynamo(self):
        selfie_data = {'Item': {'PK': 'student#19003315',
          'SK': 'selfie#19003315#0',
          'automaticReview': {'automaticallyRejected': True,
                              'labels': [{'confidence': Decimal('98.54370880126953'),
                                          'coords': {'Height': Decimal('0.8659809827804565'),
                                                     'Left': Decimal('0.012313545681536198'),
                                                     'Top': Decimal('0.11108686774969101'),
                                                     'Width': Decimal('0.9711952805519104')},
                                          'name': 'Person',
                                          'parents': []},
                                         {'confidence': Decimal('98.54370880126953'),
                                          'coords': {'Height': Decimal('0.8659809827804565'),
                                                     'Left': Decimal('0.012313545681536198'),
                                                     'Top': Decimal('0.11108686774969101'),
                                                     'Width': Decimal('0.9711952805519104')},
                                          'name': 'Hat',
                                          'parents': []},
                                         {'confidence': Decimal('98.54370880126953'),
                                          'coords': {'Height': Decimal('0.8659809827804565'),
                                                     'Left': Decimal('0.012313545681536198'),
                                                     'Top': Decimal('0.11108686774969101'),
                                                     'Width': Decimal('0.9711952805519104')},
                                          'name': 'Face',
                                          'parents': []}],
                              'rejectionReasons': ['COVERED_FACE']},
          'dateCreated': '2022-10-01T16:01:59.149927',
          'idSelfie': Decimal('0'),
          'message': 'the selfie was retriven',
          'rejectionDescription': 'Balaclava',
          'rejectionReasons': ['COVERED_FACE'],
          'state': 'DECLINED',
          'url': 'https://i.imgur.com/0KFBHTB.jpg'},
 'ResponseMetadata': {'HTTPHeaders': {'content-length': '1205',
                                      'content-type': 'application/x-amz-json-1.0',
                                      'date': 'Thu, 17 Nov 2022 22:42:43 GMT',
                                      'server': 'Jetty(9.4.48.v20220622)',
                                      'x-amz-crc32': '4019106892',
                                      'x-amzn-requestid': '055ea0db-82bd-4c0d-91d2-84d032f12336'},
                      'HTTPStatusCode': 200,
                      'RequestId': '055ea0db-82bd-4c0d-91d2-84d032f12336',
                      'RetryAttempts': 0}}


        student_data = {
            "ra": "19003315",
            "name": "Bruno Vilardi Bueno",
            "email": "bruno@bruno.com"
        }

        selfie_dto = SelfieDynamoDTO.from_dynamo(selfie_data["Item"], student_data)

        assert selfie_dto.idSelfie == 0
        assert selfie_dto.student.ra == Student(**student_data).ra
        assert selfie_dto.student.name == Student(**student_data).name
        assert selfie_dto.student.email == Student(**student_data).email
        assert selfie_dto.dateCreated == datetime(2022, 10, 1, 16, 1, 59, 149927)
        assert selfie_dto.url == 'https://i.imgur.com/0KFBHTB.jpg'
        assert selfie_dto.state == 'DECLINED'
        assert selfie_dto.rejectionReasons == ['COVERED_FACE']
        assert selfie_dto.rejectionDescription == 'Balaclava'
        assert selfie_dto.automaticReview.automaticallyRejected == True
        assert selfie_dto.automaticReview.labels[0]['name'] == 'Person'
        assert selfie_dto.automaticReview.labels[0]['confidence'] == 98.54370880126953
        assert selfie_dto.automaticReview.labels[0]['parents'] == []
        assert selfie_dto.automaticReview.labels[0]['coords']['Height'] == 0.8659809827804565
        assert selfie_dto.automaticReview.labels[0]['coords']['Left'] == 0.012313545681536198
        assert selfie_dto.automaticReview.labels[0]['coords']['Top'] == 0.11108686774969101
        assert selfie_dto.automaticReview.labels[0]['coords']['Width'] == 0.9711952805519104
        assert selfie_dto.automaticReview.labels[1]['name'] == 'Hat'
        assert selfie_dto.automaticReview.labels[1]['confidence'] == 98.54370880126953
        assert selfie_dto.automaticReview.labels[1]['parents'] == []
        assert selfie_dto.automaticReview.labels[1]['coords']['Height'] == 0.8659809827804565
        assert selfie_dto.automaticReview.labels[1]['coords']['Left'] == 0.012313545681536198
        assert selfie_dto.automaticReview.labels[1]['coords']['Top'] == 0.11108686774969101
        assert selfie_dto.automaticReview.labels[1]['coords']['Width'] == 0.9711952805519104
        assert selfie_dto.automaticReview.labels[2]['name'] == 'Face'
        assert selfie_dto.automaticReview.labels[2]['confidence'] == 98.54370880126953
        assert selfie_dto.automaticReview.labels[2]['parents'] == []
        assert selfie_dto.automaticReview.labels[2]['coords']['Height'] == 0.8659809827804565
        assert selfie_dto.automaticReview.labels[2]['coords']['Left'] == 0.012313545681536198
        assert selfie_dto.automaticReview.labels[2]['coords']['Top'] == 0.11108686774969101
        assert selfie_dto.automaticReview.labels[2]['coords']['Width'] == 0.9711952805519104




    def test_to_entity(self):
        repo = StudentRepositoryMock()

        selfie_dto = SelfieDynamoDTO(
            idSelfie=0,
            student=repo.students[0],
            dateCreated=datetime(2022, 10, 1, 16, 1, 59, 149927),
            url='https://i.imgur.com/0KFBHTB.jpg',
            state='DECLINED',
            rejectionReasons=['COVERED_FACE'],
            rejectionDescription='Balaclava',
            automaticReview=repo.selfies[0].automaticReview
        )

        selfie_entity = selfie_dto.to_entity()

        assert selfie_entity == repo.selfies[0]
