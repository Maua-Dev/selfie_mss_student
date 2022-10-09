from src.helpers.errors.domain_errors import EntityError
from src.helpers.errors.usecase_errors import NoItemsFound
from src.domain.entities.student import Student
from src.infra.repositories.student_repository_mock import IStudentRepository

class DeleteStudentUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str) -> None:
        
        if not Student.validate_ra(ra):
            raise EntityError('ra')

        self.repo.delete_student(ra=ra)
        