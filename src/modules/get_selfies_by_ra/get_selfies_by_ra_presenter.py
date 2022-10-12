from src.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.modules.get_selfies_by_ra.get_selfies_by_ra_controller import GetSelfiesByRaController
from src.modules.get_selfies_by_ra.get_selfies_by_ra_usecase import GetSelfiesByRaUsecase



def lambda_handler(event, context):
    repo = StudentRepositoryMock() 
    usecase = GetSelfiesByRaUsecase(repo)
    controller = GetSelfiesByRaController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

