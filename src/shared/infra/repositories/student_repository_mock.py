import datetime
from turtle import st
from typing import List, Tuple
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.entities.student import Student
from src.shared.domain.repositories.student_repository_interface import IStudentRepository

class StudentRepositoryMock(IStudentRepository):

    students: List[Student]

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
            )
        ]

        self.selfies = [
            Selfie(
                idSelfie=0,
                student=self.students[0],
                dateUpload=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/0KFBHTB.jpg",
                state=STATE.DECLINED,
                rejectionReason=REJECTION_REASON.COVERED_FACE,
                rejectionDescription="Balaclava"
            ),
            Selfie(
                idSelfie=1,
                student=self.students[0],
                dateUpload=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/b9qFYmb.jpg",
                state=STATE.APPROVED,
                rejectionReason = REJECTION_REASON.NONE,
                rejectionDescription = ""
            ),
            Selfie(
                idSelfie=0,
                student=self.students[1],
                dateUpload=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/dv7Q5VT.jpg",
                state=STATE.PENDING_REVIEW,
                rejectionReason = REJECTION_REASON.NONE,
                rejectionDescription = ""
            ),
            Selfie(
                idSelfie=0,
                student=self.students[2],
                dateUpload=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://pps.whatsapp.net/v/t61.24694-24/56153869_1240493612792530_7354067850044112896_n.jpg?ccb=11-4&oh=01_AVydS_LW2WM2tLLKeEKbZIAlVJCbgJlfZ96y3yQnXAFBEA&oe=635822E5",
                state=STATE.APPROVED,
                rejectionReason = REJECTION_REASON.NONE,
                rejectionDescription = ""
            ),
            Selfie(
                idSelfie=0,
                student=self.students[3],
                dateUpload=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/4ewA19S.png",
                state=STATE.IN_REVIEW,
                rejectionReason = REJECTION_REASON.NONE,
                rejectionDescription = ""
            ),
        ]

    def get_student(self, ra: str) -> Student:
        for student in self.students:
            if(student.ra == ra):
                return student
        return None

    def update_student(self, ra: str, new_name: str = None, new_email: str = None) -> Student:
        idxStudent = -1

        for idx, possible_student in enumerate(self.students):
            if(possible_student.ra == ra):
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
            if(self.students[idx].ra == ra):
                student = self.students.pop(idx)
                return student
        raise NoItemsFound("ra")

    def create_student(self, student: Student) -> Student:
        self.students.append(student)

        return student
    
    def get_selfies_by_ra(self, ra) -> Tuple[List[Selfie], Student]:
        return [selfie for selfie in self.selfies if selfie.student.ra == ra]
            
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
    
    def create_selfie(self, ra: str, url: str) -> Selfie:
        
        student = self.get_student(ra=ra)
        if student == None:
            raise NoItemsFound("ra")
        
        selfie = Selfie(
            student=student,
            dateUpload=datetime.datetime.now(),
            idSelfie=len(self.get_selfies_by_ra(ra=ra)),
            state=STATE.PENDING_REVIEW,
            url=url,
            rejectionReason = REJECTION_REASON.NONE,
            rejectionDescription = ""
            )
        
        self.selfies.append(selfie)
        
        return selfie
        
        
        
                
        