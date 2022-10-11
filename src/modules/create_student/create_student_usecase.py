from src.helpers.errors.domain_errors import EntityError
from src.domain.entities.student import Student
from src.infra.repositories.student_repository_mock import IStudentRepository

class CreateStudentUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, student: Student) -> None:

        # if not Student.validate_ra(Student.ra):
        #     raise EntityError('ra')

        # if not Student.validate_email(Student.email):
        #     raise EntityError('email')

        self.repo.create_student(student)
        