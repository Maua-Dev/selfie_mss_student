import pytest
from src.shared.helpers.errors.domain_errors import EntityError, EntityParameterTypeError
from src.shared.domain.entities.student import Student


class Test_Student():
    def test_student(self):
        student = Student(ra="21010757", name="Guardanapo",
                          email="euodeiopytest@terra.com")

        assert type(student) == Student

    def test_student_ra_must_be_decimal(self):
        with pytest.raises(EntityError):
            student = Student(ra="Guardana", name="Guardanapo",
                          email="euodeiopytest@terra.com")

        

    def test_student_error_ra(self):
        with pytest.raises(EntityError):
            Student(ra='', name='EhSobreIsso', email='palavrao@nao.com')
            
    def test_student_error_name(self):
        with pytest.raises(EntityError):
            Student(ra='19003315', name='', email='aws@boy.com')
            
    def test_student_error_email(self):
        with pytest.raises(EntityError):
            Student(ra='19003315', name='Bruno Vilardi Bueno', email='aws.com')

    def test_student_ra_with_dot(self):
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
    
    def test_student_method_validate_email(self):
        email_test = "awsboi@aws.com"
        assert Student.validate_email(email=email_test) == True

    def test_student_method_validate_email_without_atmark(self):
        email_test = "awsboiaws.com"
        assert Student.validate_email(email=email_test) == False

    def test_student_method_validate_email_without_final_dot(self):
        email_test = "awsboi@awscom"
        assert Student.validate_email(email=email_test) == False
    
    def test_student_float(self):
        with pytest.raises(EntityError):
            student = Student(ra=1.2, name="Guardanapo",
                            email="euodeiopytest@terra.com")

    def test_student_float(self):
            with pytest.raises(EntityError):
                student = Student(ra=21014442.0, name="Guardanapo",
                                email="euodeiopytest@terra.com")
