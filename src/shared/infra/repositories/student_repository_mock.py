import datetime
from typing import Dict, List, Tuple
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.entities.student import Student
from src.shared.domain.repositories.student_repository_interface import IStudentRepository

class StudentRepositoryMock(IStudentRepository):

    students: List[Student]
    selfies: List[Selfie]
    
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
                rejectionReason=REJECTION_REASON.COVERED_FACE,
                rejectionDescription="Balaclava"
            ),
            Selfie(
                idSelfie=1,
                student=self.students[0],
                dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/b9qFYmb.jpg",
                state=STATE.APPROVED,
                rejectionReason = REJECTION_REASON.NONE,
                rejectionDescription = ""
            ),
            Selfie(
                idSelfie=0,
                student=self.students[1],
                dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/dv7Q5VT.jpg",
                state=STATE.PENDING_REVIEW,
                rejectionReason = REJECTION_REASON.NONE,
                rejectionDescription = ""
            ),
            Selfie(
                idSelfie=0,
                student=self.students[2],
                dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://pps.whatsapp.net/v/t61.24694-24/56153869_1240493612792530_7354067850044112896_n.jpg?ccb=11-4&oh=01_AVydS_LW2WM2tLLKeEKbZIAlVJCbgJlfZ96y3yQnXAFBEA&oe=635822E5",
                state=STATE.APPROVED,
                rejectionReason = REJECTION_REASON.NONE,
                rejectionDescription = ""
            ),
            Selfie(
                idSelfie=0,
                student=self.students[3],
                dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/4ewA19S.png",
                state=STATE.IN_REVIEW,
                rejectionReason = REJECTION_REASON.NONE,
                rejectionDescription = ""
            ),
            Selfie(
                idSelfie=0,
                student=self.students[5],
                dateCreated=datetime.datetime(2022, 10, 1, 16, 1, 59, 149927),
                url="https://i.imgur.com/4ewA19S.png",
                state=STATE.DECLINED,
                rejectionReason = REJECTION_REASON.COVERED_FACE,
                rejectionDescription = "Usou chapéu de mexicano que cobriu a cara"
            ),
            Selfie(
                idSelfie=1,
                student=self.students[5],
                dateCreated=datetime.datetime(2022, 10, 2, 16, 1, 59, 149927),
                url="https://i.imgur.com/4ewA19S.png",
                state=STATE.DECLINED,
                rejectionReason = REJECTION_REASON.BRIGHT_BACKGROUND,
                rejectionDescription = "Tirou foto no meio da Rave, enquanto aparecia um brilho forte"
            ),
            Selfie(
                idSelfie=2,
                student=self.students[5],
                dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/4ewA19S.png",
                state=STATE.APPROVED,
                rejectionReason = REJECTION_REASON.NONE,
                rejectionDescription = ""
            ),
            Selfie(
                idSelfie=2,
                student=self.students[5],
                dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/4ewA19S.png",
                state=STATE.APPROVED,
                rejectionReason = REJECTION_REASON.NONE,
                rejectionDescription = ""
            ),
            Selfie(
                idSelfie=0,
                student=self.students[6],
                dateCreated=datetime.datetime(2022, 10, 12, 16, 1, 59, 149927),
                url="https://i.imgur.com/4ewA19S.png",
                state=STATE.DECLINED,
                rejectionReason = REJECTION_REASON.BRIGHT_BACKGROUND,
                rejectionDescription = "O brilho dos olhos dela é senscaional"
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
        
        student = self.get_student(ra=ra)
        
        if student ==  None:
            raise NoItemsFound("ra")
   
        selfies = [selfie for selfie in self.selfies if selfie.student.ra == ra]
        
        selfies.sort(key=lambda x:x.dateCreated)

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
        
    def update_selfie(self, ra: str, idSelfie: int, new_state: STATE, new_rejectionReason: REJECTION_REASON, new_rejectionDescription: str) -> Selfie:
        idxSelfie = -1
        for idx in range(len(self.selfies)):
            if self.selfies[idx].student.ra == ra and self.selfies[idx].idSelfie == idSelfie:
                    idxSelfie = idx
                    
        if idxSelfie == -1:
            raise NoItemsFound("idSelfie")
        
        if new_state != None:
            self.selfies[idxSelfie].state = new_state
            
        if new_rejectionReason != None:
            self.selfies[idxSelfie].rejectionReason = new_rejectionReason
            
        if new_rejectionDescription != None:
            self.selfies[idxSelfie].rejectionDescription = new_rejectionDescription
            
        return self.selfies[idxSelfie]   


    def get_all_selfies(self) -> List[Selfie]:
        return self.selfies    
    
    def check_student_has_approved_selfie(self, ra: str) -> bool:
        selfies, student = self.get_selfies_by_ra(ra=ra)
        for selfie in selfies:
            if selfie.state == STATE.APPROVED:
                return True
            
        return False 
    
    def get_all_students(self) -> List[Student]:
        return self.students
            
        
                
       