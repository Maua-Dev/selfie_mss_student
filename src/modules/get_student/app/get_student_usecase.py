from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.entities.student import Student
from src.shared.domain.repositories.student_repository_interface import IStudentRepository
class GetStudentUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str) -> Student:

        if not Student.validate_ra(ra):
            raise EntityError('ra')

        student = self.repo.get_student(ra=ra)
        
        if student == None:
            raise NoItemsFound("Student")
        
        return student