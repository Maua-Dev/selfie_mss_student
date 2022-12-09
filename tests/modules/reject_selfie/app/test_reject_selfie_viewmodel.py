from src.modules.reject_selfie.app.reject_selfie_viewmodel import RejectSelfieViewModel
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock


class Test_RejectSelfieViewmodel:
    def test_reject_selfie_viewmodel(self):
        repo = StudentRepositoryMock()
        review = repo.reviews[3]
        reviewViewModel = RejectSelfieViewModel(review).to_dict()
        
        assert reviewViewModel == {'idReview': 0, 'state': 'PENDING_VALIDATION', 'reviewer': {'ra': '04618', 'name': 'Bruno Cambui Marques', 'email': 'bruno.marques@maua.br', 'active': True}, 'selfie': {'idSelfie': 0, 'dateCreated': '2022-10-01T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'DECLINED', 'rejectionReasons': ['COVERED_FACE'], 'rejectionDescription': 'Usou chapéu de mexicano que cobriu a cara', 'automaticReview': {'automaticallyRejected': True, 'rejectionReasons': ['COVERED_FACE'], 'labels': [{'name': 'Portrait', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Face', 'Head', 'Person', 'Photography']}, {'name': 'Hat', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Human', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}]}}, 'dateAssigned': '2022-11-28T16:01:59.149927', 'dateReviewed': '2022-12-02T16:05:59.149927', 'message': 'the review was rejected'}
        
        