from src.helpers.errors.domain_errors import EntityError
from src.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from src.domain.entities.student import Student
from src.infra.repositories.student_repository_mock import IStudentRepository

class UpdateStudentUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str, new_name: str = None, new_email: str = None) -> Student:
        if not Student.validate_ra(ra):
            raise EntityError('ra')

        if new_email != None and not Student.validate_email(email=new_email):
            raise EntityError('email')

        return self.repo.update_student(ra=ra, new_name=new_name, new_email=new_email)
        