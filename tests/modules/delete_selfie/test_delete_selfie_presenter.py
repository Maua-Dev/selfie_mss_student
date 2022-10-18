import pytest
from src.modules.delete_selfie.delete_selfie_presenter import lambda_handler

class Test_DeleteSelfiePresenter:

    def test_delete_selfie(self):
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
          "body": '{"ra":"21010757",  "idSelfie":"0", "parameter2": "value"}',
          "pathParameters": None,
          "isBase64Encoded": None,
          "stageVariables": None
        }
     
        
        response = lambda_handler(event, None)
        assert response["statusCode"] == 200
        assert response["body"]["student"]["name"] == "Victor"
        assert response["body"]["selfie"]["url"] == "https://drive.google.com/uc?id=12ZARnQJpkmm9dxprC8i9O7DkQPeiL0zu"        
        assert response["body"]["selfie"]["idSelfie"] == 0
        assert response["body"]["selfie"]["rejectionReason"] == "COVERED_FACE"
        assert response["body"]["selfie"]["rejectionDescription"] == "Balaclava"
        assert response["body"]['message'] == "the selfie was deleted"

    def test_delete_selfie_found(self):
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
          "body": '{"ra":"21010757",  "idSelfie":"4", "parameter2": "value"}',
          "pathParameters": None,
          "isBase64Encoded": None,
          "stageVariables": None
        }

        
        
        response = lambda_handler(event, None)
        assert response["statusCode"] == 404
        assert response["body"] == "No items found for ra or idSelfie"
  
    def test_delete_selfie_idSelfie_is_missing(self):
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
          "body": '{"ra":"21010757", "parameter2": "value"}',
          "pathParameters": None,
          "isBase64Encoded": None,
          "stageVariables": None
        }


        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert response["body"] == "Field idSelfie is missing"
        
    def test_delete_selfie_student_not_found(self):
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
            "ra":"21019302",
            "idSelfie":"1",
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
          "body": '{"ra":"21019302",  "idSelfie":"1", "parameter2": "value"}',
          "pathParameters": None,
          "isBase64Encoded": None,
          "stageVariables": None
        }


        response = lambda_handler(event, None)
        assert response["statusCode"] == 404
        assert response["body"] == "No items found for ra or idSelfie"