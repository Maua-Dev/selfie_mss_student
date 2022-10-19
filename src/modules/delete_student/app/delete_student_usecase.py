from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.entities.student import Student
from src.shared.infra.repositories.student_repository_mock import IStudentRepository

class DeleteStudentUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str) -> None:
        
        if not Student.validate_ra(ra):
            raise EntityError('ra')

        student = self.repo.delete_student(ra=ra)
        return student
        