from src.shared.environments import Environments
from .get_reviewer_usecase import GetReviewerUsecase
from .get_reviewer_controller import GetReviewerController
from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse



def lambda_handler(event, context):
    repo = Environments.get_student_repo()()
    usecase = GetReviewerUsecase(repo)
    controller = GetReviewerController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

