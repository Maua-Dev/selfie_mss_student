import pytest
from src.modules.update_selfie.app.update_selfie_viewmodel import UpdateSelfieViewModel
from src.shared.domain.entities.student import Student
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock


class Test_UpdateSelfieViewModel:
    def test_update_selfie_view_model(self):
        repo = StudentRepositoryMock()

        result = {
           'automaticReview': {'automaticallyRejected': True,
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
                                           'name': 'Hat',
                                           'parents': []},
                                          {'confidence': 98.54370880126953,
                                           'coords': {'Height': 0.8659809827804565,
                                                      'Left': 0.012313545681536198,
                                                      'Top': 0.11108686774969101,
                                                      'Width': 0.9711952805519104},
                                           'name': 'Face',
                                           'parents': []}],
                               'rejectionReasons': ['COVERED_FACE']},
            'dateCreated': '2022-10-01T16:01:59.149927',
            'idSelfie': 0,
            'message': 'the selfie was updated',
            'rejectionDescription': 'Balaclava',
            'rejectionReasons': ['COVERED_FACE'],
            'state': 'DECLINED',
            'student': {'email': 'eusousoller@gmail.com',
                        'name': 'Victor',
                        'ra': '21010757'},
            'url': 'https://i.imgur.com/0KFBHTB.jpg',
           }

        selfie = repo.selfies[0]
        
        
        selfieViewModel = UpdateSelfieViewModel(selfie=selfie).to_dict()
        
        assert selfieViewModel == result
        
        