import datetime
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction
from src.shared.domain.entities.student import Student
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.repositories.student_repository_interface import IStudentRepository
from src.shared.helpers.functions.read_automatic_review import read_automatic_review
class CreateSelfieUsecase:
    def __init__(self, repo:IStudentRepository):
        self.repo = repo
        
    def __call__(self, ra: str, url: str, automaticReview: dict) -> Selfie:
        
        if not Student.validate_ra(ra):
            raise EntityError('ra')
        
        if type(automaticReview) != dict:
            raise EntityError("automaticReview")
        
        student = self.repo.get_student(ra=ra)
        if student == None:
            raise NoItemsFound("ra")
    
        if self.repo.check_student_has_approved_selfie(ra=ra):       
            raise ForbiddenAction("Student")

        automaticReviewInstance = read_automatic_review(automaticReview)

        selfie = Selfie(
            student=student,
            dateCreated=datetime.datetime.now(),
            url=url,
            state=STATE.PENDING_REVIEW if not automaticReviewInstance.automaticallyRejected else STATE.DECLINED,
            idSelfie=len(self.repo.get_selfies_by_ra(ra=ra)[0]),
            rejectionReasons=[REJECTION_REASON.NONE] if not automaticReviewInstance.automaticallyRejected else automaticReviewInstance.rejectionReasons,
            rejectionDescription=None if not automaticReviewInstance.automaticallyRejected else "auto-rejected by AI",
            automaticReview=automaticReviewInstance

        )
        
        selfie = self.repo.create_selfie(selfie=selfie)
        
        return selfie



