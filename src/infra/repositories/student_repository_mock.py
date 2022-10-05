from typing import List
from src.domain.entities.student import Student
from src.domain.repositories.student_repository_interface import IStudentRepository

class StudentRepositoryMock(IStudentRepository):

    students:List[Student]

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
        
    def get_student(self, ra:str, email:str) -> Student:
        for student in self.students:
            if(student.ra == ra and student.email == email):
                return student
        return None