
from typing import List
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.repositories.student_repository_interface import IStudentRepository


class GetAllSelfiesUsecase:
      def __init__(self, repo:IStudentRepository):
        self.repo = repo
  
      def __call__(self) -> List[Selfie]:
          return self.repo.get_all_selfies()