import pytest
from src.shared.domain.entities.student import Student
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.get_selfie.get_selfie_viewmodel import GetSelfieViewModel

class Test_GetStudentViewModel:
    def test_get_selfie_view_model(self):
        repo = StudentRepositoryMock()
        selfie = repo.selfies[0]

        result = {
          'dateUpload': '2022-10-12T16:01:59.149927',
          'idSelfie': 0,
          'state': 'DECLINED',
          'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
          'rejectionReason': 'COVERED_FACE',
          'rejectionDescription': 'Balaclava',
          'message':"the selfie was retriven"
          }
        
        studentViewModel = GetSelfieViewModel(selfie).to_dict()
        
        assert studentViewModel == result
        
        