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
            rejectionReasons = [REJECTION_REASON.NONE],
            rejectionDescription = "",
            automaticReview=AutomaticReview(
                    automaticallyRejected=True,
                    rejectionReasons=[REJECTION_REASON.NOT_ALLOWED_BACKGROUND, REJECTION_REASON.NO_PERSON_RECOGNIZED],
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

        expected = {'dateCreated': '2022-10-12T16:01:59.149927',
          'idSelfie': 0,
          'message': 'the selfie was created',
          'rejectionDescription': '',
          'rejectionReasons': ["NONE"],
          'state': 'APPROVED',
          'student': {'email': 'gui@cleme.com',
                      'name': 'Guilherme Clementino',
                      'ra': '21007586'},
          'url': 'https://www.youtube.com/watch?v=X5oh7Gc3kG4',
          'automaticReview': {'automaticallyRejected': True,
                              'labels': [{'confidence': 98.13214,
                                          'coords': {'Height': 0.8659809827804565,
                                                     'Left': 0.012313545681536198,
                                                     'Top': 0.11108686774969101,
                                                     'Width': 0.9711952805519104},
                                          'name': 'Building',
                                          'parents': ['Architecture']},
                                         {'confidence': 98.54370880126953,
                                          'coords': {'Height': 0.8659809827804565,
                                                     'Left': 0.012313545681536198,
                                                     'Top': 0.11108686774969101,
                                                     'Width': 0.9711952805519104},
                                          'name': 'Face',
                                          'parents': []},
                                         {'confidence': 98.54370880126953,
                                          'coords': {'Height': 0.8659809827804565,
                                                     'Left': 0.012313545681536198,
                                                     'Top': 0.11108686774969101,
                                                     'Width': 0.9711952805519104},
                                          'name': 'Person',
                                          'parents': []}],
                              'rejectionReasons': ["NOT_ALLOWED_BACKGROUND", "NO_PERSON_RECOGNIZED"]}}
        
        selfieViewModel = CreateSelfieViewModel(selfie).to_dict()

        assert selfieViewModel == expected
