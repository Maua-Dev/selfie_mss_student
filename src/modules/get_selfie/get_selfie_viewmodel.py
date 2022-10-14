from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.entities.selfie import Selfie

class GetSelfieViewModel:
    idSelfie: int
    dateUpload: str
    url: str
    state: STATE
    rejectionReason: REJECTION_REASON
    rejectionDescription: str

    def __init__(self, selfie: Selfie):
        self.idSelfie = selfie.idSelfie
        self.dateUpload = selfie.dateUpload
        self.url = selfie.url
        self.state = selfie.state
        self.rejectionReason =  selfie.rejectionReason
        self.rejectionDescription = selfie.rejectionDescription

    def to_dict(self) -> dict:
        return {
            "idSelfie" : self.idSelfie,
            "dateUpload" : self.dateUpload.isoformat(),
            "url" : self.url,
            "state" : self.state.value,
            "rejectionReason": self.rejectionReason.value,
            "rejectionDescription": self.rejectionDescription,
            "message": "the selfie was retriven"
        }