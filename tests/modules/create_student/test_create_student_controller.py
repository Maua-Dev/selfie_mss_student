from src.domain.entities.student import Student
from src.modules.create_student.create_student_usecase import CreateStudentUsecase
from src.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.create_student.create_student_controller import CreateStudentController
from src.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound


class Test_CreateStudentController:

    def test_create_student_controller(self):
        repo = StudentRepositoryMock()
        usecase = CreateStudentUsecase(repo=repo)
        controller = CreateStudentController(usecase=usecase)
        request = HttpRequest(query_params={
            "ra": "20006110",
            "name": "Ai Rubio",
            "email": "aii@rubio.com"
        })


        response = controller(request=request)

        assert response.status_code == 201
        assert response.body['ra'] == "20006110"
        assert response.body['name'] == "Ai Rubio"
        assert response.body['message'] == "User was created successfully"

    def test_create_student_controller_missing_ra(self):
        repo = StudentRepositoryMock()
        usecase = CreateStudentUsecase(repo=repo)
        controller = CreateStudentController(usecase=usecase)
        request = HttpRequest(query_params={
            "name": "Maria Vernasqui",
            "email": "maluzinha@teamo.com",
        })
        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is missing"

    def test_create_student_controller_missing_name(self):
        repo = StudentRepositoryMock()
        usecase = CreateStudentUsecase(repo=repo)
        controller = CreateStudentController(usecase=usecase)
        request = HttpRequest(query_params={
            "ra": "2100208",
            "email": "maluzinha@teamo.com",
        })
        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field name is missing"

    def test_create_student_controller_missing_email(self):
        repo = StudentRepositoryMock()
        usecase = CreateStudentUsecase(repo=repo)
        controller = CreateStudentController(usecase=usecase)
        request = HttpRequest(query_params={
            "ra": "2100208",
            "name": "Maria Vernasqui",
        })
        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field email is missing"

    def test_create_student_controller_bad_request_int(self):
        repo = StudentRepositoryMock()
        usecase = CreateStudentUsecase(repo=repo)
        controller = CreateStudentController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": 21002088,
            "name": "Maria Vernasqui",
            "email": "maluzinha@teamo.com",
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "ra must be a string"

    def test_create_student_controller_bad_request_invalid_ra_dash(self):
        repo = StudentRepositoryMock()
        usecase = CreateStudentUsecase(repo=repo)
        controller = CreateStudentController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "2100208-8",
            "name": "Maria Vernasqui",
            "email": "maluzinha@teamo.com",
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is not valid"

    def test_create_student_controller_bad_request_invalid_ra_wrong_len(self):
        repo = StudentRepositoryMock()
        usecase = CreateStudentUsecase(repo=repo)
        controller = CreateStudentController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "2100208",
            "name": "Maria Vernasqui",
            "email": "maluzinha@teamo.com",
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is not valid"

    def test_create_student_controller_bad_request_invalid_email_without_at(self):
        repo = StudentRepositoryMock()
        usecase = CreateStudentUsecase(repo=repo)
        controller = CreateStudentController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "21002088",
            "name": "Maria Vernasqui",
            "email": "maluzinhateamo.com",
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field email is not valid"

    def test_create_student_controller_bad_request_invalid_email_without_final_dot(self):
        repo = StudentRepositoryMock()
        usecase = CreateStudentUsecase(repo=repo)
        controller = CreateStudentController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "21002088",
            "name": "Maria Vernasqui",
            "email": "maluzinha@teamocom",
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field email is not valid"

    def test_create_student_controller_bad_request_invalid_name(self):
        repo = StudentRepositoryMock()
        usecase = CreateStudentUsecase(repo=repo)
        controller = CreateStudentController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "21002088",
            "name": "",
            "email": "maluzinha@teamo.com",
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field name is not valid"

    def test_create_student_controller_bad_request_duplicated_ra(self):
        repo = StudentRepositoryMock()
        usecase = CreateStudentUsecase(repo=repo)
        controller = CreateStudentController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "21014442",
            "name": "Maria Luiza te amo",
            "email": "maluzinha@teamo.com",
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "The item alredy exists for this ra"
