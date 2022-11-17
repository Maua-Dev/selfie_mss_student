import json

from src.modules.request_upload_selfie.app.request_upload_selfie_presenter import lambda_handler


class Test_RequestUploadSelfiePresenter:

    def test_request_upload_selfie(self):
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
            "body": '{"ra": "21002088","name": "MARIA LUIZA VERNASQUI VERGANI","email": "21.00208-8@maua.br"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        expected = {
                  'fields': {'AWSAccessKeyId': 'ACCESSKEY-21002088',
                             'key': '21002088/selfie-2022-11-09-20:55:11-35aa9.jpeg',
                             'policy': 'POLICY-21002088',
                             'signature': 'SIGNATURE-21002088',
                             'x-amz-meta-email': '21.00208-8@maua.br',
                             'x-amz-meta-name': 'MARIA LUIZA VERNASQUI VERGANI',
                             'x-amz-meta-ra': '21002088'},
                  'url': 'https://test-selfie-bucket.s3.amazonaws.com/',
                 }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 200
        assert json.loads(response["body"])['url'] == expected['url']
        assert json.loads(response["body"])['fields']['AWSAccessKeyId'] == expected['fields']['AWSAccessKeyId']
        assert json.loads(response["body"])['fields']['key'][:8] == expected['fields']['key'][:8]
        assert json.loads(response["body"])['fields']['policy'] == expected['fields']['policy']
        assert json.loads(response["body"])['fields']['x-amz-meta-email'] == expected['fields']['x-amz-meta-email']
        assert json.loads(response["body"])['fields']['x-amz-meta-name'] == expected['fields']['x-amz-meta-name']
        assert json.loads(response["body"])['fields']['x-amz-meta-ra'] == expected['fields']['x-amz-meta-ra']

    def test_request_upload_selfie_missing_email(self):
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
            "body":'{"ra": "21002088","name": "Scott Flansburg"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        expected = 'Field email is missing'

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == expected

    def test_request_upload_selfie_missing_name(self):
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
            "body":'{"ra": "21002088", "email": "21.00208-8@maua.br"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        expected = 'Field name is missing'

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == expected

    def test_request_upload_selfie_ra_invalid_int(self):
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
            "body": '{"ra": 21002088,"name": "Scott Flansburg","email": "calculadorahumana@florestatropical.com.uk"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        expected = 'ra must be a string'

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == expected
