from src.domain.enums.state_enum import STATE
from src.domain.entities.selfie import Selfie

class GetSelfieViewModel:
    idSelfie: int
    dateUpload: str
    url: str
    state: STATE

    def __init__(self, selfie: Selfie):
        self.idSelfie = selfie.idSelfie
        self.dateUpload = selfie.dateUpload
        self.url = selfie.url
        self.state = selfie.state

    def to_dict(self) -> dict:
        return {
            "idSelfie" : self.idSelfie,
            "dateUpload" : self.dateUpload.isoformat(),
            "url" : self.url,
            "state" : self.state.value,
            "message": "the selfie was retriven"
        }