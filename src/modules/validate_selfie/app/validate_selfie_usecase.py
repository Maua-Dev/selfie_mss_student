from typing import Dict
from src.shared.domain.repositories.student_repository_interface import IStudentRepository

class ValidateSelfieUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, rekognitionResult: dict, ra:str, url: str) -> Dict:
        pass
        
    