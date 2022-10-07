import pytest
from src.helpers.errors.domain_errors import EntityError
from src.domain.entities.student import Student


class Test_Student():
    def test_student(self):
        student = Student(ra="21010757", name="PyTest...",
                          email="euodeiopytest@terra.com")

        assert type(student) == Student

    def test_student_error(self):
        with pytest.raises(EntityError):
            Student(ra='', name='', email='')

    def test_student_ra_not_number(self):
        with pytest.raises(EntityError):
            Student(ra="21.010757", name="PyTest...",
                    email="euodeiopytest@terra.com")
