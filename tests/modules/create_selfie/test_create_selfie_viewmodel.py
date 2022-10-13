import datetime
import pytest
from src.domain.enums.state_enum import STATE
from src.modules.create_selfie.create_selfie_viewmodel import CreateSelfieViewModel
from src.domain.entities.student import Student
from src.domain.entities.selfie import Selfie
from src.infra.repositories.student_repository_mock import StudentRepositoryMock


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
            dateUpload=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927)
        )

        expected = {
            "student": {
                "ra":"21007586",
                "email":"gui@cleme.com",
                "name":"Guilherme Clementino"
                },
            "idSelfie": 0,
            "url": "https://www.youtube.com/watch?v=X5oh7Gc3kG4",
            "dateUpload": "2022-10-12T16:01:59.149927",
            "state": "APPROVED",
            "message": "the selfie was created"
        }
        
        selfieViewModel = CreateSelfieViewModel(selfie).to_dict()

        assert selfieViewModel == expected
