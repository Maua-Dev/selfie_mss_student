import json
from datetime import datetime
from decimal import Decimal

from src.shared.domain.entities.automatic_review import AutomaticReview
from src.shared.domain.entities.label import Label
from src.shared.domain.entities.selfie import Selfie
from src.shared.domain.entities.student import Student
from src.shared.domain.enums.rejection_reason_enum import REJECTION_REASON
from src.shared.domain.enums.state_enum import STATE


class StudentDynamoDTO:
    ra: str
    name: str
    email: str

    def __init__(self, ra: str, name: str, email: str):
        self.ra = ra
        self.name = name
        self.email = email

    @staticmethod
    def from_dynamo(student_data: dict) -> "StudentDynamoDTO":
        """
        Parse data from DynamoDB to StudentDynamoDTO
        @param student_data: dict from DynamoDB
        """
        return StudentDynamoDTO(
            ra=student_data['ra'],
            name=student_data['name'],
            email=student_data['email'],
        )


    def to_entity(self) -> Student:
        """
        Parse data from SelfieDynamoDTO to Student
        """
        return Student(
            ra=self.ra,
            name=self.name,
            email=self.email,
        )


    @staticmethod
    def from_entity(student: Student) -> "StudentDynamoDTO":
        """
        Parse data from Student to StudentDynamoDTO
        """
        return StudentDynamoDTO(
            ra=student.ra,
            name=student.name,
            email=student.email,
        )

    def to_dynamo(self) -> dict:
        """
        Parse data from StudentDynamoDTO to dict
        """
        return {
            "entity": "student",
            "ra": self.ra,
            "name": self.name,
            "email": self.email,
        }




    def __repr__(self):
        return json.dumps(self.__dict__, indent=4, default=str)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

