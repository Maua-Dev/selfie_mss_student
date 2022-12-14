import json

from src.modules.get_all_selfies.app.get_all_selfies_presenter import lambda_handler


class Test_GetAllSelfiesPresenter:

    def test_get_all_selfies(self):

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
        assert json.loads(response['body'])['all_selfies'][0]['url'] == 'https://i.imgur.com/0KFBHTB.jpg'
        assert json.loads(response['body'])['all_selfies'][7]['student']['email'] == 'iamronald@mageofprogramming.com.br'
        assert json.loads(response['body'])['all_selfies'][7]['automaticReview']['rejectionReasons'] == ['NONE']
        assert json.loads(response['body'])['message'] == 'all selfies were retriven'
