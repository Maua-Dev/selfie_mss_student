from src.helpers.errors.domain_errors import EntityError
from src.helpers.errors.usecase_errors import NoItemsFound
from src.domain.entities.student import Student
from src.infra.repositories.student_repository_mock import IStudentRepository

class UpdateStudentUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str, new_name: str = None, new_email: str = None):
        
        if not Student.validate_ra(ra):
            raise EntityError('ra')

        self.repo.update_student(ra=ra, new_name=new_name, new_email=new_email)
        