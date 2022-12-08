from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.get_review.app.get_review_viewmodel import GetReviewViewModel
import pytest

 
class Test_GetReviewViewModel:
    def test_get_review_viewmodel(self):
        repo = StudentRepositoryMock()
        review = repo.reviews[0]
        reviewViewModel = GetReviewViewModel(review).to_dict()

        result = {'idReview': 0, 'state': 'APPROVED', 'reviewer': {'ra': '03026', 'name': 'Mauro Crapino', 'email': 'mauro@maua.br', 'active': 'True'}, 'selfie': {'idSelfie': 1, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/b9qFYmb.jpg', 'state': 'APPROVED', 'rejectionReasons': ['NONE'], 'rejectionDescription': '', 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Person', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}]}}, 'dateAssigned': '2022-12-01T16:01:59.149927', 'dateReviewed': '2022-12-02T16:05:59.149927', 'message': 'the review was retriven'}
        
        assert reviewViewModel == result
        
