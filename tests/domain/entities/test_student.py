from src.domain.entities.student import Student

class Test_Student():
    def test_student(self):
        student = Student(
            ra = "21010757",
            name="PyTest...",
            email="euodeiopytest@terra.com"
        )
        
        assert True == True