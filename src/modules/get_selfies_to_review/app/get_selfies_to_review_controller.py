from src.shared.domain.entities.student import Student
from src.shared.domain.entities.selfie import Selfie
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound
from .get_selfies_to_review_usecase import GetSelfiesToReviewUsecase
from .get_selfies_to_review_viewmodel import GetSelfiesToReviewViewmodel

class GetSelfiesToReviewController:
    def __init__(self, usecase: GetSelfiesToReviewUsecase):
        self.getSelfiesToReviewUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get('reviewerRa') is None:
                raise MissingParameters('reviewerRa')

            if request.query_params.get('nSelfies') != None:
                if type(request.query_params.get('nSelfies')) != str:
                    raise EntityError('nSelfies')
                elif not request.query_params.get('nSelfies').isdecimal():
                    raise EntityError('nSelfies')


            args = (request.query_params.get('reviewerRa'), int(request.query_params.get('nSelfies'))) if request.query_params.get('nSelfies') != None else (request.query_params.get('reviewerRa'),)
            
            reviews, reviewer = self.getSelfiesToReviewUsecase(
                request.query_params.get('reviewerRa'),
                int(request.query_params.get('nSelfies')) if request.query_params.get('nSelfies') != None else None
            )
                

            viewmodel = GetSelfiesToReviewViewmodel(data=reviews, reviewer=reviewer)
            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
