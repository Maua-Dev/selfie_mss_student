import pytest
from src.modules.get_selfies_by_ra.app.get_selfies_by_ra_viewmodel import GetSelfiesByRaViewModel
from src.shared.domain.entities.student import Student
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock

class Test_GetSelfiesByRaViewModel:
    def test_get_selfies_by_ra_view_model(self):
        repo = StudentRepositoryMock()
        selfies = [repo.selfies[0], repo.selfies[1]]
        
        selfiesViewModel = GetSelfiesByRaViewModel(selfies, repo.selfies[0].student).to_dict()

        expected = {
      
           'message': 'the selfies were retriven',
           'selfies': [{'automaticReview': {'automaticallyRejected': True,
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
                        'rejectionDescription': 'Balaclava',
                        'rejectionReasons': ['COVERED_FACE'],
                        'state': 'DECLINED',
                        'url': 'https://i.imgur.com/0KFBHTB.jpg'},
                       {'automaticReview': {'automaticallyRejected': False,
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
                        'idSelfie': 1,
                        'rejectionDescription': '',
                        'rejectionReasons': ['NONE'],
                        'state': 'APPROVED',
                        'url': 'https://i.imgur.com/b9qFYmb.jpg'}],
           'student': {'email': '21.01075-7@gmail.com',
                       'name': 'João Vitor Choueri Branco',
                       'ra': '21010757'},
           }
        
        assert selfiesViewModel == expected   
        
    def test_get_selfies_by_ra_view_model_empty_list(self):
        repo = StudentRepositoryMock()
        selfies = []
        
        selfiesViewModel = GetSelfiesByRaViewModel(selfies, 
                                                    Student(
                                                            ra="17090212",
                                                            name="Monkey Guy",
                                                            email="uuaa@floresta.com"
                                                        )
                                                    ).to_dict()

        expected = {
        'message': 'the selfies were retriven',
        'selfies': [],
        'student': {'email': 'uuaa@floresta.com',
                    'name': 'Monkey Guy',
                    'ra': '17090212'},
        }
        
        assert selfiesViewModel == expected   