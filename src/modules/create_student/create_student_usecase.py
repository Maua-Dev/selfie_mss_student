from src.domain.repositories.student_repository_interface import IStudentRepository
from src.helpers.errors.usecase_errors import DuplicatedItem
from src.helpers.errors.domain_errors import EntityError
from src.domain.entities.student import Student

class CreateStudentUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, student: Student) -> Student:

        if self.repo.get_student(ra = student.ra):
            raise DuplicatedItem("ra")

        return self.repo.create_student(student)
         