from src.helpers.errors.usecase_errors import NoItemsFound
from src.domain.entities.student import Student
from src.infra.repositories.student_repository_mock import IStudentRepository

class GetStudentUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra:str) -> Student:
        student = self.repo.get_student(ra=ra)
        
        if student == None:
            raise NoItemsFound("get_student")
        
        return student
        
        