import json
from src.modules.get_approved_reviews_by_reviewer.app.get_approved_reviews_by_reviewer_presenter import lambda_handler

class Test_GetApprovedSelfiesByReviewerPresenter:

    def test_get_approved_selfies_by_reviewer_presenter(self):
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
            "reviewerRa":"03026",
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
        
        expected ={
   "reviewer":{
      "ra":"03026",
      "name":"Mauro Crapino",
      "email":"mauro@maua.br",
      "active":True
   },
   "approvedSelfies":[
      {
         "idReview":0,
         "state":"APPROVED",
         "selfie":{
            "idSelfie":1,
            "dateCreated":"2022-10-12T16:01:59.149927",
            "url":"https://i.imgur.com/b9qFYmb.jpg",
            "state":"APPROVED",
            "rejectionReasons":[
               "NONE"
            ],
            "rejectionDescription":"",
            "automaticReview":{
               "automaticallyRejected":False,
               "rejectionReasons":[
                  "NONE"
               ],
               "labels":[
                  {
                     "name":"Person",
                     "coords":{
                        "Width":0.9711952805519104,
                        "Height":0.8659809827804565,
                        "Left":0.012313545681536198,
                        "Top":0.11108686774969101
                     },
                     "confidence":98.54370880126953,
                     "parents":[
                        
                     ]
                  },
                  {
                     "name":"Face",
                     "coords":{
                        "Width":0.9711952805519104,
                        "Height":0.8659809827804565,
                        "Left":0.012313545681536198,
                        "Top":0.11108686774969101
                     },
                     "confidence":98.54370880126953,
                     "parents":[
                        
                     ]
                  }
               ]
            },
            "student":{
               "ra":"21010757",
               "name":"João Vitor Choueri Branco",
               "email":"21.01075-7@gmail.com"
            }
         },
         "dateAssigned":"2022-12-01T16:01:59.149927",
         "dateReviewed":"2022-12-02T16:05:59.149927"
      },
      {
         "idReview":0,
         "state":"APPROVED",
         "selfie":{
            "idSelfie":0,
            "dateCreated":"2022-10-12T16:01:59.149927",
            "url":"https://i.imgur.com/6a7qqRg.jpg",
            "state":"APPROVED",
            "rejectionReasons":[
               "NONE"
            ],
            "rejectionDescription":"",
            "automaticReview":{
               "automaticallyRejected":False,
               "rejectionReasons":[
                  "NONE"
               ],
               "labels":[
                  {
                     "name":"Person",
                     "coords":{
                        "Width":0.9711952805519104,
                        "Height":0.8659809827804565,
                        "Left":0.012313545681536198,
                        "Top":0.11108686774969101
                     },
                     "confidence":98.54370880126953,
                     "parents":[
                        
                     ]
                  },
                  {
                     "name":"Face",
                     "coords":{
                        
                     },
                     "confidence":98.54370880126953,
                     "parents":[
                        
                     ]
                  }
               ]
            },
            "student":{
               "ra":"22011020",
               "name":"Guirão",
               "email":"acreditaquesousollertambem@yahoo.com"
            }
         },
         "dateAssigned":"2022-11-30T16:01:59.149927",
         "dateReviewed":"2022-12-02T16:05:59.149927"
      }
   ],
   "message":"the approved sefies by reviewer were retriven"
}
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 200
        assert json.loads(response["body"]) == expected

  
    def test_get_approved_selfies_by_reviewer_presenter_empty_list(self):
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
          "approvedSelfies":[],
          "message":"the approved sefies by reviewer were retriven"
        }
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 200
        assert json.loads(response["body"]) == expected

  
    def test_get_approved_selfies_by_reviewer_presenter_no_items_found(self):
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

    def test_get_approved_selfies_by_reviewer_presenter_no_valid(self):
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
