from src.helpers.errors.domain_errors import EntityError
from src.domain.entities.student import Student
from src.infra.repositories.student_repository_mock import IStudentRepository

class CreateStudentUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str, name: str, email: str) -> None:

        if not Student.validate_ra(ra):
            raise EntityError('ra')

        if not Student.validate_email(email):
            raise EntityError('email')

        self.repo.create_student(ra=ra, name=name, email=email)
        