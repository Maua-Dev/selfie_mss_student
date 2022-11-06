from src.modules.create_selfie.app.create_selfie_usecase import CreateSelfieUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.create_selfie.app.create_selfie_controller import CreateSelfieController
from src.shared.helpers.http.http_models import HttpRequest
from src.shared.domain.enums.state_enum import STATE

AUTOMATIC_REVIEW_DICT = {
            "automaticallyRejected": "False",
            "rejectionReasons": ["NONE"],
            "labels": [{
                            "name": "Glasses",
                            "coords": {
                                    "Width": "0.6591288447380066",
                                    "Height": "0.17444363236427307",
                                    "Left": "0.19148917496204376",
                                    "Top": "0.3813813030719757"
                            },
                            "confidence": "94.5357666015625",
                            "parents": ["Accessories"],
                        },
                        {
                            "name": "Blalblas",
                            "coords": {
                                    "Width": "0.6591288480066",
                                    "Height": "0.1744236427307",
                                    "Left": "0.19148916204376",
                                    "Top": "0.3813813719757"
                            },
                            "confidence": "95.5366015625",
                            "parents": ["ASODnoasdsa", "nmdokasnkndkasnkd"],
                        }]
                  }

class Test_CreateSelfieController:

    def test_create_selfie_controller(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)
        controller = CreateSelfieController(usecase=usecase)
        request = {
            "ra": "21014442",
            "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q",
            "automaticReview": AUTOMATIC_REVIEW_DICT
        }
        
        lenBefore = len(repo.selfies)
        response = controller(request=request)
        lenAfter = lenBefore + 1


        assert response.status_code == 201
        assert response.body["message"] == "the selfie was created"
        assert len(repo.selfies) == lenAfter
        assert response.body["url"] == "https://www.youtube.com/watch?v=5IpYOF4Hi6Q"
        assert response.body["idSelfie"] == 1
        assert response.body["student"]["ra"] == "21014442"
        assert response.body["rejectionReasons"] == ["NONE"]
        assert response.body["rejectionDescription"] == None
        assert response.body["automaticReview"]["rejectionReasons"] == ["NONE"]
    
    def test_create_selfie_controller_automaticallyRejected(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)
        controller = CreateSelfieController(usecase=usecase)

        automaticReviewDict = {
                    "automaticallyRejected": "True",
                    "rejectionReasons": ["COVERED_FACE", "NO_PERSON_RECOGNIZED"],
                    "labels": [{
                                    "name": "Glasses",
                                    "coords": {
                                            "Width": "0.6591288447380066",
                                            "Height": "0.17444363236427307",
                                            "Left": "0.19148917496204376",
                                            "Top": "0.3813813030719757"
                                    },
                                    "confidence": "94.5357666015625",
                                    "parents": ["Accessories"],
                                },
                                {
                                    "name": "Blalblas",
                                    "coords": {
                                            "Width": "0.6591288480066",
                                            "Height": "0.1744236427307",
                                            "Left": "0.19148916204376",
                                            "Top": "0.3813813719757"
                                    },
                                    "confidence": "95.5366015625",
                                    "parents": ["ASODnoasdsa", "nmdokasnkndkasnkd"],
                                }]
                        }

        request = {
            "ra": "21014442",
            "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q",
            "automaticReview": automaticReviewDict
        }
        
        lenBefore = len(repo.selfies)
        response = controller(request=request)

        lenAfter = lenBefore + 1

        assert len(repo.selfies) == lenAfter
        assert response.body["url"] == "https://www.youtube.com/watch?v=5IpYOF4Hi6Q"
        assert response.body["idSelfie"] == 1
        assert response.body["student"]["ra"] == "21014442"
        assert response.status_code == 201
        assert response.body["message"] == "the selfie was created"
        assert response.body["state"] == "DECLINED"
        assert response.body["rejectionReasons"] == ["COVERED_FACE", "NO_PERSON_RECOGNIZED"]
        assert response.body["rejectionDescription"] == "auto-rejected by AI"
        assert response.body["automaticReview"]["rejectionReasons"] == ["COVERED_FACE", "NO_PERSON_RECOGNIZED"]

    def test_create_selfie_controller_missing_ra(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)
        controller = CreateSelfieController(usecase=usecase)
        request = {
            "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q",
        }
        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is missing"

    def test_create_selfie_controller_missing_url(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)
        controller = CreateSelfieController(usecase=usecase)
        request = {
            "ra": "21002008",
        }
        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field url is missing"

   
    def test_create_selfie_controller_bad_request_int(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)
        controller = CreateSelfieController(usecase=usecase)

        request = {
            "ra": 21002088,
            "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q",
            "automaticReview": AUTOMATIC_REVIEW_DICT
        }

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "ra must be a string"

    def test_create_selfie_controller_bad_request_invalid_ra_dash(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)
        controller = CreateSelfieController(usecase=usecase)

        request = {
            "ra": "2100208-8",
            "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q",
            "automaticReview": AUTOMATIC_REVIEW_DICT
        }
        
        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field ra is not valid"

    def test_create_selfie_controller_no_ra_found(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)
        controller = CreateSelfieController(usecase=usecase)

        request = {
            "ra": "12345678",
            "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q",
            "automaticReview": AUTOMATIC_REVIEW_DICT
        }
        
        response = controller(request=request)

        assert response.status_code == 404
        assert response.body == "No items found for ra"

    def test_create_selfie_controller_invalid_url(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)
        controller = CreateSelfieController(usecase=usecase)

        request = {
            "ra": "21014442",
            "url": "http://www.macaco.br",
            "automaticReview": AUTOMATIC_REVIEW_DICT
        }

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == 'Field url is not valid'
        
    def test_create_selfie_controller_student_have_approved_selfie(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)
        controller = CreateSelfieController(usecase=usecase)

        request = {
            "ra": "15013103",
            "url": "http://www.macaco.br",
            "automaticReview": AUTOMATIC_REVIEW_DICT
        }

        response = controller(request=request)

        assert response.status_code == 403
        assert response.body == 'That action is forbidden for this Student'
        
    def test_create_selfie_controller_automatic_review_must_be_dict(self):
        repo = StudentRepositoryMock()
        usecase = CreateSelfieUsecase(repo=repo)
        controller = CreateSelfieController(usecase=usecase)

        request = {
            "ra": "15013103",
            "url": "http://www.macaco.br",
            "automaticReview": 1
        }

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == 'Field automaticReview is not valid'