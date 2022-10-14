from src.shared.domain.entities.student import Student
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.http.http_models import BadRequest, Created, HttpRequest, HttpResponse, InternalServerError, NotFound
from src.modules.create_selfie.create_selfie_usecase import CreateSelfieUsecase
from src.modules.create_selfie.create_selfie_viewmodel import CreateSelfieViewModel


class CreateSelfieController:
    def __init__(self, usecase: CreateSelfieUsecase):
        self.createSelfieUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get('ra') is None:
                raise MissingParameters('ra')

            if request.query_params.get('url') is None:
                raise MissingParameters('url')

            student = self.createSelfieUsecase(ra=request.query_params.get('ra'), url=request.query_params.get('url'))
            viewmodel = CreateSelfieViewModel(student)

            return Created(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except DuplicatedItem as err:
            return BadRequest(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
