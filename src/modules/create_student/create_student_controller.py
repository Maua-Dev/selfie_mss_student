from src.shared.domain.entities.student import Student
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.http.http_models import BadRequest, Conflict, Created, HttpRequest, HttpResponse, InternalServerError, NotFound
from src.modules.create_student.create_student_usecase import CreateStudentUsecase
from src.modules.create_student.create_student_view_model import CreateStudentViewModel


class CreateStudentController:
    def __init__(self, usecase: CreateStudentUsecase):
        self.createStudentUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get('ra') is None:
                raise MissingParameters('ra')

            if request.query_params.get('name') is None:
                raise MissingParameters('name')

            if request.query_params.get('email') is None:
                raise MissingParameters('email')

            studentParam= Student(
                ra=request.query_params["ra"],
                name=request.query_params["name"],
                email=request.query_params["email"]
            )

            student = self.createStudentUsecase(studentParam)
            viewmodel = CreateStudentViewModel(student)

            return Created(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except DuplicatedItem as err:
            return Conflict(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
