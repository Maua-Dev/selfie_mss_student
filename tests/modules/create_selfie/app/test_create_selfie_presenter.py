import json

from src.modules.create_selfie.app.create_selfie_presenter import lambda_handler


class Test_CreateSelfiePresenter:

    def example_event(self, ra, automaticReview, url, message):
        return{
      "automaticReview": automaticReview,
      "ra": ra,
      "url": url,
      "message": message
  }

    def test_create_selfie(self):
        event = self.example_event(ra="21014442", url="https://www.youtube.com/watch?v=5IpYOF4Hi6Q", automaticReview={
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
            }, message="the selfie was created")

        response = lambda_handler(event, None)
        assert response["statusCode"] == 201
        assert json.loads(response["body"])["message"] == "the selfie was created"
        assert json.loads(response["body"])["idSelfie"] == 1
        assert json.loads(response["body"])["rejectionReasons"] == ["NONE"]
        assert json.loads(response["body"])["rejectionDescription"] == None
        assert json.loads(response["body"])["state"] == "PENDING_REVIEW"
        assert json.loads(response["body"])["student"]["ra"] == "21014442"
        assert json.loads(response["body"])["automaticReview"]["automaticallyRejected"] == False

    def test_create_selfie_automaticallyRejected(self):
        event = self.example_event(ra="21014442", url="https://www.youtube.com/watch?v=5IpYOF4Hi6Q", automaticReview={
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
            }, message="the selfie was created")




        response = lambda_handler(event, None)
        assert response["statusCode"] == 201
        assert json.loads(response["body"])["message"] == "the selfie was created"
        assert json.loads(response["body"])["idSelfie"] == 1
        assert json.loads(response["body"])["rejectionReasons"] == ["COVERED_FACE"]
        assert json.loads(response["body"])["rejectionDescription"] == "auto-rejected by AI"
        assert json.loads(response["body"])["state"] == "DECLINED"
        assert json.loads(response["body"])["student"]["ra"] == "21014442"
        assert json.loads(response["body"])["automaticReview"]["automaticallyRejected"] == True


    def test_create_selfie_missing_ra(self):
        event = self.example_event(ra=None, url="https://www.youtube.com/watch?v=5IpYOF4Hi6Q", automaticReview={}, message="Field ra is missing")

        expected = 'Field ra is missing'

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == expected

    def test_create_selfie_ra_invalid_int(self):
        event = self.example_event(ra=123, url="https://www.youtube.com/watch?v=5IpYOF4Hi6Q", automaticReview={
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
            }, message="ra must be a string")

        expected = 'ra must be a string'

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == expected
        
    def test_create_selfie_not_found_ra(self):
        event = self.example_event(ra="12345678", url="https://www.youtube.com/watch?v=5IpYOF4Hi6Q", automaticReview={
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
        }, message="No items found for ra")

        expected = 'No items found for ra'

        response = lambda_handler(event, None)
        assert response["statusCode"] == 404
        assert json.loads(response["body"]) == expected

    
    def test_create_selfie_invalid_url(self):
        event = self.example_event(ra="21014442", url="http://www.youtube.com/watch?v=5IpYOF4Hi6Q", automaticReview={'automaticallyRejected': 'False', 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Glasses', 'coords': {'Width': '0.6591288447380066', 'Height': '0.17444363236427307', 'Left': '0.19148917496204376', 'Top': '0.3813813030719757'}, 'confidence': '94.5357666015625', 'parents': ['Accessories']}, {'name': 'Blalblas', 'coords': {'Width': '0.6591288480066', 'Height': '0.1744236427307', 'Left': '0.19148916204376', 'Top': '0.3813813719757'}, 'confidence': '95.5366015625', 'parents': ['ASODnoasdsa', 'nmdokasnkndkasnkd']}]}, message="Invalid url")

        expected = 'Field url is not valid'

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == expected

    def test_create_selfie_student_have_approved_selfie(self):
        event = self.example_event(ra="15013103", url="https://www.youtube.com/watch?v=5IpYOF4Hi6Q", automaticReview={'automaticallyRejected': 'False', 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Glasses', 'coords': {'Width': '0.6591288447380066', 'Height': '0.17444363236427307', 'Left': '0.19148917496204376', 'Top': '0.3813813030719757'}, 'confidence': '94.5357666015625', 'parents': ['Accessories']}, {'name': 'Blalblas', 'coords': {'Width': '0.6591288480066', 'Height': '0.1744236427307', 'Left': '0.19148916204376', 'Top': '0.3813813719757'}, 'confidence': '95.5366015625', 'parents': ['ASODnoasdsa', 'nmdokasnkndkasnkd']}]} , message="That action is forbidden for this Student")


        expected = 'That action is forbidden for this Student'

        response = lambda_handler(event, None)
        assert response["statusCode"] == 403
        assert json.loads(response["body"]) == expected

    def test_random(self):
        event = {'automaticReview': {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Tie', 'coords': {'Height': 0.37231645, 'Left': 0.3910927, 'Top': 0.6276425, 'Width': 0.16625582}, 'confidence': 99.999825, 'parents': ['Accessories', 'Formal Wear']}, {'name': 'Formal Wear', 'coords': {}, 'confidence': 99.999825, 'parents': []}, {'name': 'Accessories', 'coords': {}, 'confidence': 99.999825, 'parents': []}, {'name': 'Jacket', 'coords': {}, 'confidence': 99.999, 'parents': ['Clothing', 'Coat']}, {'name': 'Coat', 'coords': {}, 'confidence': 99.999, 'parents': ['Clothing']}, {'name': 'Clothing', 'coords': {}, 'confidence': 99.999, 'parents': []}, {'name': 'Blazer', 'coords': {}, 'confidence': 99.99808, 'parents': ['Clothing', 'Coat', 'Jacket']}, {'name': 'Suit', 'coords': {}, 'confidence': 99.99604, 'parents': ['Clothing', 'Formal Wear']}, {'name': 'Portrait', 'coords': {}, 'confidence': 99.992744, 'parents': ['Face', 'Head', 'Person', 'Photography']}, {'name': 'Photography', 'coords': {}, 'confidence': 99.992744, 'parents': []}, {'name': 'Head', 'coords': {}, 'confidence': 99.992744, 'parents': ['Person']}, {'name': 'Face', 'coords': {}, 'confidence': 99.992744, 'parents': ['Head', 'Person']}, {'name': 'Person', 'coords': {'Height': 0.86876976, 'Left': 0.0004339218, 'Top': 0.13055886, 'Width': 0.9951039}, 'confidence': 98.94463, 'parents': []}, {'name': 'Person', 'coords': {'Height': 0.15293843, 'Left': 0.61985844, 'Top': 0.42348433, 'Width': 0.10980775}, 'confidence': 90.77731, 'parents': []}, {'name': 'Shirt', 'coords': {}, 'confidence': 99.12194, 'parents': ['Clothing']}, {'name': 'Man', 'coords': {'Height': 0.86876976, 'Left': 0.0004339218, 'Top': 0.13055886, 'Width': 0.9951039}, 'confidence': 98.94463, 'parents': ['Adult', 'Male', 'Person']}, {'name': 'Man', 'coords': {'Height': 0.15293843, 'Left': 0.61985844, 'Top': 0.42348433, 'Width': 0.10980775}, 'confidence': 90.77731, 'parents': ['Adult', 'Male', 'Person']}, {'name': 'Adult', 'coords': {'Height': 0.86876976, 'Left': 0.0004339218, 'Top': 0.13055886, 'Width': 0.9951039}, 'confidence': 98.94463, 'parents': ['Person']}, {'name': 'Adult', 'coords': {'Height': 0.15293843, 'Left': 0.61985844, 'Top': 0.42348433, 'Width': 0.10980775}, 'confidence': 90.77731, 'parents': ['Person']}, {'name': 'Male', 'coords': {'Height': 0.86876976, 'Left': 0.0004339218, 'Top': 0.13055886, 'Width': 0.9951039}, 'confidence': 98.94463, 'parents': ['Person']}, {'name': 'Male', 'coords': {'Height': 0.15293843, 'Left': 0.61985844, 'Top': 0.42348433, 'Width': 0.10980775}, 'confidence': 90.77731, 'parents': ['Person']}]}, 'ra': '21002088', 'url': 'https://selfiemssstudent-stack-selfierepositorystackselfi-lezfi9mqiw4j.s3.us-east-2.amazonaws.com/foto.png', 'message': 'Selfie has been validated'}

        response = lambda_handler(event, None)

        assert response["statusCode"] == 201