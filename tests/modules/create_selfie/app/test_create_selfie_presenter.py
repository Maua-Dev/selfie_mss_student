import json

from src.modules.create_selfie.app.create_selfie_presenter import http_request_handler


class Test_CreateSelfiePresenter:

    def test_create_selfie(self):
        event = {
            "ra":"21014442",
            "url":"https://www.youtube.com/watch?v=5IpYOF4Hi6Q",
            "automaticReview":{
                "automaticallyRejected":"False",
                "rejectionReasons":[
                    "NONE"
                ],
                "labels":[
                    {
                        "name":"Glasses",
                        "coords":{
                        "Width":"0.6591288447380066",
                        "Height":"0.17444363236427307",
                        "Left":"0.19148917496204376",
                        "Top":"0.3813813030719757"
                        },
                        "confidence":"94.5357666015625",
                        "parents":[
                        "Accessories"
                        ]
                    },
                    {
                        "name":"Blalblas",
                        "coords":{
                        "Width":"0.6591288480066",
                        "Height":"0.1744236427307",
                        "Left":"0.19148916204376",
                        "Top":"0.3813813719757"
                        },
                        "confidence":"95.5366015625",
                        "parents":[
                        "ASODnoasdsa",
                        "nmdokasnkndkasnkd"
                        ]
                    }
                ]
            }
            }




        response = http_request_handler(event, None)
        assert response["statusCode"] == 201
        assert json.loads(response["body"])["message"] == "the selfie was created"
        assert json.loads(response["body"])["idSelfie"] == 1
        assert json.loads(response["body"])["rejectionReasons"] == ["NONE"]
        assert json.loads(response["body"])["rejectionDescription"] == None
        assert json.loads(response["body"])["state"] == "PENDING_REVIEW"
        assert json.loads(response["body"])["student"]["ra"] == "21014442"
        assert json.loads(response["body"])["automaticReview"]["automaticallyRejected"] == False

    def test_create_selfie_automaticallyRejected(self):
        event = {
            "ra":"21014442",
            "url":"https://www.youtube.com/watch?v=5IpYOF4Hi6Q",
            "automaticReview":{
                "automaticallyRejected":"True",
                "rejectionReasons":[
                    "COVERED_FACE"
                ],
                "labels":[
                    {
                        "name":"Glasses",
                        "coords":{
                        "Width":"0.6591288447380066",
                        "Height":"0.17444363236427307",
                        "Left":"0.19148917496204376",
                        "Top":"0.3813813030719757"
                        },
                        "confidence":"94.5357666015625",
                        "parents":[
                        "Accessories"
                        ]
                    },
                    {
                        "name":"Blalblas",
                        "coords":{
                        "Width":"0.6591288480066",
                        "Height":"0.1744236427307",
                        "Left":"0.19148916204376",
                        "Top":"0.3813813719757"
                        },
                        "confidence":"95.5366015625",
                        "parents":[
                        "ASODnoasdsa",
                        "nmdokasnkndkasnkd"
                        ]
                    }
                ]
            }
            }




        response = http_request_handler(event, None)
        assert response["statusCode"] == 201
        assert json.loads(response["body"])["message"] == "the selfie was created"
        assert json.loads(response["body"])["idSelfie"] == 1
        assert json.loads(response["body"])["rejectionReasons"] == ["COVERED_FACE"]
        assert json.loads(response["body"])["rejectionDescription"] == "auto-rejected by AI"
        assert json.loads(response["body"])["state"] == "DECLINED"
        assert json.loads(response["body"])["student"]["ra"] == "21014442"
        assert json.loads(response["body"])["automaticReview"]["automaticallyRejected"] == True


    def test_create_selfie_missing_ra(self):
        event = {"url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q"}
            

        expected = 'Field ra is missing'

        response = http_request_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == expected

    def test_create_selfie_ra_invalid_int(self):
        event = {
            "ra":21014442,
            "url":"https://www.youtube.com/watch?v=5IpYOF4Hi6Q",
            "automaticReview":{
                "automaticallyRejected":"False",
                "rejectionReasons":["NONE"],
                "labels":[
                    {
                        "name":"Glasses",
                        "coords":{
                        "Width":"0.6591288447380066",
                        "Height":"0.17444363236427307",
                        "Left":"0.19148917496204376",
                        "Top":"0.3813813030719757"
                        },
                        "confidence":"94.5357666015625",
                        "parents":[
                        "Accessories"
                        ]
                    },
                    {
                        "name":"Blalblas",
                        "coords":{
                        "Width":"0.6591288480066",
                        "Height":"0.1744236427307",
                        "Left":"0.19148916204376",
                        "Top":"0.3813813719757"
                        },
                        "confidence":"95.5366015625",
                        "parents":[
                        "ASODnoasdsa",
                        "nmdokasnkndkasnkd"
                        ]
                    }
                ]
            }
        }

        expected = 'ra must be a string'

        response = http_request_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == expected
        
    def test_create_selfie_not_found_ra(self):
        event = {
        "ra":"12345678",
        "url":"https://www.youtube.com/watch?v=5IpYOF4Hi6Q",
        "automaticReview":{
            "automaticallyRejected":"False",
            "rejectionReasons":["NONE"],
            "labels":[
                {
                    "name":"Glasses",
                    "coords":{
                    "Width":"0.6591288447380066",
                    "Height":"0.17444363236427307",
                    "Left":"0.19148917496204376",
                    "Top":"0.3813813030719757"
                    },
                    "confidence":"94.5357666015625",
                    "parents":[
                    "Accessories"
                    ]
                },
                {
                    "name":"Blalblas",
                    "coords":{
                    "Width":"0.6591288480066",
                    "Height":"0.1744236427307",
                    "Left":"0.19148916204376",
                    "Top":"0.3813813719757"
                    },
                    "confidence":"95.5366015625",
                    "parents":[
                    "ASODnoasdsa",
                    "nmdokasnkndkasnkd"
                    ]
                }
            ]
        }
        }

        expected = 'No items found for ra'

        response = http_request_handler(event, None)
        assert response["statusCode"] == 404
        assert json.loads(response["body"]) == expected

    
    def test_create_selfie_invalid_url(self):
            event = {'ra': '21014442', 'url': 'http://www.youtube.com/watch?v=5IpYOF4Hi6Q', 'automaticReview': {'automaticallyRejected': 'False', 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Glasses', 'coords': {'Width': '0.6591288447380066', 'Height': '0.17444363236427307', 'Left': '0.19148917496204376', 'Top': '0.3813813030719757'}, 'confidence': '94.5357666015625', 'parents': ['Accessories']}, {'name': 'Blalblas', 'coords': {'Width': '0.6591288480066', 'Height': '0.1744236427307', 'Left': '0.19148916204376', 'Top': '0.3813813719757'}, 'confidence': '95.5366015625', 'parents': ['ASODnoasdsa', 'nmdokasnkndkasnkd']}]}}

            expected = 'Field url is not valid'

            response = http_request_handler(event, None)
            assert response["statusCode"] == 400
            assert json.loads(response["body"]) == expected

    def test_create_selfie_student_have_approved_selfie(self):
            event = {'ra': '15013103', 'url': 'https://www.youtube.com/watch?v=5IpYOF4Hi6Q', 'automaticReview': {'automaticallyRejected': 'False', 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Glasses', 'coords': {'Width': '0.6591288447380066', 'Height': '0.17444363236427307', 'Left': '0.19148917496204376', 'Top': '0.3813813030719757'}, 'confidence': '94.5357666015625', 'parents': ['Accessories']}, {'name': 'Blalblas', 'coords': {'Width': '0.6591288480066', 'Height': '0.1744236427307', 'Left': '0.19148916204376', 'Top': '0.3813813719757'}, 'confidence': '95.5366015625', 'parents': ['ASODnoasdsa', 'nmdokasnkndkasnkd']}]}}
                

            expected = 'That action is forbidden for this Student'

            response = http_request_handler(event, None)
            assert response["statusCode"] == 403
            assert json.loads(response["body"]) == expected
   
    