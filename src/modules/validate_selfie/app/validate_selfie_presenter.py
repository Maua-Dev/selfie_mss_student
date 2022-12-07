from src.shared.environments import Environments
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from .validate_selfie_usecase import ValidateSelfieUsecase
from .validate_selfie_controller import ValidateSelfieController
from src.shared.helpers.http.http_models import HttpRequest

repo = Environments.get_student_repo()()
usecase = ValidateSelfieUsecase(repo)
controller = ValidateSelfieController(usecase)


def lambda_handler(event: dict, context):
    body = {}

    body['ra'] = event.get('bucketMetadataResult').get('Metadata').get('ra')
    body['name'] = event.get('bucketMetadataResult').get('Metadata').get('name')
    body['email'] = event.get('bucketMetadataResult').get('Metadata').get('email')
    body[
        'url'] = f"https://{event.get('detail').get('bucket').get('name')}.s3.{Environments.get_envs().region}.amazonaws.com/{event.get('detail').get('object').get('key')}"
    body['rekognitionResult'] = event.get('rekognitionResult')

    http_request = HttpRequest(body=body, headers=event.get("headers"), query_params=event.get("query_params"))
    response = controller(request=http_request)

    return response
