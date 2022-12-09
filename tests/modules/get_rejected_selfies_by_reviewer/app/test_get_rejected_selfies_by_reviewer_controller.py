
from src.modules.get_rejected_selfies_by_reviewer.app.get_rejected_selfies_by_reviewer_controller import GetRejectedSelfiesByReviewerController
from src.modules.get_rejected_selfies_by_reviewer.app.get_rejected_selfies_by_reviewer_usecase import GetRejectedSelfiesByReviewerUsecase
from src.modules.get_rejected_selfies_by_reviewer.app.get_rejected_selfies_by_reviewer_viewmodel import GetRejectedSelfiesByReviewerViewModel
from src.shared.helpers.http.http_models import HttpRequest
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock


class Test_GetRejectedSelfiesByReviewerController:
    def test_get_rejected_selfies_by_reviewer_controller(self):
        repo = StudentRepositoryMock()
        usecase = GetRejectedSelfiesByReviewerUsecase(repo=repo)
        controller = GetRejectedSelfiesByReviewerController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": repo.reviewers[3].ra,
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body == GetRejectedSelfiesByReviewerViewModel(listRejectedReviews=[repo.reviews[7], repo.reviews[9]], reviewer=repo.reviews[6].reviewer).to_dict()

    def test_get_rejected_selfies_by_reviewer_controller_empty_list(self):
        repo = StudentRepositoryMock()
        usecase = GetRejectedSelfiesByReviewerUsecase(repo=repo)
        controller = GetRejectedSelfiesByReviewerController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": repo.reviewers[1].ra,
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body == GetRejectedSelfiesByReviewerViewModel(listRejectedReviews=[], reviewer=repo.reviewers[1]).to_dict()

    def test_get_rejected_selfies_by_reviewer_controller_no_items_found(self):
        repo = StudentRepositoryMock()
        usecase = GetRejectedSelfiesByReviewerUsecase(repo=repo)
        controller = GetRejectedSelfiesByReviewerController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": "12345",
        })

        response = controller(request=request)

        assert response.status_code == 404
        assert response.body == "No items found for reviewerRa"

    def test_get_rejected_selfies_by_reviewer_controller_missing_reviewerRa(self):
        repo = StudentRepositoryMock()
        usecase = GetRejectedSelfiesByReviewerUsecase(repo=repo)
        controller = GetRejectedSelfiesByReviewerController(usecase=usecase)

        request = HttpRequest(query_params={
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field reviewerRa is missing"

    def test_get_rejected_selfies_by_reviewer_controller_reviewerRa_not_valid(self):
        repo = StudentRepositoryMock()
        usecase = GetRejectedSelfiesByReviewerUsecase(repo=repo)
        controller = GetRejectedSelfiesByReviewerController(usecase=usecase)

        request = HttpRequest(query_params={
            "reviewerRa": "1234",
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field reviewerRa is not valid"