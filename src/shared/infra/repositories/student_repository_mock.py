import datetime
from typing import Dict, List, Tuple
from src.shared.domain.entities.automatic_review import AutomaticReview
from src.shared.domain.entities.label import Label
from src.shared.domain.entities.review import Review
from src.shared.domain.entities.reviewer import Reviewer
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.enums.review_state_enum import REVIEW_STATE
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.entities.student import Student
from src.shared.domain.repositories.student_repository_interface import IStudentRepository


class StudentRepositoryMock(IStudentRepository):
    students: List[Student]
    selfies: List[Selfie]
    reviewers: List[Reviewer]
    reviews: List[Review]

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
                idReview = 0,
                state=REVIEW_STATE.APPROVED,
                reviewer=self.reviewers[0],
                selfie=self.selfies[1],
                dateAssigned=datetime.datetime(2022, 12, 1, 16, 1, 59, 149927),
                dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
              ),
          Review(
                idReview = 0,
                state=REVIEW_STATE.APPROVED,
                reviewer=self.reviewers[0],
                selfie=self.selfies[3],
                dateAssigned=datetime.datetime(2022, 11, 30, 16, 1, 59, 149927),
                dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
              ),
          Review(
                idReview = 0,
                state=REVIEW_STATE.APPROVED,
                reviewer=self.reviewers[2],
                selfie=self.selfies[4],
                dateAssigned=datetime.datetime(2022, 11, 9, 16, 1, 59, 149927),
                dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
              ),
          Review(
                idReview = 0,
                state=REVIEW_STATE.PENDING_VALIDATION,
                reviewer=self.reviewers[3],
                selfie=self.selfies[5],
                dateAssigned=datetime.datetime(2022, 11, 28, 16, 1, 59, 149927),
                dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
              ),
          Review(
                idReview = 0,
                state=REVIEW_STATE.PENDING_VALIDATION,
                reviewer=self.reviewers[3],
                selfie=self.selfies[9],
                dateAssigned=datetime.datetime(2022, 11, 28, 16, 1, 59, 149927),
                dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
              ),
          Review(
                idReview = 0,
                state=REVIEW_STATE.PENDING_VALIDATION,
                reviewer=self.reviewers[3],
                selfie=self.selfies[8],
                dateAssigned=datetime.datetime(2022, 11, 28, 16, 1, 59, 149927),
                dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
              ),
          Review(
                idReview = 0,
                state=REVIEW_STATE.PENDING_VALIDATION,
                reviewer=self.reviewers[3],
                selfie=self.selfies[7],
                dateAssigned=datetime.datetime(2022, 11, 28, 16, 1, 59, 149927),
                dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
              ),
          Review(
                idReview = 1,
                state=REVIEW_STATE.DECLINED,
                reviewer=self.reviewers[3],
                selfie=self.selfies[7],
                dateAssigned=datetime.datetime(2022, 11, 1, 16, 1, 59, 149927),
                dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
              ),
          Review(
                idReview=2,
                state=REVIEW_STATE.APPROVED,
                reviewer=self.reviewers[3],
                selfie=self.selfies[8],
                dateAssigned=datetime.datetime(2022, 11, 2, 16, 1, 59, 149927),
                dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
              ),
          Review(
                idReview = 1,
                state=REVIEW_STATE.DECLINED,
                reviewer=self.reviewers[3],
                selfie=self.selfies[9],
                dateAssigned=datetime.datetime(2022, 11, 1, 16, 1, 59, 149927),
                dateReviewed=datetime.datetime(2022, 12, 2, 16, 5, 59, 149927)
              )
        ]

        
    def get_student(self, ra: str) -> Student:
        for student in self.students:
            if (student.ra == ra):
                return student
        return None

    def update_student(self, ra: str, new_name: str = None, new_email: str = None) -> Student:
        idxStudent = -1

        for idx, possible_student in enumerate(self.students):
            if (possible_student.ra == ra):
                student = possible_student
                idxStudent = idx
                break

        if idxStudent == -1:
            raise NoItemsFound("ra")

        if new_name != None:
            student.name = new_name

        if new_email != None:
            student.email = new_email

        self.students[idxStudent] = student

        return self.students[idxStudent]

    def delete_student(self, ra: str) -> Student:
        for idx in range(len(self.students)):
            if (self.students[idx].ra == ra):
                student = self.students.pop(idx)
                return student
        raise NoItemsFound("ra")

    def create_student(self, student: Student) -> Student:
        self.students.append(student)

        return student

    def get_selfies_by_ra(self, ra) -> Tuple[List[Selfie], Student]:

        student = self.get_student(ra=ra)

        if student == None:
            raise NoItemsFound("ra")

        selfies = [selfie for selfie in self.selfies if selfie.student.ra == ra]

        selfies.sort(key=lambda x: x.dateCreated)

        return selfies, student

    def get_selfie(self, ra: str, idSelfie: int) -> Selfie:
        for selfie in self.selfies:
            if selfie.student.ra == ra and selfie.idSelfie == idSelfie:
                return selfie
        return None

    def delete_selfie(self, ra: str, idSelfie: int) -> Tuple[Selfie, Student]:

        for idx, selfie in enumerate(self.selfies):
            if selfie.student.ra == ra and selfie.idSelfie == idSelfie:
                return self.selfies.pop(idx), selfie.student
        return None, None

    def create_selfie(self, selfie: Selfie) -> Selfie:
        self.selfies.append(selfie)

        return selfie

    def update_selfie(self, ra: str, idSelfie: int, new_state: STATE = None,
                      new_rejectionReasons: list[REJECTION_REASON] = None,
                      new_rejectionDescription: str = None) -> Selfie:
        idxSelfie = -1
        for idx in range(len(self.selfies)):
            if self.selfies[idx].student.ra == ra and self.selfies[idx].idSelfie == idSelfie:
                idxSelfie = idx

        if idxSelfie == -1:
            raise NoItemsFound("idSelfie")

        if new_state != None:
            self.selfies[idxSelfie].state = new_state

        if new_rejectionReasons != None:
            self.selfies[idxSelfie].rejectionReasons = new_rejectionReasons

        if new_rejectionDescription != None:
            self.selfies[idxSelfie].rejectionDescription = new_rejectionDescription

        return self.selfies[idxSelfie]

    def get_all_selfies(self) -> List[Selfie]:
        
        all_selfies = self.selfies
        all_selfies.sort(key=lambda x: x.dateCreated)
        
        return all_selfies

    def check_student_has_approved_selfie(self, ra: str) -> bool:
        selfies, student = self.get_selfies_by_ra(ra=ra)
        for selfie in selfies:
            if selfie.state == STATE.APPROVED:
                return True

        return False

    def get_all_students(self) -> List[Tuple[List[Selfie], Student]]:
        all_students = list()
        for student in self.students:
            all_students.append(self.get_selfies_by_ra(ra=student.ra))

        return all_students
    
    def get_review(self, idReview: int, idSelfie:int, studentRa:str) -> Review:
        for review in self.reviews:
            if review.idReview == idReview and idSelfie == review.selfie.idSelfie and review.selfie.student.ra == studentRa:
                return review
            
        return None
    
    def create_review(self, review: Review) -> Review:
        self.reviews.append(review)
        
        return review
    
    def update_review(self, idReview: int, idSelfie:int, studentRa:str, new_state: REVIEW_STATE = None, new_rejectionReasons: List[REJECTION_REASON] = None, new_rejectionDescription: str = None) -> Review:
        
        review = self.get_review(idReview=idReview, idSelfie=idSelfie, studentRa=studentRa)
        
        if new_state != None:
            review.state = new_state
            
        review.selfie = self.update_selfie(ra=studentRa, idSelfie=idSelfie, new_state=STATE[new_state.value], new_rejectionDescription=new_rejectionDescription, new_rejectionReasons=new_rejectionReasons)
        review.dateReviewed = datetime.datetime.now()
        return review
    
    def delete_review(self, reviewerRa: str, idReview: int, idSelfie:int, studentRa:str) -> Review:
        for idx, review in enumerate(self.reviews):
            if review.idReview == idReview and review.reviewer.ra == reviewerRa and idSelfie == review.selfie.idSelfie and review.selfie.student.ra == studentRa:
                return self.reviews.pop(idx)
        

    def create_reviewer(self, reviewer: Reviewer) -> Reviewer:
        self.reviewers.append(reviewer)

        return reviewer
    
    def update_reviewer(self, ra: str, new_name: str = None, new_email: str = None, new_active: bool = None) -> Reviewer:
        idxReviewer = -1

        for idx, possible_reviewer in enumerate(self.reviewers):
            if (possible_reviewer.ra == ra):
                reviewer = possible_reviewer
                idxReviewer = idx
                break

        if idxReviewer == -1:
            raise NoItemsFound("ra")

        if new_name != None:
            reviewer.name = new_name

        if new_email != None:
            reviewer.email = new_email

        if new_active != None:
            reviewer.active = new_active

        self.reviewers[idxReviewer] = reviewer

        return self.reviewers[idxReviewer]

    def delete_reviewer(self, ra: str) -> Reviewer:
        for idx in range(len(self.reviewers)):
            if (self.reviewers[idx].ra == ra):
                reviewer = self.reviewers.pop(idx)
                return reviewer
        raise NoItemsFound("ra")

    def get_reviewer(self, ra: str) -> Reviewer:
        for reviewer in self.reviewers:
            if (reviewer.ra == ra):
                return reviewer
        return None

    def get_rejected_reviews_by_reviewer(self, reviewerRa: str) -> Tuple[Reviewer, List[Review]]:
        reviews = list()
        reviewer = self.get_reviewer(reviewerRa)
        if reviewer == None:
            raise NoItemsFound("reviewerRa")
        
        for review in self.reviews:
            if review.reviewer.ra == reviewerRa and review.state == REVIEW_STATE.DECLINED:
                reviews.append(review)

        return reviewer, reviews  

    def get_approved_selfies_by_reviewer(self, reviewerRa: str) -> Tuple[Reviewer, List[Review]]:
        reviews = list()
        reviewer = self.get_reviewer(reviewerRa)
        if reviewer == None:
            raise NoItemsFound("reviewerRa")
        
        for review in self.reviews:
            if review.reviewer.ra == reviewerRa and review.state == REVIEW_STATE.APPROVED:
                reviews.append(review)

        return reviewer, reviews
    
    def get_pending_validation_selfies_assigned(self, reviewerRa: str) -> List[Review]:
        return [review for review in self.reviews if review.reviewer.ra == reviewerRa and review.state == REVIEW_STATE.PENDING_VALIDATION]            
    
    def assign_selfies(self, reviewer: Reviewer, nSelfies: int) -> List[Review]:
        new_assign_reviews = list()
        counter = 0
        
        for idx, selfie in enumerate(self.get_all_selfies()):
            if counter == nSelfies:
                break
            if selfie.state == STATE.PENDING_REVIEW:
                self.selfies[idx].state = STATE.IN_REVIEW
                review = Review(
                    selfie=selfie,
                    dateAssigned=datetime.datetime.now(),
                    reviewer=reviewer,
                    state=REVIEW_STATE.PENDING_VALIDATION,
                    idReview=len([review for review in self.reviews if review.selfie.url == selfie.url and review.selfie.student.ra == selfie.student.ra])
                )
                new_assign_reviews.append(review)
                counter += 1
                
        return new_assign_reviews
    
    def get_selfies_to_review(self, reviewerRa: str, nSelfies: int = 10) -> Tuple[List[Review], Reviewer]:
        reviewer = self.get_reviewer(ra=reviewerRa)
        
        if reviewer == None:
            raise NoItemsFound("reviewerRa")
        
        selfies_to_review = self.get_pending_validation_selfies_assigned(reviewerRa=reviewerRa)
        
        if len(selfies_to_review) < nSelfies:
            new_assigned_selfies = self.assign_selfies(nSelfies=nSelfies-len(selfies_to_review), reviewer=reviewer)
            selfies_to_review.extend(new_assigned_selfies)
        
    
        return selfies_to_review, reviewer

    def approve_selfie(self, studentRa: str, idSelfie: int, idReview: int) -> Review:
        review = self.get_review(idReview=idReview, idSelfie=idSelfie, studentRa=studentRa)
        review.state = REVIEW_STATE.APPROVED
        review.dateReviewed = datetime.datetime.now()
        
        review.selfie = self.update_selfie(ra=studentRa, idSelfie=idSelfie, new_state=STATE.APPROVED)
        return review
        
    def reject_selfie(self, studentRa: str, idSelfie: int, idReview: int, new_rejectionReasons: list[REJECTION_REASON] = None, new_rejectionDescription: str = None) -> Review:
        review = self.get_review(idReview=idReview, idSelfie=idSelfie, studentRa=studentRa)
        
        review.state = REVIEW_STATE.DECLINED
        review.selfie.state = STATE.DECLINED
        
        if new_rejectionDescription != None:
            review.selfie.rejectionDescription = new_rejectionDescription
        
        if new_rejectionReasons != None:
            review.selfie.rejectionReasons = new_rejectionReasons
        review.dateReviewed = datetime.datetime.now()
                
        self.update_selfie(ra=studentRa, idSelfie=idSelfie, new_state=STATE.DECLINED)
        return review
            
