from src.modules.delete_selfie.delete_selfie_viewmodel import DeleteSelfieViewModel
from src.helpers.errors.domain_errors import EntityError
from src.helpers.errors.usecase_errors import NoItemsFound
from src.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound
from src.modules.delete_selfie.delete_selfie_usecase import DeleteSelfieUsecase


class DeleteSelfieController:
    def __init__(self, usecase: DeleteSelfieUsecase):
        self.DeleteSelfieUsecase = usecase

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
         
            selfie, student = self.DeleteSelfieUsecase(
                ra = request.query_params.get("ra"),
                idSelfie = int(request.query_params.get("idSelfie")),
            )

            return OK(DeleteSelfieViewModel(data=selfie, student=student).to_dict())

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
