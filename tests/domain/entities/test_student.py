import pytest
from src.helpers.errors.domain_errors import EntityError, EntityParameterTypeError
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
        with pytest.raises(EntityError) as err:
            Student(ra="21.010757", name="PyTest...",
                    email="euodeiopytest@terra.com")

    def test_student_method_validate_ra(self):
        ra_test = "21014442"
        assert Student.validate_ra(ra=ra_test) == True

    def test_student_method_validate_ra_error_dot_dash(self):
        ra_test = "21.01444-2"
        assert Student.validate_ra(ra=ra_test) == False

    def test_student_method_validate_ra_error_letter(self):
        ra_test = "21ABCs=01444-2"
        assert Student.validate_ra(ra=ra_test) == False

    def test_student_method_validate_ra_error_special_char(self):
        ra_test = "21@0144$42"
        assert Student.validate_ra(ra=ra_test) == False

    def test_student_method_validate_ra_error_nine_digits(self):
        ra_test = "2101444221"
        assert Student.validate_ra(ra=ra_test) == False

    def test_student_method_validate_ra_int(self):
        with pytest.raises(EntityParameterTypeError) as err:
            ra_test = 21014442
            Student.validate_ra(ra=ra_test)
