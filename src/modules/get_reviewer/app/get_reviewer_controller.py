from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound

from .get_reviewer_usecase import GetReviewerUsecase
from .get_reviewer_viewmodel import GetReviewerViewModel


class GetReviewerController:
    def __init__(self, usecase: GetReviewerUsecase):
        self.getReviewerUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get('ra') is None:
                raise MissingParameters('ra')

            reviewer = self.getReviewerUsecase(
                ra=request.query_params["ra"]
            )
            viewmodel = GetReviewerViewModel(reviewer)
            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
