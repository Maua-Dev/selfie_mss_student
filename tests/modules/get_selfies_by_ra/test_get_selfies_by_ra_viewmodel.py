import pytest
from src.modules.get_selfies_by_ra.get_selfies_by_ra_viewmodel import GetSelfiesByRaViewModel
from src.shared.domain.entities.student import Student
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock

class Test_GetSelfiesByRaViewModel:
    def test_get_selfies_by_ra_view_model(self):
        repo = StudentRepositoryMock()
        selfies = [repo.selfies[0], repo.selfies[1]]
        
        selfiesViewModel = GetSelfiesByRaViewModel(selfies, repo.selfies[0].student).to_dict()

        expected = {
        'message': 'the selfies were retriven',
        'selfies': [{'dateUpload': '2022-10-12T16:01:59.149927',
                    'idSelfie': 0,
                    'state': 'DECLINED',
                    'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'},
                    {'dateUpload': '2022-10-12T16:01:59.149927',
                    'idSelfie': 1,
                    'state': 'APPROVED',
                    'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}],
        'student': {'email': 'eusousoller@gmail.com',
                    'name': 'Victor',
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