from datetime import datetime
from decimal import Decimal

from src.shared.domain.entities.label import Label
from src.shared.domain.entities.student import Student
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
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
        assert selfie_dto.state == STATE.DECLINED
        assert selfie_dto.rejectionReasons == [REJECTION_REASON.COVERED_FACE]
        assert selfie_dto.rejectionDescription == 'Balaclava'
        assert selfie_dto.automaticReview.automaticallyRejected == True
        assert type(selfie_dto.automaticReview.labels[0]) == Label
        assert type(selfie_dto.automaticReview.labels[1]) == Label
        assert type(selfie_dto.automaticReview.labels[2]) == Label
        assert selfie_dto.automaticReview.labels[0].name == 'Person'
        assert selfie_dto.automaticReview.labels[0].confidence == 98.54370880126953
        assert selfie_dto.automaticReview.labels[0].parents == []
        assert selfie_dto.automaticReview.labels[0].coords['Height'] == 0.8659809827804565
        assert selfie_dto.automaticReview.labels[0].coords['Left'] == 0.012313545681536198
        assert selfie_dto.automaticReview.labels[0].coords['Top'] == 0.11108686774969101
        assert selfie_dto.automaticReview.labels[0].coords['Width'] == 0.9711952805519104
        assert selfie_dto.automaticReview.labels[1].name == 'Hat'
        assert selfie_dto.automaticReview.labels[1].confidence == 98.54370880126953
        assert selfie_dto.automaticReview.labels[1].parents == []
        assert selfie_dto.automaticReview.labels[1].coords['Height'] == 0.8659809827804565
        assert selfie_dto.automaticReview.labels[1].coords['Left'] == 0.012313545681536198
        assert selfie_dto.automaticReview.labels[1].coords['Top'] == 0.11108686774969101
        assert selfie_dto.automaticReview.labels[1].coords['Width'] == 0.9711952805519104
        assert selfie_dto.automaticReview.labels[2].name == 'Face'
        assert selfie_dto.automaticReview.labels[2].confidence == 98.54370880126953
        assert selfie_dto.automaticReview.labels[2].parents == []
        assert selfie_dto.automaticReview.labels[2].coords['Height'] == 0.8659809827804565
        assert selfie_dto.automaticReview.labels[2].coords['Left'] == 0.012313545681536198
        assert selfie_dto.automaticReview.labels[2].coords['Top'] == 0.11108686774969101
        assert selfie_dto.automaticReview.labels[2].coords['Width'] == 0.9711952805519104

    def test_to_entity(self):
        repo = StudentRepositoryMock()

        selfie_dto = SelfieDynamoDTO(
            idSelfie=0,
            student=repo.students[0],
            dateCreated=datetime(2022, 10, 1, 16, 1, 59, 149927),
            url='https://i.imgur.com/0KFBHTB.jpg',
            state=STATE.DECLINED,
            rejectionReasons=[REJECTION_REASON.COVERED_FACE],
            rejectionDescription='Balaclava',
            automaticReview=repo.selfies[0].automaticReview
        )

        selfie_entity = selfie_dto.to_entity()

        assert selfie_entity.idSelfie == repo.selfies[0].idSelfie
        assert selfie_entity.student.ra == repo.selfies[0].student.ra
        assert selfie_entity.student.name == repo.selfies[0].student.name
        assert selfie_entity.student.email == repo.selfies[0].student.email
        assert selfie_entity.dateCreated == repo.selfies[0].dateCreated
        assert selfie_entity.url == repo.selfies[0].url
        assert selfie_entity.state == repo.selfies[0].state
        assert selfie_entity.rejectionReasons == repo.selfies[0].rejectionReasons
        assert selfie_entity.rejectionDescription == repo.selfies[0].rejectionDescription
        assert selfie_entity.automaticReview.automaticallyRejected == repo.selfies[0].automaticReview.automaticallyRejected

        for i in range(len(selfie_entity.automaticReview.labels)):
            assert selfie_entity.automaticReview.labels[i].name == repo.selfies[0].automaticReview.labels[i].name
            assert selfie_entity.automaticReview.labels[i].confidence == repo.selfies[0].automaticReview.labels[i].confidence
            assert selfie_entity.automaticReview.labels[i].parents == repo.selfies[0].automaticReview.labels[i].parents
            assert selfie_entity.automaticReview.labels[i].coords == repo.selfies[0].automaticReview.labels[i].coords







    def test_from_entity(self):
        repo = StudentRepositoryMock()

        selfie_dto = SelfieDynamoDTO.from_entity(repo.selfies[0])

        expected_selfie_dto = SelfieDynamoDTO(
            idSelfie=repo.selfies[0].idSelfie,
            student=repo.selfies[0].student,
            dateCreated=repo.selfies[0].dateCreated,
            url=repo.selfies[0].url,
            state=repo.selfies[0].state,
            rejectionReasons=repo.selfies[0].rejectionReasons,
            rejectionDescription=repo.selfies[0].rejectionDescription,
            automaticReview=repo.selfies[0].automaticReview,
        )

        assert selfie_dto == expected_selfie_dto

    def test_to_dynamo(self):
        repo = StudentRepositoryMock()

        selfie_dto = SelfieDynamoDTO(
            idSelfie=0,
            student=repo.students[0],
            dateCreated=datetime(2022, 10, 1, 16, 1, 59, 149927),
            url='https://i.imgur.com/0KFBHTB.jpg',
            state=STATE.DECLINED,
            rejectionReasons=[REJECTION_REASON.COVERED_FACE],
            rejectionDescription='Balaclava',
            automaticReview=repo.selfies[0].automaticReview
        )

        selfie_dynamo = selfie_dto.to_dynamo()

        assert selfie_dynamo['idSelfie'] == 0
        assert selfie_dynamo['dateCreated'] == datetime(2022, 10, 1, 16, 1, 59, 149927).isoformat()
        assert selfie_dynamo['url'] == 'https://i.imgur.com/0KFBHTB.jpg'
        assert selfie_dynamo['state'] == 'DECLINED'
        assert selfie_dynamo['rejectionReasons'] == ['COVERED_FACE']
        assert selfie_dynamo['rejectionDescription'] == 'Balaclava'
        assert selfie_dynamo['automaticReview']['automaticallyRejected'] == True

        for i in range(len(repo.selfies[0].automaticReview.labels)):
            assert selfie_dynamo['automaticReview']['labels'][i]['name'] == repo.selfies[0].automaticReview.labels[i].name
            assert selfie_dynamo['automaticReview']['labels'][i]['confidence'] == Decimal(str(repo.selfies[0].automaticReview.labels[i].confidence))
            assert selfie_dynamo['automaticReview']['labels'][i]['parents'] == repo.selfies[0].automaticReview.labels[i].parents
            assert selfie_dynamo['automaticReview']['labels'][i]['coords']['Height'] == Decimal(str(repo.selfies[0].automaticReview.labels[i].coords['Height']))
            assert selfie_dynamo['automaticReview']['labels'][i]['coords']['Left'] == Decimal(str(repo.selfies[0].automaticReview.labels[i].coords['Left']))
            assert selfie_dynamo['automaticReview']['labels'][i]['coords']['Top'] == Decimal(str(repo.selfies[0].automaticReview.labels[i].coords['Top']))
            assert selfie_dynamo['automaticReview']['labels'][i]['coords']['Width'] == Decimal(str(repo.selfies[0].automaticReview.labels[i].coords['Width']))

    def test_from_dynamo_to_entity(self):
        repo = StudentRepositoryMock()
        dynamo_item = {
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
          'rejectionDescription': 'Balaclava',
          'rejectionReasons': ['COVERED_FACE'],
          'state': 'DECLINED',
          'url': 'https://i.imgur.com/0KFBHTB.jpg'}

        entity = SelfieDynamoDTO.from_dynamo(dynamo_item, {"ra": "21010757", "name": "Victor", "email": "eusousoller@gmail.com"}).to_entity()

        assert entity.idSelfie == repo.selfies[0].idSelfie
        assert entity.student.ra == repo.selfies[0].student.ra
        assert entity.student.name == repo.selfies[0].student.name
        assert entity.student.email == repo.selfies[0].student.email
        assert entity.dateCreated == repo.selfies[0].dateCreated
        assert entity.url == repo.selfies[0].url
        assert entity.state == repo.selfies[0].state
        assert entity.rejectionReasons == repo.selfies[0].rejectionReasons
        assert entity.rejectionDescription == repo.selfies[0].rejectionDescription
        assert entity.automaticReview.automaticallyRejected == repo.selfies[0].automaticReview.automaticallyRejected

        for i in range(len(repo.selfies[0].automaticReview.labels)):
            assert entity.automaticReview.labels[i].name == repo.selfies[0].automaticReview.labels[i].name
            assert entity.automaticReview.labels[i].confidence == repo.selfies[0].automaticReview.labels[i].confidence
            assert entity.automaticReview.labels[i].parents == repo.selfies[0].automaticReview.labels[i].parents
            assert entity.automaticReview.labels[i].coords['Height'] == repo.selfies[0].automaticReview.labels[i].coords['Height']
            assert entity.automaticReview.labels[i].coords['Left'] == repo.selfies[0].automaticReview.labels[i].coords['Left']
            assert entity.automaticReview.labels[i].coords['Top'] == repo.selfies[0].automaticReview.labels[i].coords['Top']
            assert entity.automaticReview.labels[i].coords['Width'] == repo.selfies[0].automaticReview.labels[i].coords['Width']



    def test_from_entity_to_dynamo(self):
        repo = StudentRepositoryMock()

        entity = repo.selfies[0]

        dynamo_item = {
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
            'rejectionDescription': 'Balaclava',
            'rejectionReasons': ['COVERED_FACE'],
            'state': 'DECLINED',
            'url': 'https://i.imgur.com/0KFBHTB.jpg',
            'entity': 'selfie'

        }

        dynamo_item_from_dto = SelfieDynamoDTO.from_entity(entity).to_dynamo()

        assert dynamo_item == dynamo_item_from_dto






