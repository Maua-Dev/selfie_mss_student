import datetime
from typing import List
from src.domain.entities.selfie import Selfie
from src.domain.enums.state_enum import STATE
from src.helpers.errors.usecase_errors import NoItemsFound
from src.domain.entities.student import Student
from src.domain.repositories.student_repository_interface import IStudentRepository

"""
selfieId: int
    student: Student
    dateUpload: datetime.datetime
    url: str
    state: STATE
"""

"""
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"
    IN_REVIEW = "IN_REVIEW"
    PENDING_REVIEW = "PENDING_REVIEW"
    NOT_SENT = "NOT_SENT"
"""


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
                selfieId=0,
                student=self.students[0],
                dateUpload=datetime.datetime.now(),
                url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                state=STATE.DECLINED
            ),
            Selfie(
                selfieId=1,
                student=self.students[0],
                dateUpload=datetime.datetime.now(),
                url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                state=STATE.APPROVED
            ),
            Selfie(
                selfieId=0,
                student=self.students[1],
                dateUpload=datetime.datetime.now(),
                url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                state=STATE.PENDING_REVIEW
            ),
            Selfie(
                selfieId=0,
                student=self.students[2],
                dateUpload=datetime.datetime.now(),
                url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                state=STATE.APPROVED
            ),
            Selfie(
                selfieId=0,
                student=self.students[3],
                dateUpload=datetime.datetime.now(),
                url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                state=STATE.IN_REVIEW
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
