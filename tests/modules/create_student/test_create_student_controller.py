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

        lenBefore = len(repo.students)

        response = controller(request=request)

        expected = Student(
            ra="20006110",
            name="Ai Rubio",
            email="aii@rubio.com"
        )

        lenAfter = lenBefore + 1

        assert len(repo.students) == lenAfter
        assert repo.students[lenAfter - 1].ra == expected.ra
        assert repo.students[lenAfter - 1].name == expected.name
        assert repo.students[lenAfter - 1].email == expected.email
        assert response.status_code == 201

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
