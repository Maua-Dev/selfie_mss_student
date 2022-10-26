import json

from src.modules.create_selfie.app.create_selfie_presenter import lambda_handler


class Test_CreateSelfiePresenter:

    def test_create_selfie(self):
        event = {
        'version': '2.0',
        'routeKey': '$default',
        'rawPath': '/',
        'rawQueryString':'',
        'headers':
        {'content-length': '85',
        'x-amzn-tls-version':'TLSv1.2',
        'x-forwarded-proto': 'https',
        'postman-token': 'd29237ea-84e1-4702-9468-66a524684090',
        'x-forwarded-port': '443',
        'x-forwarded-for': '191.193.227.175',
        'accept': '*/*',
        'x-amzn-tls-cipher-suite': 'ECDHE-RSA-AES128-GCM-SHA256',
        'x-amzn-trace-id': 'Root=1-634dedaf-6307b9c627f4d40e777ad9cd',
        'host': 'd2w3ehxv3vp45jbnpflej2oxue0kbsny.lambda-url.us-east-1.on.aws',
        'content-type': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'user-agent': 'PostmanRuntime/7.29.2'},
        'requestContext':
        {'accountId': 'anonymous', 'apiId': 'd2w3ehxv3vp45jbnpflej2oxue0kbsny', 'domainName': 'd2w3ehxv3vp45jbnpflej2oxue0kbsny.lambda-url.us-east-1.on.aws', 'domainPrefix': 'd2w3ehxv3vp45jbnpflej2oxue0kbsny', 'http': {'method': 'POST', 'path': '/', 'protocol': 'HTTP/1.1', 'sourceIp': '191.193.227.175', 'userAgent': 'PostmanRuntime/7.29.2'}, 'requestId': 'f7ef0445-f100-4362-bb4a-13772177292b', 'routeKey': '$default', 'stage': '$default', 'time': '18/Oct/2022:00:05:03 +0000', 'timeEpoch': 1666051503383}, 'body': '{\r\n    "ra": "21010757",\r\n    "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q"\r\n}', 'isBase64Encoded': False}


        response = lambda_handler(event, None)
        assert response["statusCode"] == 201
        assert json.loads(response["body"])["idSelfie"] == 2
        assert json.loads(response["body"])["rejectionReason"] == "NONE"
        assert json.loads(response["body"])["rejectionDescription"] == None
        assert json.loads(response["body"])["state"] == "PENDING_REVIEW"
        assert json.loads(response["body"])["student"]["ra"] == "21010757"

    def test_create_selfie_missing_ra(self):
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
            'body': '{\r\n "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q"\r\n}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        expected = 'Field ra is missing'

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == expected

    def test_create_selfie_ra_invalid_int(self):
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
            'body': '{\r\n    "ra": 21010757,\r\n "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q"\r\n}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        expected = 'ra must be a string'

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == expected
        
    def test_create_selfie_not_found_ra(self):
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
            'body': '{\r\n    "ra": "12345678",\r\n "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q"\r\n}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        expected = 'No items found for ra'

        response = lambda_handler(event, None)
        assert response["statusCode"] == 404
        assert json.loads(response["body"]) == expected

    
    def test_create_selfie_invalid_url(self):
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
                'body': '{\r\n    "ra": "21014442",\r\n "url": "http:/vitinhodohype.com.br"\r\n}',
                "pathParameters": None,
                "isBase64Encoded": None,
                "stageVariables": None
            }

            expected = 'Field url is not valid'

            response = lambda_handler(event, None)
            assert response["statusCode"] == 400
            assert json.loads(response["body"]) == expected

    def test_create_selfie_student_have_approved_selfie(self):
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
                'body': '{\r\n    "ra": "15013103",\r\n "url": "http:/vitinhodohype.com.br"\r\n}',
                "pathParameters": None,
                "isBase64Encoded": None,
                "stageVariables": None
            }

            expected = 'That action is forbidden for this Student'

            response = lambda_handler(event, None)
            assert response["statusCode"] == 403
            assert json.loads(response["body"]) == expected
   
    