import pytest
from src.modules.update_selfie.app.update_selfie_viewmodel import UpdateSelfieViewModel
from src.shared.domain.entities.student import Student
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
"""
Selfie(
                idSelfie=0,
                student=self.students[0],
                dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/0KFBHTB.jpg",
                state=STATE.DECLINED,
                rejectionReason=REJECTION_REASON.COVERED_FACE,
                rejectionDescription="Balaclava"
            ),Student(
                ra="21010757",
                name="Victor",
                email="eusousoller@gmail.com"
            ),    
"""
class Test_UpdateSelfieViewModel:
    def test_update_selfie_view_model(self):
        repo = StudentRepositoryMock()

        result = {
            "idSelfie" : 0,
            "dateCreated" : "2022-10-01T16:01:59.149927",
            "url" : "https://i.imgur.com/0KFBHTB.jpg",
            "state" : "DECLINED",
            "rejectionReason": "COVERED_FACE",
            "rejectionDescription": "Balaclava",
            "student": {"ra":"21010757","name":"Victor","email":"eusousoller@gmail.com"},
            "message": "the selfie was updated"
        }

        selfie = repo.selfies[0]
        
        
        selfieViewModel = UpdateSelfieViewModel(selfie=selfie).to_dict()
        
        assert selfieViewModel == result
        
        