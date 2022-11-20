from src.shared.domain.entities.student import Student
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.repositories.selfie_repository_interface import ISelfieRepository
from src.shared.domain.repositories.student_repository_interface import IStudentRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound

class RequestUploadSelfieUsecase:
    def __init__(self, repoSelfie:ISelfieRepository, repoStudent:IStudentRepository):
        self.repoSelfie = repoSelfie
        self.repoStudent = repoStudent

    def __call__(self, ra: str, name: str, email: str) -> dict:

        if not Student.validate_ra(ra):
            raise EntityError('ra')
        
        if not Student.validate_email(email):
            raise EntityError('email')

        if not Student.validate_name(name):
            raise EntityError('name')

        selfies, student = self.repoStudent.get_selfies_by_ra(ra=ra)

        if len(selfies) > 0 and not all([selfie.state == STATE.DECLINED for selfie in selfies]):
            raise ForbiddenAction("Student")        
        else: 
            presignedPost = self.repoSelfie.request_upload_selfie(ra=ra, name=name, email=email)


        return presignedPost