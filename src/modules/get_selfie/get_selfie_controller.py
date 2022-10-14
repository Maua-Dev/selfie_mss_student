from dataclasses import field
from multiprocessing.sharedctypes import Value
from src.shared.domain.entities.student import Student
from src.shared.domain.entities.selfie import Selfie
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound
from src.modules.get_selfie.get_selfie_viewmodel import GetSelfieViewModel
from src.modules.get_selfie.get_selfie_usecase import GetSelfieUsecase


class GetSelfieController:
    def __init__(self, usecase: GetSelfieUsecase):
        self.getSelfieUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get('ra') is None:
                raise MissingParameters('ra')

            if request.query_params.get('idSelfie') is None:
                raise MissingParameters('idSelfie')


            if type(request.query_params.get('idSelfie')) != str:
                raise WrongTypeParameter(
                    fieldName="idSelfie",
                    fieldTypeExpected="str",
                    fieldTypeReceived=request.query_params.get('idSelfie').__class__.__name__
                )
            if not request.query_params.get('idSelfie').isdecimal():
                raise EntityError("idSelfie")
                    
            
            selfie = self.getSelfieUsecase(
                ra=request.query_params.get('ra'),
                idSelfie=int(request.query_params.get('idSelfie'))
                )
            viewmodel = GetSelfieViewModel(selfie)
            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
