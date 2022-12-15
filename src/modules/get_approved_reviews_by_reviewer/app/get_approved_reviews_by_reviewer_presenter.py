from .get_approved_reviews_by_reviewer_usecase import GetApprovedSelfiesByReviewerUsecase
from .get_approved_reviews_by_reviewer_controller import GetApprovedSelfiesByReviewerController
from src.shared.environments import Environments

from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse



def lambda_handler(event, context):
    repo = Environments.get_student_repo()()
    usecase = GetApprovedSelfiesByReviewerUsecase(repo)
    controller = GetApprovedSelfiesByReviewerController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

