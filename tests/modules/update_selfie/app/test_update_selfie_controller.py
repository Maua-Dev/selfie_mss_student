import datetime
from src.shared.domain.entities.selfie import Selfie
from src.modules.update_selfie.app.update_selfie_usecase import UpdateSelfieUsecase
from src.shared.domain.enums.state_enum import STATE
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.update_selfie.app.update_selfie_controller import UpdateSelfieController
from src.shared.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON

class Test_UpdateSelfieController:

    def test_update_selfie_controller(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)
        controller = UpdateSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra":"21010757", 
            "idSelfie":'0',
            "new_state":"DECLINED",
            "new_rejectionReason":"NO_PERSON_RECOGNIZED",
            "new_rejectionDescription":"Please appear more"
        })
        response = controller(request=request)

        expected = Selfie(student=repo.students[0], idSelfie=0, state=STATE.DECLINED, rejectionReason=REJECTION_REASON.NO_PERSON_RECOGNIZED, rejectionDescription="Please appear more", dateUpload=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),url="https://i.imgur.com/0KFBHTB.jpg")


        assert response.status_code == 200
        assert response.body["student"]['ra'] == expected.student.ra
        assert response.body['state'] == expected.state.value
        assert response.body['message'] == "the selfie was updated"
        
    def test_update_selfie_controller_state(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)
        controller = UpdateSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra":"21010757", 
            "idSelfie":'0',
            "new_state":"APPROVED",
        })
        response = controller(request=request)


        assert response.status_code == 200
        assert response.body['student']['ra'] == "21010757"
        assert response.body['state'] == "APPROVED"
        assert response.body['message'] == "the selfie was updated"

    def test_update_selfie_controller_no_items_found(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)
        controller = UpdateSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "ra": "21014441",
            "idSelfie": "0"
        })

        response = controller(request=request)

        assert response.body == "No items found for ra or idSelfie"
        assert response.status_code == 404

    def test_update_selfie_controller_bad_request(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)
        controller = UpdateSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "ra":"21010757"
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field idSelfie is missing"

    def test_update_selfie_controller_bad_request_int(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)
        controller = UpdateSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "ra": 21014440,
            "idSelfie": '0'
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "ra must be a string"

    def test_update_selfie_controller_bad_request_invalid_ra(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)
        controller = UpdateSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "ra": "2101444",
            "idSelfie": '0'
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is not valid"

    def test_update_selfie_controller_id_selfie_int(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)
        controller = UpdateSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "ra": "21015444",
            "idSelfie": 0
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field idSelfie isn\'t in the right type.\n Received: int.\n Expected: str"

    def test_update_selfie_controller_invalid_state(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)
        controller = UpdateSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "ra": "21010757",
            "idSelfie": '0',
            "new_state":"Vilas"

        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field new_state is not valid"

    def test_update_selfie_controller_invalid_rejection_reason(self):
        repo = StudentRepositoryMock()
        usecase = UpdateSelfieUsecase(repo=repo)
        controller = UpdateSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "ra": "21010757",
            "idSelfie": '0',
            "new_rejectionReason":"Vilas"

        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field new_rejectionReason is not valid"