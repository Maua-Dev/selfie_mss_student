from src.shared.environments import Environments
from src.shared.infra.repositories.student_repository_dynamo import StudentRepositoryDynamo
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
import os
import boto3


def setup_dynamo_table():
    print('Setting up dynamo table...')
    dynamo_client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
    tables = dynamo_client.list_tables()['TableNames']

    if not tables:
        print('Creating table...')
        dynamo_client.create_table(
            TableName='selfie_mss_student-table',
            KeySchema=[
                {
                    'AttributeName': 'PK',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'SK',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'PK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'SK',
                    'AttributeType': 'S'
                }
            ],
            BillingMode='PAY_PER_REQUEST'
        )
        print('Table "selfie_mss_student-table" created!\n')
    else:
        print('Table already exists!\n')



def load_mock_to_local_dynamo():


    if Environments.get_envs().endpoint_url == 'http://localhost:8000':
        setup_dynamo_table()


    # os.environ["STAGE"] = "TEST"
    mock_repo = StudentRepositoryMock()
    dynamo_repo = StudentRepositoryDynamo()

    print('Loading mock data to dynamo...')

    print('Loading students...')
    count = 0
    for student in mock_repo.students:
        print(f'Loading student {student.ra} | {student.name}...')
        dynamo_repo.create_student(student)
        count += 1
    print(f'{count} students loaded!\n')

    print('\nLoading Selfies...')
    count = 0
    for selfie in mock_repo.selfies:
        print(f'Loading selfie {selfie.student.ra} - {selfie.idSelfie} | {selfie.url}...')
        dynamo_repo.create_selfie(selfie)
        count += 1
    print(f'{count} selfies loaded!\n')

    print('Done!')


if __name__ == '__main__':
    load_mock_to_local_dynamo()
