from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.get_selfies_to_review.app.get_selfies_to_review_presenter import lambda_handler
import pytest
import json


class Test_GetSelfiesToReviewPresenter:
    def test_get_selfies_to_review_presenter(self):
        repo = StudentRepositoryMock()
        
        event = {
        "version": "2.0",
        "routeKey": "$default",
        "rawPath": "/my/path", 
        "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
        "cookies": [
            "cookie1",
            "cookie2"
        ],
        "headers": {
            "header1": "value1",
            "header2": "value1,value2"
        },
        "queryStringParameters": {
            "reviewerRa":repo.reviews[3].reviewer.ra,
            "nSelfies":"5",
            "parameter2": "value"
        },
        "requestContext": {
            "accountId": "123456789012",
            "apiId": "<urlid>",
            "authentication": None,
            "authorizer": {
                "iam": {
                        "accessKey": "AKIA...",
                        "accountId": "111122223333",
                        "callerId": "AIDA...",
                        "cognitoIdentity": None,
                        "principalOrgId": None,
                        "userArn": "arn:aws:iam::111122223333:user/example-user",
                        "userId": "AIDA..."
                }
            },
            "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
            "domainPrefix": "<url-id>",
            "http": {
            "method": "POST",
            "path": "/my/path",
            "protocol": "HTTP/1.1",
            "sourceIp": "123.123.123.123",
            "userAgent": "agent"
            },
            "requestId": "id",
            "routeKey": "$default",
            "stage": "$default",
            "time": "12/Mar/2020:19:03:58 +0000",
            "timeEpoch": 1583348638390
        },
        "body": "Hello from client!",
        "pathParameters": None,
        "isBase64Encoded": None,
        "stageVariables": None
        }
    
        
        response = lambda_handler(event, None)
        assert response["statusCode"] == 200
        assert len(json.loads(response["body"])["reviews"]) == 5
        assert json.loads(response["body"])["message"] == "the reviews were retriven"

    def test_get_selfies_to_review_presenter_bad_request(self):
        repo = StudentRepositoryMock()
        
        event = {
        "version": "2.0",
        "routeKey": "$default",
        "rawPath": "/my/path", 
        "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
        "cookies": [
            "cookie1",
            "cookie2"
        ],
        "headers": {
            "header1": "value1",
            "header2": "value1,value2"
        },
        "queryStringParameters": {
            "reviewerRa":"3033030303033",
            "nSelfies":"5",
            "parameter2": "value"
        },
        "requestContext": {
            "accountId": "123456789012",
            "apiId": "<urlid>",
            "authentication": None,
            "authorizer": {
                "iam": {
                        "accessKey": "AKIA...",
                        "accountId": "111122223333",
                        "callerId": "AIDA...",
                        "cognitoIdentity": None,
                        "principalOrgId": None,
                        "userArn": "arn:aws:iam::111122223333:user/example-user",
                        "userId": "AIDA..."
                }
            },
            "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
            "domainPrefix": "<url-id>",
            "http": {
            "method": "POST",
            "path": "/my/path",
            "protocol": "HTTP/1.1",
            "sourceIp": "123.123.123.123",
            "userAgent": "agent"
            },
            "requestId": "id",
            "routeKey": "$default",
            "stage": "$default",
            "time": "12/Mar/2020:19:03:58 +0000",
            "timeEpoch": 1583348638390
        },
        "body": "Hello from client!",
        "pathParameters": None,
        "isBase64Encoded": None,
        "stageVariables": None
        }
    
        
        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field reviewerRa is not valid"

    def test_get_selfies_to_review_presenter_not_found(self):
        repo = StudentRepositoryMock()
        
        event = {
        "version": "2.0",
        "routeKey": "$default",
        "rawPath": "/my/path", 
        "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
        "cookies": [
            "cookie1",
            "cookie2"
        ],
        "headers": {
            "header1": "value1",
            "header2": "value1,value2"
        },
        "queryStringParameters": {
            "reviewerRa":"12345",
            "nSelfies":"5",
            "parameter2": "value"
        },
        "requestContext": {
            "accountId": "123456789012",
            "apiId": "<urlid>",
            "authentication": None,
            "authorizer": {
                "iam": {
                        "accessKey": "AKIA...",
                        "accountId": "111122223333",
                        "callerId": "AIDA...",
                        "cognitoIdentity": None,
                        "principalOrgId": None,
                        "userArn": "arn:aws:iam::111122223333:user/example-user",
                        "userId": "AIDA..."
                }
            },
            "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
            "domainPrefix": "<url-id>",
            "http": {
            "method": "POST",
            "path": "/my/path",
            "protocol": "HTTP/1.1",
            "sourceIp": "123.123.123.123",
            "userAgent": "agent"
            },
            "requestId": "id",
            "routeKey": "$default",
            "stage": "$default",
            "time": "12/Mar/2020:19:03:58 +0000",
            "timeEpoch": 1583348638390
        },
        "body": "Hello from client!",
        "pathParameters": None,
        "isBase64Encoded": None,
        "stageVariables": None
        }
    
        
        response = lambda_handler(event, None)
        assert response["statusCode"] == 404
        assert json.loads(response["body"]) == "No items found for reviewerRa"