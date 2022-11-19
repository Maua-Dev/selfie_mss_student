from src.shared.environments import Environments
from .update_student_usecase import UpdateStudentUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from .update_student_controller import UpdateStudentController
from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse



def lambda_handler(event, context):
    repo = Environments.get_student_repo()()
    usecase = UpdateStudentUsecase(repo)
    controller = UpdateStudentController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()



