from src.modules.update_student.update_student_view_model import UpdateStudentViewModel
from src.helpers.errors.domain_errors import EntityError
from src.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from src.helpers.errors.controller_errors import MissingParameters
from src.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound
from src.modules.update_student.update_student_usecase import UpdateStudentUsecase


class UpdateStudentController:
    def __init__(self, usecase: UpdateStudentUsecase):
        self.updateStudentUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get('ra') is None:
                raise MissingParameters('ra')
            student = self.updateStudentUsecase(
                ra=request.query_params.get("ra"),
                new_name=request.query_params.get("new_name"),
                new_email=request.query_params.get("new_email")
            )

            viewmodel = UpdateStudentViewModel(student)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except DuplicatedItem as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
