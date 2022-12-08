from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound, Forbidden
from .approve_selfie_usecase import ApproveSelfieUsecase
from .approve_selfie_viewmodel import ApproveSelfieViewModel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter


class ApproveSelfieController:
    def __init__(self, usecase: ApproveSelfieUsecase):
        self.approveSelfieUsecase = usecase
        
    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get("reviewerRa") == None:
                raise MissingParameters("reviewerRa")
            if request.body.get("reviewIdentifier") == None:
                raise MissingParameters("reviewIdentifier")
        
            
            parsedIdReviewParams = request.body.get("reviewIdentifier").split('-') #studentRa-idSelfie-idReview
            
            if len(parsedIdReviewParams) != 3:
                raise EntityError("reviewIdentifier")
            
            if not parsedIdReviewParams[1].isdecimal():
                raise EntityError("idSelfie")
            
            if not parsedIdReviewParams[2].isdecimal():
                raise EntityError("idReview")
                
                
            
            review = self.approveSelfieUsecase(
                reviewerRa=request.body.get("reviewerRa"),
                studentRa=parsedIdReviewParams[0],
                idSelfie=int(parsedIdReviewParams[1]),
                idReview=int(parsedIdReviewParams[2])
            )
            viewmodel = ApproveSelfieViewModel(review=review)
            return OK(viewmodel.to_dict())
        
        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)
        
        except ForbiddenAction as err:
            return Forbidden(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
