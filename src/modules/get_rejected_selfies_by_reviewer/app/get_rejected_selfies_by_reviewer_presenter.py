from .get_rejected_selfies_by_reviewer_usecase import GetRejectedSelfiesByReviewerUsecase
from .get_rejected_selfies_by_reviewer_controller import GetRejectedSelfiesByReviewerController
from src.shared.environments import Environments

from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse



def lambda_handler(event, context):
    repo = Environments.get_student_repo()()
    usecase = GetRejectedSelfiesByReviewerUsecase(repo)
    controller = GetRejectedSelfiesByReviewerController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

