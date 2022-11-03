from src.modules.delete_selfie.app.delete_selfie_controller import DeleteSelfieController
from src.modules.delete_selfie.app.delete_selfie_usecase import DeleteSelfieUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.helpers.http.http_models import HttpRequest


class Test_DeleteSelfieController:

    def test_delete_selfie_controller(self):
        repo = StudentRepositoryMock()
        lenghtBefore = len(repo.selfies)
        usecase = DeleteSelfieUsecase(repo=repo)
        controller = DeleteSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra": "21014442",
            "idSelfie": "0"
        })
        response = controller(request=request)

        expected = {
           'message': 'the selfie was deleted',
           'selfie': {'automaticReview': {'automaticallyRejected': False,
                                          'labels': [{'confidence': 98.54370880126953,
                                                      'coords': {'Height': 0.8659809827804565,
                                                                 'Left': 0.012313545681536198,
                                                                 'Top': 0.11108686774969101,
                                                                 'Width': 0.9711952805519104},
                                                      'name': 'Person',
                                                      'parents': []},
                                                     {'confidence': 98.54370880126953,
                                                      'coords': {'Height': 0.8659809827804565,
                                                                 'Left': 0.012313545681536198,
                                                                 'Top': 0.11108686774969101,
                                                                 'Width': 0.9711952805519104},
                                                      'name': 'Face',
                                                      'parents': []}],
                                          'rejectionReasons': ['NONE']},
                      'dateCreated': '2022-10-12T16:01:59.149927',
                      'idSelfie': 0,
                      'rejectionDescription': '',
                      'rejectionReasons': ['NONE'],
                      'state': 'PENDING_REVIEW',
                      'url': 'https://i.imgur.com/dv7Q5VT.jpg'},
           'student': {'email': 'eutambemsousoler@outlook.com',
                       'name': 'Soller',
                       'ra': '21014442'},
          }
        
        assert response.status_code == 200
        assert len(repo.selfies) == lenghtBefore - 1
        assert response.body == expected

    def test_delete_selfie_controller_selfie_not_found(self):
        repo = StudentRepositoryMock()
        lenghtBefore = len(repo.selfies)
        usecase = DeleteSelfieUsecase(repo=repo)
        controller = DeleteSelfieController(usecase=usecase)
        request = HttpRequest(body={
            "ra": "21014442",
            "idSelfie": "10"
        })
        response = controller(request=request)

        
        assert response.body == "No items found for ra or idSelfie"
        assert response.status_code == 404


    def test_delete_selfie_controller_no_ra_found(self):
        repo = StudentRepositoryMock()
        usecase = DeleteSelfieUsecase(repo=repo)
        controller = DeleteSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "ra": "21007586",
            "idSelfie": "10"
        })

        response = controller(request=request)

        assert response.body == "No items found for ra or idSelfie"
        assert response.status_code == 404

    def test_delete_selfie_controller_bad_request_missing_ra(self):
        repo = StudentRepositoryMock()
        usecase = DeleteSelfieUsecase(repo=repo)
        controller = DeleteSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "idSelfie": "10"
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is missing"


    def test_delete_selfie_controller_bad_request_missing_idSelfie(self):
        repo = StudentRepositoryMock()
        usecase = DeleteSelfieUsecase(repo=repo)
        controller = DeleteSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "ra": "21007586",
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field idSelfie is missing"

    def test_delete_selfie_controller_bad_request_ra_int(self):
        repo = StudentRepositoryMock()
        usecase = DeleteSelfieUsecase(repo=repo)
        controller = DeleteSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "ra": 21014440,
            "idSelfie": "1"
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "ra must be a string"

    def test_delete_selfie_controller_bad_request_invalid_ra(self):
        repo = StudentRepositoryMock()
        usecase = DeleteSelfieUsecase(repo=repo)
        controller = DeleteSelfieController(usecase=usecase)

        request = HttpRequest(body={
            "ra": "2101444",
            "idSelfie": "10"
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is not valid"

    def test_delete_selfie_controller_bad_request_Idselfie_int(self):
          repo = StudentRepositoryMock()
          usecase = DeleteSelfieUsecase(repo=repo)
          controller = DeleteSelfieController(usecase=usecase)

          request = HttpRequest(body={
              "ra": "21010757",
              "idSelfie": 1
          })

          response = controller(request=request)

          assert response.status_code == 400
          assert response.body == "Field idSelfie isn\'t in the right type.\n Received: int.\n Expected: str"

    def test_delete_selfie_controller_bad_request_Idselfie_word(self):
        repo = StudentRepositoryMock()
        usecase = DeleteSelfieUsecase(repo=repo)
        controller = DeleteSelfieController(usecase=usecase)

        request = HttpRequest(body= {
            "ra": "21010757",
            "idSelfie": "MACACOUAUAUAUAUAUAAUAUAU"
        })

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field idSelfie is not valid"


      
    def test_delete_selfie_controller_forbidden_item(self):
        repo = StudentRepositoryMock()
        usecase = DeleteSelfieUsecase(repo=repo)
        controller = DeleteSelfieController(usecase=usecase)

        request = HttpRequest(body= {
            "ra": "21010757",
            "idSelfie": "1"
        })

        response = controller(request=request)
        assert response.status_code == 403
        assert response.body == "That action is forbidden for this Selfie"


      