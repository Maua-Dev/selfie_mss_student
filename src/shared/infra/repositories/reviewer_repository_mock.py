

import datetime
from src.shared.domain.entities.automatic_review import AutomaticReview
from src.shared.domain.entities.label import Label
from src.shared.domain.entities.review import Review
from src.shared.domain.entities.reviwer import Reviewer
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.student import Student
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.review_state_enum import REVIEW_STATE
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.repositories.reviewer_repository_interface import IReviewerRepository


class ReviwerRepositoryMock(IReviewerRepository):
    reviewers: list[Reviewer]
    reviews: list[Review]
    selfies: list[Selfie]
    students: list[Student]

    def __init__(self):
      
        self.students = [
            Student(
                ra="21010757",
                name="Victor",
                email="eusousoller@gmail.com"
            ),
            Student(
                ra="21014442",
                name="Soller",
                email="eutambemsousoler@outlook.com"
            ),
            Student(
                ra="21014443",
                name="Guirão",
                email="acreditaquesousollertambem@yahoo.com"
            ),
            Student(
                ra="21014440",
                name="Eh o Vilas do Mockas",
                email="eusouoawsboy@amazon.com"
            ),
            Student(
                ra="17090212",
                name="Monkey Guy",
                email="uuaa@floresta.com"
            ),
            Student(
                ra="15013103",
                name="Little Ronald",
                email="iamronald@mageofprogramming.com.br"
            ),
            Student(
                ra="21002088",
                name="Maluzinha",
                email="mvergani.enactusmaua@gmail.com"
            )
        ]

        self.selfies = [
            Selfie(
                idSelfie=0,
                student=self.students[0],
                dateCreated=datetime.datetime(2022, 10, 1, 16, 1, 59, 149927),
                url="https://i.imgur.com/0KFBHTB.jpg",
                state=STATE.DECLINED,
                rejectionReasons=[REJECTION_REASON.COVERED_FACE],
                rejectionDescription="Balaclava",
                automaticReview=AutomaticReview(
                    automaticallyRejected=True,
                    rejectionReasons=[REJECTION_REASON.COVERED_FACE],
                    labels=[
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
                        Label(
                            name="Hat",
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
                    ]
                )
            ),
            Selfie(
                idSelfie=1,
                student=self.students[0],
                dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/b9qFYmb.jpg",
                state=STATE.APPROVED,
                rejectionReasons=[REJECTION_REASON.NONE],
                rejectionDescription="",
                automaticReview=AutomaticReview(
                    automaticallyRejected=False,
                    rejectionReasons=[REJECTION_REASON.NONE],
                    labels=[
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
                    ]
                )
            ),
            Selfie(
                idSelfie=0,
                student=self.students[1],
                dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/dv7Q5VT.jpg",
                state=STATE.PENDING_REVIEW,
                rejectionReasons=[REJECTION_REASON.NONE],
                rejectionDescription="",
                automaticReview=AutomaticReview(
                    automaticallyRejected=False,
                    rejectionReasons=[REJECTION_REASON.NONE],
                    labels=[
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
                    ]
                )
            ),
            Selfie(
                idSelfie=0,
                student=self.students[2],
                dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/6a7qqRg.jpg",
                state=STATE.APPROVED,
                rejectionReasons=[REJECTION_REASON.NONE],
                rejectionDescription="",
                automaticReview=AutomaticReview(
                    automaticallyRejected=False,
                    rejectionReasons=[REJECTION_REASON.NONE],
                    labels=[
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
                        Label(
                            name="Face",
                            coords={},
                            confidence=98.54370880126953,
                            parents=[],
                        ),
                    ]
                )
            ),
            Selfie(
                idSelfie=0,
                student=self.students[3],
                dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/4ewA19S.png",
                state=STATE.IN_REVIEW,
                rejectionReasons=[REJECTION_REASON.NONE],
                rejectionDescription="",
                automaticReview=AutomaticReview(
                    automaticallyRejected=False,
                    rejectionReasons=[REJECTION_REASON.NONE],
                    labels=[
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
                        Label(
                            name="Face",
                            coords={
                                "Width": 0.9711952805519104,
                                "Height": 0.8659809827804565,
                                "Left": 0.012313545681536198,
                                "Top": 0.11108686774969101
                            },
                            confidence=99.12312312,
                            parents=[],
                        ),
                    ]
                )
            ),
            Selfie(
                idSelfie=0,
                student=self.students[5],
                dateCreated=datetime.datetime(2022, 10, 1, 16, 1, 59, 149927),
                url="https://i.imgur.com/4ewA19S.png",
                state=STATE.DECLINED,
                rejectionReasons=[REJECTION_REASON.COVERED_FACE],
                rejectionDescription="Usou chapéu de mexicano que cobriu a cara",
                automaticReview=AutomaticReview(
                    automaticallyRejected=True,
                    rejectionReasons=[REJECTION_REASON.COVERED_FACE],
                    labels=[
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
                            name="Hat",
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
                            name="Human",
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
            ),
            Selfie(
                idSelfie=1,
                student=self.students[5],
                dateCreated=datetime.datetime(2022, 10, 2, 16, 1, 59, 149927),
                url="https://i.imgur.com/4ewA19S.png",
                state=STATE.DECLINED,
                rejectionReasons=[REJECTION_REASON.NOT_ALLOWED_BACKGROUND],
                rejectionDescription="Tirou foto no meio da Rave, enquanto aparecia um brilho forte",
                automaticReview=AutomaticReview(
                    automaticallyRejected=True,
                    rejectionReasons=[REJECTION_REASON.NOT_ALLOWED_BACKGROUND],
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
            ),
            Selfie(
                idSelfie=2,
                student=self.students[5],
                dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/4ewA19S.png",
                state=STATE.DECLINED,
                rejectionReasons=[REJECTION_REASON.NONE],
                rejectionDescription="",
                automaticReview=AutomaticReview(
                    automaticallyRejected=False,
                    rejectionReasons=[REJECTION_REASON.NONE],
                    labels=[
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

            ),
            Selfie(
                idSelfie=3,
                student=self.students[5],
                dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/4ewA19S.png",
                state=STATE.APPROVED,
                rejectionReasons=[REJECTION_REASON.NONE],
                rejectionDescription="",
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
                ),

            ),
            Selfie(
                idSelfie=0,
                student=self.students[6],
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
            )
        ]


        self.reviewers = [
            Reviewer(ra="03026", name="Mauro Crapino",
                          email="mauro@maua.br", active=True),
            Reviewer(ra="04359", name="JOSE FERNANDO XAVIER GONCALES",
                          email="fernando.goncales@maua.br", active=True),
            Reviewer(ra="04712", name="Luiz Miguel Rocha Seixeiro",
                          email="luiz.seixeiro@maua.br", active=True),
            Reviewer(ra="04618", name="Bruno Cambui Marques",
                          email="bruno.marques@maua.br", active=True)
        ]

        self.reviews = [
          Review(
                reviewId = 0,
                state=REVIEW_STATE.APPROVED,
                reviewer=self.reviewers[0],
                selfie=self.selfies[1],
                dateAssigned=datetime.datetime(2022, 12, 1, 16, 1, 59, 149927),
                dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
              ),
          Review(
                reviewId = 0,
                state=REVIEW_STATE.APPROVED,
                reviewer=self.reviewers[1],
                selfie=self.selfies[2],
                dateAssigned=datetime.datetime(2022, 11, 31, 16, 1, 59, 149927),
                dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
              ),
          Review(
                reviewId = 0,
                state=REVIEW_STATE.APPROVED,
                reviewer=self.reviewers[2],
                selfie=self.selfies[4],
                dateAssigned=datetime.datetime(2022, 11, 9, 16, 1, 59, 149927),
                dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
              ),
          Review(
                reviewId = 0,
                state=REVIEW_STATE.PENDING_VALIDATION,
                reviewer=self.reviewers[3],
                selfie=self.selfies[5],
                dateAssigned=datetime.datetime(2022, 11, 28, 16, 1, 59, 149927),
                dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
              ),
          Review(
                reviewId = 1,
                state=REVIEW_STATE.DECLINED,
                reviewer=self.reviewers[3],
                selfie=self.selfies[7],
                dateAssigned=datetime.datetime(2022, 11, 1, 16, 1, 59, 149927),
                dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
              ),
          Review(
                reviewId=2,
                state=REVIEW_STATE.APPROVED,
                reviewer=self.reviewers[3],
                selfie=self.selfies[8],
                dateAssigned=datetime.datetime(2022, 11, 2, 16, 1, 59, 149927),
                dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
              )

        ]