from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, ForbiddenAction, NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.http.http_models import BadRequest, Created, HttpRequest, HttpResponse, InternalServerError, NotFound, Conflict, Forbidden
from .create_selfie_usecase import CreateSelfieUsecase
from .create_selfie_viewmodel import CreateSelfieViewModel


class CreateSelfieController:
    def __init__(self, usecase: CreateSelfieUsecase):
        self.createSelfieUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get('ra') is None:
                raise MissingParameters('ra')

            if request.body.get('url') is None:
                raise MissingParameters('url')

            if request.body.get('automaticReview') is None:
                raise MissingParameters('automaticReview')
            
            selfie = self.createSelfieUsecase(ra=request.body.get('ra'), url=request.body.get('url'), automaticReview=request.body.get("automaticReview"))
            viewmodel = CreateSelfieViewModel(selfie)

            return Created(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)
        
        except ForbiddenAction as err:
            return Forbidden(body=err.message)

        except DuplicatedItem as err:
            return Conflict(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
