from src.shared.domain.entities.student import Student
from src.shared.domain.repositories.student_repository_interface import IStudentRepository
from src.shared.helpers.errors.usecase_errors import DuplicatedItem


class CreateStudentUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, student: Student) -> Student:

        if self.repo.get_student(ra = student.ra):
            raise DuplicatedItem("ra")

        return self.repo.create_student(student)
         