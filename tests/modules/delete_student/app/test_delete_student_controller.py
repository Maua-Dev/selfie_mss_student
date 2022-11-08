from src.modules.delete_student.app.delete_student_usecase import DeleteStudentUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.delete_student.app.delete_student_controller import DeleteStudentController
from src.shared.helpers.http.http_models import HttpRequest


class Test_DeleteStudentController:

    def test_delete_student_controller(self):
        repo = StudentRepositoryMock()
        lenghtBefore = len(repo.students)
        usecase = DeleteStudentUsecase(repo=repo)
        controller = DeleteStudentController(usecase=usecase)
        request = HttpRequest(body={
            "ra": "21014443",
        })
        response = controller(request=request)
        expected = {
            "ra":"21014443",
            "name":"Guirão",
            "email":"acreditaquesousollertambem@yahoo.com",
            "message":"User was deleted successfully"
        } 
        
        assert response.status_code == 200
        assert len(repo.students) == lenghtBefore - 1
        assert response.body == expected



    def test_delete_student_controller_no_items_found(self):
        repo = StudentRepositoryMock()
        usecase = DeleteStudentUsecase(repo=repo)
        controller = DeleteStudentController(usecase=usecase)

        request = HttpRequest(body={
            "ra": "21014432",
        })

        response = controller(request=request)

        assert response.body == "No items found for ra"
        assert response.status_code == 404

    def test_delete_student_controller_bad_request_missing_ra(self):
        repo = StudentRepositoryMock()
        usecase = DeleteStudentUsecase(repo=repo)
        controller = DeleteStudentController(usecase=usecase)

        request = HttpRequest(body={
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is missing"

    def test_delete_student_controller_bad_request_int(self):
        repo = StudentRepositoryMock()
        usecase = DeleteStudentUsecase(repo=repo)
        controller = DeleteStudentController(usecase=usecase)

        request = HttpRequest(body={
            "ra": 21014440,
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "ra must be a string"

    def test_delete_student_controller_bad_request_invalid_ra(self):
        repo = StudentRepositoryMock()
        usecase = DeleteStudentUsecase(repo=repo)
        controller = DeleteStudentController(usecase=usecase)

        request = HttpRequest(body={
            "ra": "2101444",
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is not valid"
