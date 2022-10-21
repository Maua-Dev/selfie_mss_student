import datetime
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.modules.create_selfie.app.create_selfie_viewmodel import CreateSelfieViewModel
from src.shared.domain.entities.student import Student
from src.shared.domain.entities.selfie import Selfie


class Test_CreateSelfieViewModel:
    def test_create_selfie_view_model(self):
        student = Student(
            ra="21007586",
            name="Guilherme Clementino",
            email="gui@cleme.com"
        )

        selfie = Selfie(
            student=student,
            url="https://www.youtube.com/watch?v=X5oh7Gc3kG4",
            idSelfie=0,
            state=STATE.APPROVED,
            dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
            rejectionReason = REJECTION_REASON.NONE,
            rejectionDescription = ""
        )

        expected = {
            "student": {
                "ra":"21007586",
                "email":"gui@cleme.com",
                "name":"Guilherme Clementino"
                },
            "idSelfie": 0,
            "url": "https://www.youtube.com/watch?v=X5oh7Gc3kG4",
            "dateCreated": "2022-10-12T16:01:59.149927",
            "state": "APPROVED",
            "rejectionReason": "NONE",
            "rejectionDescription": "",
            "message": "the selfie was created"
        }
        
        selfieViewModel = CreateSelfieViewModel(selfie).to_dict()

        assert selfieViewModel == expected
