from src.modules.create_student.create_student_usecase import CreateStudentUsecase
from src.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.create_student.create_student_controller import CreateStudentController
from src.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


def lambda_handler(event, context):
    repo = StudentRepositoryMock()
    usecase = CreateStudentUsecase(repo)
    controller = CreateStudentController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
