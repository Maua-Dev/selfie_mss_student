from src.domain.entities.student import Student
from src.modules.update_student.update_student_usecase import UpdateStudentUsecase
from src.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.update_student.update_student_controller import UpdateStudentController
from src.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound

class Test_UpdateStudentController:

    def test_update_student_controller_ra_only(self):
        repo = StudentRepositoryMock()
        usecase = UpdateStudentUsecase(repo=repo)
        controller = UpdateStudentController(usecase=usecase)
        request = HttpRequest(query_params={
            "ra": "21014443",
        })
        response = controller(request=request)

        expected = Student(
            ra="21014443",
            name="Guirão",
            email="acreditaquesousollertambem@yahoo.com"
        )

        assert response.status_code == 200
        assert repo.students[2].ra == expected.ra
        assert repo.students[2].name == expected.name
        assert repo.students[2].email == expected.email

    def test_update_student_controller_ra_name(self):
        repo = StudentRepositoryMock()
        usecase = UpdateStudentUsecase(repo=repo)
        controller = UpdateStudentController(usecase=usecase)
        request = HttpRequest(query_params={
            "ra": "21014443",
            "new_name": "Volkswagen",
        })
        response = controller(request=request)

        expected = Student(
            ra="21014443",
            name="Volkswagen",
            email="acreditaquesousollertambem@yahoo.com"
        )

        assert response.status_code == 200
        assert repo.students[2].ra == expected.ra
        assert repo.students[2].name == expected.name
        assert repo.students[2].email == expected.email

    def test_update_student_controller_ra_email(self):
        repo = StudentRepositoryMock()
        usecase = UpdateStudentUsecase(repo=repo)
        controller = UpdateStudentController(usecase=usecase)
        request = HttpRequest(query_params={
            "ra": "21014443",
            "new_email": "joaj@gmail.com",
        })
        response = controller(request=request)

        expected = Student(
            ra="21014443",
            name="Guirão",
            email="joaj@gmail.com"
        )

        assert response.status_code == 200
        assert repo.students[2].ra == expected.ra
        assert repo.students[2].name == expected.name
        assert repo.students[2].email == expected.email

    def test_update_student_controller_ra_name_email(self):
        repo = StudentRepositoryMock()
        usecase = UpdateStudentUsecase(repo=repo)
        controller = UpdateStudentController(usecase=usecase)
        request = HttpRequest(query_params={
            "ra": "21014443",
            "new_name": "matuê",
            "new_email": "matue@pandora.com.br"
        })
        response = controller(request=request)

        expected = Student(
            ra="21014443",
            name="matuê",
            email="matue@pandora.com.br"
        )

        assert response.status_code == 200
        assert repo.students[2].ra == expected.ra
        assert repo.students[2].name == expected.name
        assert repo.students[2].email == expected.email

    def test_update_student_controller_no_items_found(self):
        repo = StudentRepositoryMock()
        usecase = UpdateStudentUsecase(repo=repo)
        controller = UpdateStudentController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "21014441",
        })

        response = controller(request=request)

        assert response.body == "No items found for ra"
        assert response.status_code == 404

    def test_update_student_controller_bad_request(self):
        repo = StudentRepositoryMock()
        usecase = UpdateStudentUsecase(repo=repo)
        controller = UpdateStudentController(usecase=usecase)

        request = HttpRequest(query_params={
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is missing"

    def test_update_student_controller_bad_request_int(self):
        repo = StudentRepositoryMock()
        usecase = UpdateStudentUsecase(repo=repo)
        controller = UpdateStudentController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": 21014440,
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "ra must be a string"

    def test_update_student_controller_bad_request_invalid_ra(self):
        repo = StudentRepositoryMock()
        usecase = UpdateStudentUsecase(repo=repo)
        controller = UpdateStudentController(usecase=usecase)

        request = HttpRequest(query_params={
            "ra": "2101444",
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is not valid"
        
