from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.student import Student
from src.shared.domain.repositories.selfie_repository_interface import ISelfieRepository
from src.shared.helpers.errors.domain_errors import EntityError

class RequestUploadSelfieUsecase:
    def __init__(self, repo:ISelfieRepository):
        self.repo = repo
        
    def __call__(self, ra: str, name: str, email: str) -> dict:

        if not Student.validate_ra(ra):
            raise EntityError('ra')
        
        if not Student.validate_email(email):
            raise EntityError('email')

        if not Student.validate_name(name):
            raise EntityError('name')

        presigned_post = self.repo.request_upload_selfie(ra=ra, name=name, email=email)

        return presigned_post