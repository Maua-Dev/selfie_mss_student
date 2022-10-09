from itertools import count
from typing import List
from src.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from src.domain.entities.student import Student
from src.domain.repositories.student_repository_interface import IStudentRepository


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

    def get_student(self, ra: str) -> Student:
        for student in self.students:
            if(student.ra == ra):
                return student
        return None

    def update_student(self, ra: str, new_name: str = None, new_email: str = None) -> None:

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

    def create_student(self, ra: str, name: str, email: str) -> None:


        for student in self.students:
            if(student.ra == ra and student.email == email):
                raise DuplicatedItem("ra and email")
            elif(student.email == email):
                raise DuplicatedItem("email")
            elif(student.ra == ra):
                raise DuplicatedItem("ra")

        student = Student(
            ra=ra,
            name=name,
            email=email
        )

        self.students.append(student)
