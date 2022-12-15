import json
from datetime import datetime
from decimal import Decimal

from src.shared.domain.entities.automatic_review import AutomaticReview
from src.shared.domain.entities.label import Label
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.student import Student
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE


class SelfieDynamoDTO:
    idSelfie: int
    student: Student
    dateCreated: datetime
    url: str
    state: STATE
    rejectionReasons: list[REJECTION_REASON]
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
    def from_dynamo(selfie_data: dict, student_data: dict) -> "SelfieDynamoDTO":
        """
        Parse data from DynamoDB to SelfieDynamoDTO
        @param selfie_data: dict from DynamoDB
        """



        automatic_review_parsed = {
            "automaticallyRejected": selfie_data['automaticReview']['automaticallyRejected'],
            "labels": [Label(
                    confidence=float(i['confidence']),
                    coords={'Height': float(i['coords']['Height']),
                               'Left': float(i['coords']['Left']),
                               'Top': float(i['coords']['Top']),
                               'Width': float(i['coords']['Width'])
                               } if i['coords'] else {},
                    name=i['name'],
                    parents=i["parents"]) for i in selfie_data['automaticReview']['labels']],
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
            state=STATE[selfie_data['state']],
            rejectionReasons= [REJECTION_REASON[reason] for reason in selfie_data['rejectionReasons']],
            rejectionDescription=selfie_data['rejectionDescription'],
            automaticReview=AutomaticReview(**automatic_review_parsed)
        )

    def to_entity(self) -> Selfie:
        """
        Parse data from SelfieDynamoDTO to Selfie
        """
        return Selfie(
            idSelfie=self.idSelfie,
            student=self.student,
            dateCreated=self.dateCreated,
            url=self.url,
            state=self.state,
            rejectionReasons=self.rejectionReasons,
            rejectionDescription=self.rejectionDescription,
            automaticReview=self.automaticReview
        )

    @staticmethod
    def from_entity(selfie: Selfie) -> "SelfieDynamoDTO":
        """
        Parse data from Selfie to SelfieDynamoDTO
        """
        return SelfieDynamoDTO(
            idSelfie=selfie.idSelfie,
            student=selfie.student,
            dateCreated=selfie.dateCreated,
            url=selfie.url,
            state=selfie.state,
            rejectionReasons=selfie.rejectionReasons,
            rejectionDescription=selfie.rejectionDescription,
            automaticReview=selfie.automaticReview
        )

    def to_dynamo(self) -> dict:
        """
        Parse data from SelfieDynamoDTO to DynamoDB format
        """
        return {
            "entity": "selfie",
            "idSelfie": Decimal(str(self.idSelfie)),
            "dateCreated": self.dateCreated.isoformat(),
            "url": self.url,
            "state": self.state.value,
            "rejectionReasons": [reason.value for reason in self.rejectionReasons],
            "rejectionDescription": self.rejectionDescription,
            "automaticReview": {
                "automaticallyRejected": self.automaticReview.automaticallyRejected,
                "labels": [{
                    'confidence': Decimal(str(i.confidence)),
                    'coords': {'Height': Decimal(str(i.coords['Height'])),
                               'Left': Decimal(str(i.coords['Left'])),
                               'Top': Decimal(str(i.coords['Top'])),
                               'Width': Decimal(str(i.coords['Width']))
                               } if i.coords else {},
                    'name': i.name,
                    'parents': i.parents} for i in self.automaticReview.labels],
                "rejectionReasons": [reason.value for reason in self.automaticReview.rejectionReasons],
            },
            "GSI1-SK": f"selfie#{self.student.ra}#{self.idSelfie}",
            "GSI1-PK": f"{self.state.value}",
        }




    def __repr__(self):
        return json.dumps(self.__dict__, indent=4, default=str)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

