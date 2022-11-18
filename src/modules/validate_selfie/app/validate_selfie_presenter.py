from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from .validate_selfie_usecase import ValidateSelfieUsecase
from .validate_selfie_controller import ValidateSelfieController
from src.shared.helpers.http.http_models import HttpRequest


def http_request_handler(event: dict, context):
    repo = StudentRepositoryMock()
    usecase = ValidateSelfieUsecase(repo)
    controller = ValidateSelfieController(usecase)

    http_request = HttpRequest(body=event["body"])
    response = controller(request=http_request)

    return response