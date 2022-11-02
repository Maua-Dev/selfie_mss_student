import datetime
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.modules.create_selfie.app.create_selfie_viewmodel import CreateSelfieViewModel
from src.shared.domain.entities.student import Student
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.automatic_review import AutomaticReview
from src.shared.domain.entities.label import Label


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
            rejectionDescription = "",
            automaticReview=AutomaticReview(
                    automaticallyRejected=True,
                    rejectionReason=REJECTION_REASON.NOT_ALLOWED_BACKGROUND,
                    labels=[
                        Label(
                            name="Building",
                            coords={
                                        "Width": 0.9711952805519104,
                                        "Height": 0.8659809827804565,
                                        "Left": 0.012313545681536198,
                                        "Top": 0.11108686774969101
                                    },
                            confidence=98.13214,
                            parents=["Architecture"],
                            ),
                        Label(
                            name="Face",
                            coords={
                                        "Width": 0.9711952805519104,
                                        "Height": 0.8659809827804565,
                                        "Left": 0.012313545681536198,
                                        "Top": 0.11108686774969101
                                    },
                            confidence=98.54370880126953,
                            parents=[],
                        ),
                        Label(
                            name="Person",
                            coords={
                                        "Width": 0.9711952805519104,
                                        "Height": 0.8659809827804565,
                                        "Left": 0.012313545681536198,
                                        "Top": 0.11108686774969101
                                    },
                            confidence=98.54370880126953,
                            parents=[],
                        ),
                    ]
                )
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
