
from .get_all_students_controller import GetAllStudentsController
from .get_all_students_usecase import GetAllStudentsUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse



def lambda_handler(event, context):
    repo = StudentRepositoryMock() 
    usecase = GetAllStudentsUsecase(repo)
    controller = GetAllStudentsController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

