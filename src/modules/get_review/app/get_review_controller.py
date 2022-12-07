from .get_review_usecase import GetReviewUsecase
from .get_review_viewmodel import GetReviewViewModel
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound
from src.shared.helpers.errors.domain_errors import EntityError

class GetReviewController:
    def __init__(self, usecase: GetReviewUsecase):
        self.getReviewUsecase = usecase
        
    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get("reviewerRa") == None:
                raise MissingParameters("reviewerRa")
            if request.query_params.get("reviewIdentifier") == None:
                raise MissingParameters("reviewIdentifier")
        
            
            parsedIdReviewParams = request.query_params.get("reviewIdentifier").split('-') #studentRa-idSelfie-idReview
            
            if len(parsedIdReviewParams) != 3:
                raise EntityError("reviewIdentifier")
            
            if not parsedIdReviewParams[1].isdecimal():
                raise EntityError("idSelfie")
            
            if not parsedIdReviewParams[2].isdecimal():
                raise EntityError("idReview")
                
                
            
            review = self.getReviewUsecase(
                reviewerRa=request.query_params.get("reviewerRa"),
                studentRa=parsedIdReviewParams[0],
                idSelfie=int(parsedIdReviewParams[1]),
                idReview=int(parsedIdReviewParams[2])
            )
            viewmodel = GetReviewViewModel(review=review)
            return OK(viewmodel.to_dict())
        
        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
