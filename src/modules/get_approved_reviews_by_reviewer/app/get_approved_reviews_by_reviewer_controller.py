
from .get_approved_reviews_by_reviewer_viewmodel import GetApprovedSelfiesByReviewerViewModel
from .get_approved_reviews_by_reviewer_usecase import GetApprovedSelfiesByReviewerUsecase
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound
from src.shared.helpers.errors.domain_errors import EntityError

class GetApprovedSelfiesByReviewerController:
    def __init__(self, usecase: GetApprovedSelfiesByReviewerUsecase):
        self.GetApprovedSelfiesByReviewerUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get("reviewerRa") == None:
                raise MissingParameters("reviewerRa")

            reviewer, reviews = self.GetApprovedSelfiesByReviewerUsecase(
                reviewerRa=request.query_params.get("reviewerRa"),
            )

            viewmodel = GetApprovedSelfiesByReviewerViewModel(listApprovedReviews=reviews, reviewer=reviewer)
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