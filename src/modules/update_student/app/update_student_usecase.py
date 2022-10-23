from src.shared.domain.repositories.student_repository_interface import IStudentRepository
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterError
from src.shared.domain.entities.student import Student

class UpdateStudentUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str, new_name: str = None, new_email: str = None) -> Student:
        if not Student.validate_ra(ra):
            raise EntityError('ra')

        if new_email != None and not Student.validate_email(email=new_email):
            raise EntityError('email')

        if new_name != None and not Student.validate_name(name=new_name):
            raise EntityParameterError(f"name length must be bigger than {Student.MIN_NAME_LENGTH}")

        return self.repo.update_student(ra=ra, new_name=new_name, new_email=new_email)
        