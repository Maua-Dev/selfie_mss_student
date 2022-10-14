from src.modules.get_student.get_student_usecase import GetStudentUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.get_student.get_student_controller import GetStudentController
from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse



def lambda_handler(event, context):
    repo = StudentRepositoryMock() 
    usecase = GetStudentUsecase(repo)
    controller = GetStudentController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

