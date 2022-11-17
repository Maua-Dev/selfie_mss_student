from .request_upload_selfie_viewmodel import RequestUploadSelfieViewModel
from .request_upload_selfie_usecase import RequestUploadSelfieUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.http.http_models import OK, BadRequest, Forbidden, HttpRequest, HttpResponse, InternalServerError, NotFound


class RequestUploadSelfieController:
    def __init__(self, usecase: RequestUploadSelfieUsecase):
        self.requestUploadSelfieUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get('ra') is None:
                raise MissingParameters('ra')

            if request.body.get('name') is None:
                raise MissingParameters('name')

            if request.body.get('email') is None:
                raise MissingParameters('email')

            presignedPost = self.requestUploadSelfieUsecase(email=request.body.get('email'), name=request.body.get('name'), ra=request.body.get('ra'))
            viewmodel = RequestUploadSelfieViewModel(presignedPost)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except ForbiddenAction as err:
            return Forbidden(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
