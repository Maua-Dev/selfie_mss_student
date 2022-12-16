from src.shared.infra.dtos.reviewer_dynamo_dto import ReviewerDynamoDTO
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock


class Test_ReviewerDynamoDTO:
    def test_from_entity(self):
        repo = StudentRepositoryMock()      
        reviewer_entity = repo.reviewers[0]
        
        assert ReviewerDynamoDTO.from_entity(reviewer=reviewer_entity).__dict__ == {
                                                                    "ra":reviewer_entity.ra,
                                                                    "name":reviewer_entity.name,
                                                                    "email":reviewer_entity.email,
                                                                    "active":reviewer_entity.active
                                                                }
        
    def test_to_dynamo(self):
        repo = StudentRepositoryMock()      
        reviewer_dto = ReviewerDynamoDTO.from_entity(reviewer=repo.reviewers[0])
        
        assert reviewer_dto.to_dynamo() == {
                                                "entity": "reviewer",
                                                "ra":reviewer_dto.ra,
                                                "name":reviewer_dto.name,
                                                "email":reviewer_dto.email,
                                                "active":reviewer_dto.active
                                            }
        
    def test_from_dynamo(self):
        repo = StudentRepositoryMock()     
        
        reviewer_dynamo = {'Item': {'name': 'Mauro Crapino', 'SK': '03026', 'active': True, 'PK': 'reviewer#03026', 'entity': 'reviewer', 'email': 'mauro@maua.br', 'ra': '03026'}, 'ResponseMetadata': {'RequestId': 'dc2ed159-1780-4994-8ba1-57b4f5f307d4', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 18:43:58 GMT', 'content-type': 'application/x-amz-json-1.0', 'x-amz-crc32': '1749714046', 'x-amzn-requestid': 'dc2ed159-1780-4994-8ba1-57b4f5f307d4', 'content-length': '184', 'server': 'Jetty(9.4.48.v20220622)'}, 'RetryAttempts': 0}}
        reviewer_entity = repo.reviewers[0]
        assert ReviewerDynamoDTO.from_entity(reviewer=reviewer_entity)  == ReviewerDynamoDTO.from_dynamo(reviewer_data=reviewer_dynamo["Item"])
        
    def test_to_entity(self):
        repo = StudentRepositoryMock()     
        reviewer_entity = repo.reviewers[0]
        reviewer_from_entity_to_entity = ReviewerDynamoDTO.from_entity(reviewer=reviewer_entity)
        assert reviewer_entity.__dict__ == reviewer_from_entity_to_entity.__dict__
        