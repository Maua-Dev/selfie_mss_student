from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.get_review.app.get_review_viewmodel import GetReviewViewModel
import pytest

 
class Test_GetReviewViewModel:
    def test_get_review_viewmodel(self):
        repo = StudentRepositoryMock()
        review = repo.reviews[0]
        reviewViewModel = GetReviewViewModel(review).to_dict()

        result = {'dateAssigned': '2022-12-01T16:01:59.149927',
            'dateReviewed': '2022-12-02T16:05:59.149927',
            'idReview': 0,
            'reviewer': {'active': True,
                        'email': 'mauro@maua.br',
                        'name': 'Mauro Crapino',
                        'ra': '03026'},
            'selfie': {'automaticReview': {'automaticallyRejected': False,
                                            'labels': [{'confidence': 98.54370880126953,
                                                        'coords':{'Height': 0.8659809827804565,
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
                        'idSelfie': 1,
                        'message': 'the selfie was retriven',
                        'rejectionDescription': '',
                        'rejectionReasons': ['NONE'],
                        'state': 'APPROVED',
                        'url': 'https://i.imgur.com/b9qFYmb.jpg'},
            'state': 'APPROVED'} 

        
        assert reviewViewModel == result
        
