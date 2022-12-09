
from .get_rejected_selfies_by_reviewer_viewmodel import GetRejectedSelfiesByReviewerViewModel
from .get_rejected_selfies_by_reviewer_usecase import GetRejectedSelfiesByReviewerUsecase
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound
from src.shared.helpers.errors.domain_errors import EntityError

class GetRejectedSelfiesByReviewerController:
    def __init__(self, usecase: GetRejectedSelfiesByReviewerUsecase):
        self.GetRejectedSelfiesByReviewerUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get("reviewerRa") == None:
                raise MissingParameters("reviewerRa")

            reviewer, reviews = self.GetRejectedSelfiesByReviewerUsecase(
                reviewerRa=request.query_params.get("reviewerRa"),
            )

            viewmodel = GetRejectedSelfiesByReviewerViewModel(listRejectedReviews=reviews, reviewer=reviewer)
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