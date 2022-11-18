import json
from datetime import datetime
from decimal import Decimal

from src.shared.domain.entities.automatic_review import AutomaticReview
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.student import Student
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE


class SelfieDynamoDTO:
    idSelfie: int
    student: dict
    dateCreated: datetime
    url: str
    state: str
    rejectionReasons: list[str]
    rejectionDescription: str
    automaticReview: AutomaticReview

    def __init__(self, idSelfie: int, student: Student, dateCreated: str, url: str, state: str,
                 rejectionReasons: list[str], rejectionDescription: str, automaticReview: dict):

        self.idSelfie = idSelfie
        self.student = student
        self.dateCreated = dateCreated
        self.url = url
        self.state = state
        self.rejectionReasons = rejectionReasons
        self.rejectionDescription = rejectionDescription
        self.automaticReview = automaticReview

    @staticmethod
    def from_dynamo(selfie_data: dict, student_data: dict):
        """
        Parse data from DynamoDB to SelfieDynamoDTO
        @param selfie_data: dict from DynamoDB
        """



        automatic_review_parsed = {
            "automaticallyRejected": selfie_data['automaticReview']['automaticallyRejected'],
            "labels": [{

                    'confidence': float(i['confidence']),
                    'coords': {'Height': float(i['coords']['Height']),
                               'Left': float(i['coords']['Left']),
                               'Top': float(i['coords']['Top']),
                               'Width': float(i['coords']['Width'])
                               } if i['coords'] else {},
                    'name': i['name'],
                    'parents': i["parents"]} for i in selfie_data['automaticReview']['labels']],
            "rejectionReasons": [REJECTION_REASON[reason] for reason in selfie_data['automaticReview']['rejectionReasons']],
        }


        return SelfieDynamoDTO(
            idSelfie=int((selfie_data['idSelfie'])),
            student=Student(
                ra=student_data['ra'],
                name=student_data['name'],
                email=student_data['email']
            ),
            dateCreated=datetime.fromisoformat(selfie_data['dateCreated']),
            url=selfie_data['url'],
            state=selfie_data['state'],
            rejectionReasons=selfie_data['rejectionReasons'],
            rejectionDescription=selfie_data['rejectionDescription'],
            automaticReview=AutomaticReview(**automatic_review_parsed)
        )

    def to_entity(self):
        """
        Parse data from SelfieDynamoDTO to Selfie
        """
        return Selfie(
            idSelfie=self.idSelfie,
            student=self.student,
            dateCreated=self.dateCreated,
            url=self.url,
            state=STATE[self.state],
            rejectionReasons=[REJECTION_REASON[reason] for reason in self.rejectionReasons],
            rejectionDescription=self.rejectionDescription,
            automaticReview=self.automaticReview
        )
