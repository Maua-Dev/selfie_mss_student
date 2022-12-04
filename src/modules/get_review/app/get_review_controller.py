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
            if request.query_params.get("idReview") == None:
                raise MissingParameters("idReview")
        
            if type(request.query_params.get("idReview")) != str:
                raise WrongTypeParameter(
                    fieldName="idReview",
                    fieldTypeExpected="str",
                    fieldTypeReceived=request.query_params.get('idReview').__class__.__name__
                )
            if not request.query_params.get("idReview").isdecimal():
                raise EntityError("idReview")
            
            review = self.getReviewUsecase(
                reviewerRa=request.query_params.get("reviewerRa"),
                idReview=int(request.query_params.get("idReview"))
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
