from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.modules.delete_selfie.delete_selfie_controller import DeleteSelfieController
from src.modules.delete_selfie.delete_selfie_usecase import DeleteSelfieUsecase



def lambda_handler(event, context):
    repo = StudentRepositoryMock() 
    usecase = DeleteSelfieUsecase(repo)
    controller = DeleteSelfieController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

