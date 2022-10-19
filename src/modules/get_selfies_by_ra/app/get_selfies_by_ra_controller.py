from src.shared.domain.entities.student import Student
from src.shared.domain.entities.selfie import Selfie
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound
from .get_selfies_by_ra_viewmodel import GetSelfiesByRaViewModel
from .get_selfies_by_ra_usecase import GetSelfiesByRaUsecase


class GetSelfiesByRaController:
    def __init__(self, usecase: GetSelfiesByRaUsecase):
        self.getSelfiesByRaUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get('ra') is None:
                raise MissingParameters('ra')

            selfies, student = self.getSelfiesByRaUsecase(
                ra=request.query_params.get('ra')
            )
            viewmodel = GetSelfiesByRaViewModel(selfies, student)
            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
