from src.helpers.errors.usecase_errors import DuplicatedItem
from src.helpers.errors.domain_errors import EntityError
from src.domain.entities.student import Student
from src.infra.repositories.student_repository_mock import IStudentRepository

class CreateStudentUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, student: Student) -> Student:

        if self.repo.get_students_by_ra_or_email(ra = student.ra, email = student.email) != []:
            raise DuplicatedItem("ra or email")

        return self.repo.create_student(student)
         