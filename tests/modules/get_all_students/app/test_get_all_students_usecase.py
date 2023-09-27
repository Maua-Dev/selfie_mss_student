import datetime
from src.modules.get_all_students.app.get_all_students_usecase import GetAllStudentsUsecase
from src.shared.domain.entities.automatic_review import AutomaticReview
from src.shared.domain.entities.label import Label
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.student import Student
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.shared.domain.enums.student_state_enum import STUDENT_STATE
import pytest

class Test_GetAllStudentsUsecase:
    def test_get_all_students(self):
        repo = StudentRepositoryMock()
        usecase = GetAllStudentsUsecase(repo=repo)
       
        all_students = usecase()
       
        assert len(all_students) == len(repo.students) 
        assert all_students[0]["name"] == "João Vitor Choueri Branco"
        assert all_students[0]["status"] == STUDENT_STATE.APPROVED
        assert len(all_students[0]["selfies"]) == 2
        assert all_students[1]["status"] == STUDENT_STATE.SELFIE_PENDING_REVIEW
        assert all_students[3]["status"] == STUDENT_STATE.SELFIE_IN_REVIEW
        assert all_students[4]["status"] == STUDENT_STATE.NO_SELFIE
        assert all_students[6]["status"] == STUDENT_STATE.SELFIE_REJECTED
    
    def test_get_all_students_with_unknow_ra(self):
        repo = StudentRepositoryMock()

        repo.selfies.append(
            Selfie(
                idSelfie=0,
                student=Student(
                    email="21.01444-2@maua.br",
                    name="LUIGI GUIMARES TREVISAN",
                    ra="22011021"
                ),
                dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/4ewA19S.png",
                state=STATE.DECLINED,
                rejectionReasons=[REJECTION_REASON.NOT_ALLOWED_BACKGROUND],
                rejectionDescription="O brilho dos olhos dela é senscaional",
                automaticReview=AutomaticReview(
                    automaticallyRejected=False,
                    rejectionReasons=[REJECTION_REASON.NONE],
                    labels=[
                        Label(
                            name="Photography",
                            coords={},
                            confidence=100.00,
                            parents=[],
                        ),
                        Label(
                            name="Portrait",
                            coords={
                                "Width": 0.9711952805519104,
                                "Height": 0.8659809827804565,
                                "Left": 0.012313545681536198,
                                "Top": 0.11108686774969101
                            },
                            confidence=100.00,
                            parents=["Face", "Head", "Person", "Photography"],
                        ),
                        Label(
                            name="Head",
                            coords={},
                            confidence=100.00,
                            parents=["Person"],
                        ),
                        Label(
                            name="Face",
                            coords={
                                "Width": 0.9711952805519104,
                                "Height": 0.8659809827804565,
                                "Left": 0.012313545681536198,
                                "Top": 0.11108686774969101
                            },
                            confidence=100.00,
                            parents=["Person", "Head"],
                        ),
                        Label(
                            name="Person",
                            coords={
                                "Width": 0.9972279071807861,
                                "Height": 0.88490229845047,
                                "Left": 0.0026419830974191427,
                                "Top": 0.11343356966972351
                            },
                            confidence=99.62065124511719,
                            parents=[],
                        )
                    ]
                )
            ))

        usecase = GetAllStudentsUsecase(repo=repo)
       
        all_students = usecase()

        assert all_students[-1]["ra"] == 'unknown-ra'