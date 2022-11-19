from src.shared.environments import Environments
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from .validate_selfie_usecase import ValidateSelfieUsecase
from .validate_selfie_controller import ValidateSelfieController
from src.shared.helpers.http.http_models import HttpRequest


def http_request_handler(event: dict, context):
    repo = Environments.get_student_repo()()
    usecase = ValidateSelfieUsecase(repo)
    controller = ValidateSelfieController(usecase)

    http_request = HttpRequest(body=event["body"],headers=event.get("headers"), query_params=event.get("query_params"))
    response = controller(request=http_request)

    return response