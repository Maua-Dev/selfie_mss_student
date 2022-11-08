from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.get_selfie.app.get_selfie_viewmodel import GetSelfieViewModel

from src.shared.domain.entities.student import Student


class Test_GetStudentViewModel:
    def test_get_selfie_view_model(self):
        repo = StudentRepositoryMock()
        selfie = repo.selfies[0]

        result = {
          'dateCreated': '2022-10-01T16:01:59.149927',
          'idSelfie': 0,
          'state': 'DECLINED',
          'url': 'https://i.imgur.com/0KFBHTB.jpg',
          'rejectionReason': 'COVERED_FACE',
          'rejectionDescription': 'Balaclava',
          'message':"the selfie was retriven"
          }
        
        studentViewModel = GetSelfieViewModel(selfie).to_dict()
        
        assert studentViewModel == result
        
