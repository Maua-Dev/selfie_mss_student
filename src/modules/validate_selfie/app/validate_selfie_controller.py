from src.shared.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError
from .validate_selfie_usecase import ValidateSelfieUsecase
from .validate_selfie_viewmodel import ValidateSelfieViewModel
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.domain.entities.student import Student
from src.shared.domain.entities.selfie import Selfie
class ValidateSelfieController:
    def __init__(self, usecase: ValidateSelfieUsecase):
        self.validateSelfieUsecase = usecase
        
    def __call__(self, request:HttpRequest) -> HttpResponse:
        try:
            if request.body.get('ra') is None:
                raise EntityError('ra')
            if not Student.validate_ra(request.body.get('ra')):
                raise EntityError('ra')
            if request.body.get('url') is None:
                raise EntityError('url')
            if not Selfie.validate_url(request.body.get('url')):
                raise EntityError("url")
            if request.body.get('rekognitionResult') is None:
                raise EntityError("rekognitionResult")
            
            automaticReview = self.validateSelfieUsecase(rekognitionResult=request.body.get('rekognitionResult'))
            
            viewmodel = ValidateSelfieViewModel(data=automaticReview, ra=request.body.get('ra'), url=request.body.get('url'))
            
            return OK(viewmodel.to_dict())
            
            
        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
