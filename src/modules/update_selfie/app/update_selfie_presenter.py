from .update_selfie_usecase import UpdateSelfieUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from .update_selfie_controller import UpdateSelfieController
from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse



def lambda_handler(event, context):
    repo = StudentRepositoryMock() 
    usecase = UpdateSelfieUsecase(repo)
    controller = UpdateSelfieController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()



