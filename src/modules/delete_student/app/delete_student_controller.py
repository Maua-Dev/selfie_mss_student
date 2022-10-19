from .delete_student_viewmodel import DeleteStudentViewModel
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound
from .delete_student_usecase import DeleteStudentUsecase


class DeleteStudentController:
    def __init__(self, usecase: DeleteStudentUsecase):
        self.deleteStudentUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get('ra') is None:
                raise MissingParameters('ra')
            
            student = self.deleteStudentUsecase(
                ra=request.body.get("ra"),
            )
            return OK(DeleteStudentViewModel(student).to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
