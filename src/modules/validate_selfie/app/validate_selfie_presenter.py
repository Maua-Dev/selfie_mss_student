from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from .validate_selfie_usecase import ValidateSelfieUsecase
from .validate_selfie_controller import ValidateSelfieController
from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest


def http_request_handler(event: dict, context):
    repo = StudentRepositoryMock()
    usecase = ValidateSelfieUsecase(repo)
    controller = ValidateSelfieController(usecase)

    response = controller(request=event)

    return response