from .update_selfie_viewmodel import UpdateSelfieViewModel
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, ForbiddenAction, NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.http.http_models import OK, BadRequest, Conflict, Forbidden, HttpRequest, HttpResponse, InternalServerError, NotFound
from .update_selfie_usecase import UpdateSelfieUsecase
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON

class UpdateSelfieController:
    def __init__(self, usecase: UpdateSelfieUsecase):
        self.updateSelfieUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get('ra') is None:
                raise MissingParameters('ra')
            if request.body.get('idSelfie') is None:
                raise MissingParameters('idSelfie')
            if type(request.body.get('idSelfie')) != str:
                        raise WrongTypeParameter(
                            fieldName="idSelfie",
                            fieldTypeExpected="str",
                            fieldTypeReceived=request.body.get('idSelfie').__class__.__name__
                        )
            if not request.body.get('idSelfie').isdecimal():
                raise EntityError("idSelfie")
            if request.body.get("new_state") not in [state.value for state in STATE] and not request.body.get("new_state") is None :
                raise EntityError("new_state")
            if str(request.body.get("new_rejectionReason")).upper() not in [rejectionReason.value for rejectionReason in REJECTION_REASON]:
                raise EntityError("new_rejectionReason")


            selfie = self.updateSelfieUsecase(
                ra=request.body.get("ra"),
                idSelfie=int(request.body.get("idSelfie")),
                new_state=STATE[request.body.get("new_state")] if not request.body.get("new_state") is None else None,
                new_rejectionReason=REJECTION_REASON[str(request.body.get("new_rejectionReason")).upper()] if not request.body.get("new_rejectionReason") is None else None,
                new_rejectionDescription=request.body.get("new_rejectionDescription")
            )

            viewmodel = UpdateSelfieViewModel(selfie)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except ForbiddenAction as err:
            return Forbidden(body=err.message)

        except DuplicatedItem as err:
            return Conflict(body=err.message)

        except WrongTypeParameter as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
