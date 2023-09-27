import json
from src.modules.get_rejected_reviews_by_reviewer.app.get_rejected_reviews_by_reviewer_presenter import lambda_handler

class Test_GetRejectedSelfiesByReviewerPresenter:

    def test_get_rejected_reviews_by_reviewer_presenter(self):
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
            "reviewerRa":"04618",
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
        
        expected = {'reviewer': {'ra': '04618', 'name': 'Bruno Cambui Marques', 'email': 'bruno.marques@maua.br', 'active': True}, 'rejectedSelfies': [{'idReview': 0, 'state': 'DECLINED', 'selfie': {'idSelfie': 0, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'DECLINED', 'rejectionReasons': ['NOT_ALLOWED_BACKGROUND'], 'rejectionDescription': 'O brilho dos olhos dela é senscaional', 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Photography', 'coords': {}, 'confidence': 100.0, 'parents': []}, {'name': 'Portrait', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Face', 'Head', 'Person', 'Photography']}, {'name': 'Head', 'coords': {}, 'confidence': 100.0, 'parents': ['Person']}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Person', 'Head']}, {'name': 'Person', 'coords': {'Width': 0.9972279071807861, 'Height': 0.88490229845047, 'Left': 0.0026419830974191427, 'Top': 0.11343356966972351}, 'confidence': 99.62065124511719, 'parents': []}]}, 'student': {'ra': '22016244', 'name': 'Isabela Pizi', 'email': '22.01624-4@maua.br'}}, 'dateAssigned': '2022-11-28T16:01:59.149927', 'dateReviewed': '2022-12-02T16:05:59.149927'}, {'idReview': 0, 'state': 'DECLINED', 'selfie': {'idSelfie': 2, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'DECLINED', 'rejectionReasons': ['NONE'], 'rejectionDescription': '', 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Person', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}]}, 'student': {'ra': '15013103', 'name': 'Hector Guerrini', 'email': '15.01310-3@maua.br'}}, 'dateAssigned': '2022-11-28T16:01:59.149927', 'dateReviewed': '2022-12-02T16:05:59.149927'}, {'idReview': 1, 'state': 'DECLINED', 'selfie': {'idSelfie': 2, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'DECLINED', 'rejectionReasons': ['NONE'], 'rejectionDescription': '', 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}, {'name': 'Person', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 98.54370880126953, 'parents': []}]}, 'student': {'ra': '15013103', 'name': 'Hector Guerrini', 'email': '15.01310-3@maua.br'}}, 'dateAssigned': '2022-11-01T16:01:59.149927', 'dateReviewed': '2022-12-02T16:05:59.149927'}, {'idReview': 1, 'state': 'DECLINED', 'selfie': {'idSelfie': 0, 'dateCreated': '2022-10-12T16:01:59.149927', 'url': 'https://i.imgur.com/4ewA19S.png', 'state': 'DECLINED', 'rejectionReasons': ['NOT_ALLOWED_BACKGROUND'], 'rejectionDescription': 'O brilho dos olhos dela é senscaional', 'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Photography', 'coords': {}, 'confidence': 100.0, 'parents': []}, {'name': 'Portrait', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Face', 'Head', 'Person', 'Photography']}, {'name': 'Head', 'coords': {}, 'confidence': 100.0, 'parents': ['Person']}, {'name': 'Face', 'coords': {'Width': 0.9711952805519104, 'Height': 0.8659809827804565, 'Left': 0.012313545681536198, 'Top': 0.11108686774969101}, 'confidence': 100.0, 'parents': ['Person', 'Head']}, {'name': 'Person', 'coords': {'Width': 0.9972279071807861, 'Height': 0.88490229845047, 'Left': 0.0026419830974191427, 'Top': 0.11343356966972351}, 'confidence': 99.62065124511719, 'parents': []}]}, 'student': {'ra': '22016244', 'name': 'Isabela Pizi', 'email': '22.01624-4@maua.br'}}, 'dateAssigned': '2022-11-01T16:01:59.149927', 'dateReviewed': '2022-12-02T16:05:59.149927'}], 'message': 'the rejected sefies by reviewer were retriven'}
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 200
        assert json.loads(response["body"]) == expected

  
    def test_get_rejected_reviews_by_reviewer_presenter_empty_list(self):
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
            "reviewerRa":"04359",
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
        
        expected = {
          "reviewer":{
              "ra":"04359",
              "name":"JOSE FERNANDO XAVIER GONCALES",
              "email":"fernando.goncales@maua.br",
              "active":True
          },
          "rejectedSelfies":[],
          "message":"the rejected sefies by reviewer were retriven"
        }
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 200
        assert json.loads(response["body"]) == expected

  
    def test_get_rejected_reviews_by_reviewer_presenter_no_items_found(self):
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
        
        expected = "No items found for reviewerRa"
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 404
        assert json.loads(response["body"]) == expected

    def test_get_rejected_reviews_by_reviewer_presenter_no_valid(self):
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
            "reviewerRa":"1234",
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
        
        expected = "Field reviewerRa is not valid"
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == expected
