from src.shared.infra.repositories.student_repository_dynamo import StudentRepositoryDynamo
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
import os


def load_mock_to_local_dynamo():
    os.environ["STAGE"] = "TEST"
    mock_repo = StudentRepositoryMock()
    dynamo_repo = StudentRepositoryDynamo()

    print('Loading mock data to dynamo...')

    print('Loading students...')
    for student in mock_repo.students:
        print(f'Loading student {student.ra} | {student.name}...')
        dynamo_repo.create_student(student)

    print('\nLoading Selfies...')
    for selfie in mock_repo.selfies:
        print(f'Loading selfie {selfie.student.ra} - {selfie.idSelfie} | {selfie.url}...')
        dynamo_repo.create_selfie(selfie)

    print('Done!')


if __name__ == '__main__':
    load_mock_to_local_dynamo()
