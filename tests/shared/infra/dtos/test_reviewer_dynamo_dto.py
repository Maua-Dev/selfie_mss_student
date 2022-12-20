from src.shared.infra.dtos.reviewer_dynamo_dto import ReviewerDynamoDTO
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock


class Test_ReviewerDynamoDTO:
    def test_from_entity(self):
        repo = StudentRepositoryMock()      
        reviewer_entity = repo.reviewers[0]
        reviewer_dto = ReviewerDynamoDTO(
            ra=repo.reviewers[0].ra,
            name=repo.reviewers[0].name,
            email=repo.reviewers[0].email,
            active=repo.reviewers[0].active
        )
        
        assert ReviewerDynamoDTO.from_entity(reviewer=reviewer_entity) == reviewer_dto
        
    def test_to_dynamo(self):
        repo = StudentRepositoryMock()      
        reviewer_dto = ReviewerDynamoDTO(
            ra=repo.reviewers[0].ra,
            name=repo.reviewers[0].name,
            email=repo.reviewers[0].email,
            active=repo.reviewers[0].active
        )
        
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
        reviewer_dto = ReviewerDynamoDTO(
            ra=repo.reviewers[0].ra,
            name=repo.reviewers[0].name,
            email=repo.reviewers[0].email,
            active=repo.reviewers[0].active
        )
        assert reviewer_dto == ReviewerDynamoDTO.from_dynamo(reviewer_data=reviewer_dynamo["Item"])
        
    def test_to_entity(self):
        repo = StudentRepositoryMock()     
        reviewer_entity = repo.reviewers[0]
        reviewer_dto = ReviewerDynamoDTO(
            ra=repo.reviewers[0].ra,
            name=repo.reviewers[0].name,
            email=repo.reviewers[0].email,
            active=repo.reviewers[0].active
        )
        reviewer_from_entity_to_entity = reviewer_dto.to_entity()
        assert reviewer_entity.__dict__ == reviewer_from_entity_to_entity.__dict__
        
    def test_from_entity_to_dynamo(self):
        repo = StudentRepositoryMock()     
        reviewer_dynamo = {
                            "entity": "reviewer",
                            "ra":repo.reviewers[0].ra,
                            "name":repo.reviewers[0].name,
                            "email":repo.reviewers[0].email,
                            "active":repo.reviewers[0].active
                        }
        
        assert reviewer_dynamo == ReviewerDynamoDTO.from_entity(reviewer=repo.reviewers[0]).to_dynamo()
        
    def test_from_dynamo_to_entity(self):
        repo = StudentRepositoryMock()     
        reviewer_dynamo = {'Item': {'name': 'Mauro Crapino', 'SK': '03026', 'active': True, 'PK': 'reviewer#03026', 'entity': 'reviewer', 'email': 'mauro@maua.br', 'ra': '03026'}, 'ResponseMetadata': {'RequestId': 'dc2ed159-1780-4994-8ba1-57b4f5f307d4', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Fri, 16 Dec 2022 18:43:58 GMT', 'content-type': 'application/x-amz-json-1.0', 'x-amz-crc32': '1749714046', 'x-amzn-requestid': 'dc2ed159-1780-4994-8ba1-57b4f5f307d4', 'content-length': '184', 'server': 'Jetty(9.4.48.v20220622)'}, 'RetryAttempts': 0}}
        
        assert repo.reviewers[0].__dict__ == ReviewerDynamoDTO.from_dynamo(reviewer_data=reviewer_dynamo["Item"]).to_entity().__dict__