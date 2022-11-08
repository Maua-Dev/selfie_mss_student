from abc import ABC, abstractmethod


class ISelfieRepository(ABC):

    @abstractmethod
    def request_upload_selfie(self, ra: str, name: str, email:str) -> dict:
        pass
