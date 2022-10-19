from src.modules.get_student.app.get_student_controller import GetStudentController
from src.modules.get_student.app.get_student_usecase import GetStudentUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock

from src.shared.helpers.http.http_models import HttpRequest


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

        assert response.body == "No items found for Student"
        assert response.status_code == 404

    def test_get_student_controller_bad_request(self):
        repo = StudentRepositoryMock()
        usecase = GetStudentUsecase(repo=repo)
        controller = GetStudentController(usecase=usecase)

        request = HttpRequest(query_params={
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is missing"

    def test_get_student_controller_bad_request_int(self):
        repo = StudentRepositoryMock()
        usecase = GetStudentUsecase(repo=repo)
        controller = GetStudentController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": 21014440,
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "ra must be a string"

    def test_get_student_controller_bad_request_invalid_ra(self):
        repo = StudentRepositoryMock()
        usecase = GetStudentUsecase(repo=repo)
        controller = GetStudentController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "2101444",
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is not valid"
