from src.modules.get_student.get_student_usecase import GetStudentUsecase
from src.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.get_student.get_student_controller import GetStudentController
from src.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound


class Test_GetStudentController:
    def test_get_student_controller(self):
        repo = StudentRepositoryMock()
        usecase = GetStudentUsecase(repo=repo)
        controller = GetStudentController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "21014440",
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['name'] == "Eh o Vilas do Mockas"

    def test_get_student_controller_no_items_found(self):
        repo = StudentRepositoryMock()
        usecase = GetStudentUsecase(repo=repo)
        controller = GetStudentController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "21014441",
        })

        response = controller(request=request)

        assert response.status_code == 404

    def test_get_student_controller_bad_request(self):
        repo = StudentRepositoryMock()
        usecase = GetStudentUsecase(repo=repo)
        controller = GetStudentController(usecase=usecase)

        request = HttpRequest(query_params={
            "email": "eusouoawsboy@amazon.com"
        })

        response = controller(request=request)

        assert response.status_code == 400

    def test_get_student_controller_ra_dash_dot(self):
        repo = StudentRepositoryMock()
        usecase = GetStudentUsecase(repo=repo)
        controller = GetStudentController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "21.014   44-0",
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['name'] == "Eh o Vilas do Mockas"
