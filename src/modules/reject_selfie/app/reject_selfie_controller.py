from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound, Forbidden
from .reject_selfie_usecase import RejectSelfieUsecase
from .reject_selfie_viewmodel import RejectSelfieViewModel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter


class RejectSelfieController:
    def __init__(self, usecase: RejectSelfieUsecase):
        self.rejectSelfieUsecase = usecase
        
    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get("reviewerRa") == None:
                raise MissingParameters("reviewerRa")
            if request.body.get("reviewIdentifier") == None:
                raise MissingParameters("reviewIdentifier")
            if "new_rejectionReasons" in request.body:
                if type(request.body.get("new_rejectionReasons")) != list:
                    raise EntityError("new_rejectionReasons")
                elif not all([reason in [rejectionReasons.value for rejectionReasons in REJECTION_REASON] for reason in request.body.get("new_rejectionReasons")]):
                    raise EntityError("new_rejectionReasons")
            
            parsedIdReviewParams = request.body.get("reviewIdentifier").split('-') #studentRa-idSelfie-idReview
            
            if len(parsedIdReviewParams) != 3:
                raise EntityError("reviewIdentifier")
            
            if not parsedIdReviewParams[1].isdecimal():
                raise EntityError("idSelfie")
            
            if not parsedIdReviewParams[2].isdecimal():
                raise EntityError("idReview")
                
                
            
            review = self.rejectSelfieUsecase(
                reviewerRa=request.body.get("reviewerRa"),
                studentRa=parsedIdReviewParams[0],
                idSelfie=int(parsedIdReviewParams[1]),
                idReview=int(parsedIdReviewParams[2]),
                new_rejectionReasons=[REJECTION_REASON[reason.upper()] for reason in request.body.get("new_rejectionReasons")] if not request.body.get("new_rejectionReasons") is None else None,
                new_rejectionDescription=request.body.get("new_rejectionDescription")
            )
            viewmodel = RejectSelfieViewModel(review=review)
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
