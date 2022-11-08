from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.delete_selfie.app.delete_selfie_viewmodel import DeleteSelfieViewModel

class Test_DeleteSelfieViewModel:
    def test_get_selfie_view_model(self):
        repo = StudentRepositoryMock()
        selfie = repo.selfies[0]
        student = repo.students[0]
        result = {
            'student':{
            "ra":"21010757",
            "name":"Victor",
            "email":"eusousoller@gmail.com"
        },
            'selfie':{
            'dateCreated': '2022-10-01T16:01:59.149927',
            'idSelfie': 0,
            'state': 'DECLINED',
            'url': 'https://i.imgur.com/0KFBHTB.jpg',
            'rejectionReason': 'COVERED_FACE',
            'rejectionDescription': 'Balaclava'
            },
            'message':"the selfie was deleted"
          }
     
        
        studentViewModel = DeleteSelfieViewModel(data=selfie, student=student).to_dict()
        
        assert studentViewModel == result
        
        