import pytest
from src.modules.get_selfies_to_review.app.get_selfies_to_review_usecase import GetSelfiesToReviewUsecase
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.get_selfies_to_review.app.get_selfies_to_review_viewmodel import GetSelfiesToReviewViewmodel


class Test_GetSelfiesToReviewViewModel:
    def test_get_selfies_to_review_viewmodel(self):
        repo = StudentRepositoryMock()
        usecase = GetSelfiesToReviewUsecase(repo=repo)

        reviews = usecase(reviewerRa=repo.reviewers[3].ra, nSelfies=5)
        viewmodel = GetSelfiesToReviewViewmodel(data=reviews).to_dict()

        assert viewmodel["reviews"][0]["selfie"] == {'idSelfie': 0, 'dateCreated': '2022-10-01T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'DECLINED', 'rejectionReasons': ['COVERED_FACE'], 'rejectionDescription': 'Usou chapéu de mexicano que cobriu a cara', 'automaticReview': {'automaticallyRejected': True, 'rejectionReasons': ['COVERED_FACE'], 'labels': [{'name': 'Portrait', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Face', 'Head', 'Person', 'Photography']}, {'name': 'Hat', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Human', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}]}}
        assert len(viewmodel["reviews"]) == 5
        assert viewmodel["message"] == "the reviews were retriven"