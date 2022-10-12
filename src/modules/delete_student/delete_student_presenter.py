from src.modules.delete_student.delete_student_usecase import DeleteStudentUsecase
from src.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.delete_student.delete_student_controller import DeleteStudentController
from src.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse



def lambda_handler(event, context):
    repo = StudentRepositoryMock() 
    usecase = DeleteStudentUsecase(repo)
    controller = DeleteStudentController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()



