from src.modules.validate_selfie.app.validate_selfie_presenter import lambda_handler
import pytest

from src.shared.environments import Environments


class Test_ValidadeSelfiePresenter:
    def test_validate_selfie_presenter(self):

        event = {
      "version":"0",
      "id":"c0b7e3c7-4721-3809-e769-65f6ab7d9c9a",
      "detail-type":"Object Created",
      "source":"aws.s3",
      "account":"XXXXXXXXXXXX",
      "time":"2022-11-20T15:35:38Z",
      "region":"us-east-2",
      "resources":[
         "arn:aws:s3:::selfiemssstudent-stack-selfierepositorystackselfi-1lw4vjo4qzdoj"
      ],
      "detail":{
         "version":"0",
         "bucket":{
            "name":"selfiemssstudent-stack-selfierepositorystackselfi-1lw4vjo4qzdoj"
         },
         "object":{
            "key":"foto.png",
            "size":353715,
            "etag":"4ce0ae3aadd8c651e8113d96285ce212",
            "version-id":"rADMHOdgPsTyfqZDjn0eAbiZV07OoG9j",
            "sequencer":"00637A494A5B9942AB"
         },
         "request-id":"XBV3TZ4A7GBAC5AB",
         "requester":"264055331071",
         "source-ip-address":"189.69.5.57",
         "reason":"PutObject"
      },
      "bucketMetadataResult":{
         "AcceptRanges":"bytes",
         "ContentLength":353715,
         "ContentType":"image/png",
         "ETag":"\"4ce0ae3aadd8c651e8113d96285ce212\"",
         "LastModified":"2022-11-20T15:35:39Z",
         "Metadata":{
            "name":"João Vitor Choueri Branco",
            "email":"eusousoller@gmail.com",
            "ra":"21010757"
         },
         "VersionId":"rADMHOdgPsTyfqZDjn0eAbiZV07OoG9j"
      },
      "rekognitionResult":{
            "Labels": [
                {
                    "Name": "Photography",
                    "Confidence": 100,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Portrait",
                    "Confidence": 100,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Face"
                        },
                        {
                            "Name": "Head"
                        },
                        {
                            "Name": "Person"
                        },
                        {
                            "Name": "Photography"
                        }
                    ]
                },
                {
                    "Name": "Head",
                    "Confidence": 100,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Face",
                    "Confidence": 100,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Head"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Person",
                    "Confidence": 100,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.9972279071807861,
                                "Height": 0.88490229845047,
                                "Left": 0.0026419830974191427,
                                "Top": 0.11343356966972351
                            },
                            "Confidence": 99.62065124511719
                        }
                    ],
                    "Parents": []
                },
                {
                    "Name": "Neck",
                    "Confidence": 99.97637939453125,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Body Part"
                        },
                        {
                            "Name": "Face"
                        },
                        {
                            "Name": "Head"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Body Part",
                    "Confidence": 99.97637939453125,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Woman",
                    "Confidence": 99.62065124511719,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.9972279071807861,
                                "Height": 0.88490229845047,
                                "Left": 0.0026419830974191427,
                                "Top": 0.11343356966972351
                            },
                            "Confidence": 99.62065124511719
                        }
                    ],
                    "Parents": [
                        {
                            "Name": "Adult"
                        },
                        {
                            "Name": "Female"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Adult",
                    "Confidence": 99.62065124511719,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.9972279071807861,
                                "Height": 0.88490229845047,
                                "Left": 0.0026419830974191427,
                                "Top": 0.11343356966972351
                            },
                            "Confidence": 99.62065124511719
                        }
                    ],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Female",
                    "Confidence": 99.62065124511719,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.9972279071807861,
                                "Height": 0.88490229845047,
                                "Left": 0.0026419830974191427,
                                "Top": 0.11343356966972351
                            },
                            "Confidence": 99.62065124511719
                        }
                    ],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Smile",
                    "Confidence": 99.51373291015625,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Face"
                        },
                        {
                            "Name": "Happy"
                        },
                        {
                            "Name": "Head"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Happy",
                    "Confidence": 99.51373291015625,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Face"
                        },
                        {
                            "Name": "Head"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Black Hair",
                    "Confidence": 56.7496223449707,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Hair"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Hair",
                    "Confidence": 56.7496223449707,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Selfie",
                    "Confidence": 55.5225830078125,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Face"
                        },
                        {
                            "Name": "Head"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                }
            ],
            "LabelModelVersion": "3.0"
        }
   }


        response = lambda_handler(event, None)
        cur_region = Environments.get_envs().region
        assert response['ra'] == "21010757"
        assert response['url']== f"https://selfiemssstudent-stack-selfierepositorystackselfi-1lw4vjo4qzdoj.s3.{cur_region}.amazonaws.com/foto.png"
        assert response["automaticReview"]["automaticallyRejected"] == False
        assert response["automaticReview"]["labels"][0]["confidence"] == 100.0
        assert response['message'] == "Selfie has been validated"

    def test_validate_selfie_presenter_invalid_ra(self):
        rekognitionResult = {
            "Labels": [
                {
                    "Name": "Photography",
                    "Confidence": 100,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Portrait",
                    "Confidence": 100,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Face"
                        },
                        {
                            "Name": "Head"
                        },
                        {
                            "Name": "Person"
                        },
                        {
                            "Name": "Photography"
                        }
                    ]
                },
                {
                    "Name": "Head",
                    "Confidence": 100,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Face",
                    "Confidence": 100,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Head"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Person",
                    "Confidence": 100,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.9972279071807861,
                                "Height": 0.88490229845047,
                                "Left": 0.0026419830974191427,
                                "Top": 0.11343356966972351
                            },
                            "Confidence": 99.62065124511719
                        }
                    ],
                    "Parents": []
                },
                {
                    "Name": "Neck",
                    "Confidence": 99.97637939453125,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Body Part"
                        },
                        {
                            "Name": "Face"
                        },
                        {
                            "Name": "Head"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Body Part",
                    "Confidence": 99.97637939453125,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Woman",
                    "Confidence": 99.62065124511719,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.9972279071807861,
                                "Height": 0.88490229845047,
                                "Left": 0.0026419830974191427,
                                "Top": 0.11343356966972351
                            },
                            "Confidence": 99.62065124511719
                        }
                    ],
                    "Parents": [
                        {
                            "Name": "Adult"
                        },
                        {
                            "Name": "Female"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Adult",
                    "Confidence": 99.62065124511719,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.9972279071807861,
                                "Height": 0.88490229845047,
                                "Left": 0.0026419830974191427,
                                "Top": 0.11343356966972351
                            },
                            "Confidence": 99.62065124511719
                        }
                    ],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Female",
                    "Confidence": 99.62065124511719,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.9972279071807861,
                                "Height": 0.88490229845047,
                                "Left": 0.0026419830974191427,
                                "Top": 0.11343356966972351
                            },
                            "Confidence": 99.62065124511719
                        }
                    ],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Smile",
                    "Confidence": 99.51373291015625,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Face"
                        },
                        {
                            "Name": "Happy"
                        },
                        {
                            "Name": "Head"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Happy",
                    "Confidence": 99.51373291015625,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Face"
                        },
                        {
                            "Name": "Head"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Black Hair",
                    "Confidence": 56.7496223449707,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Hair"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Hair",
                    "Confidence": 56.7496223449707,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Selfie",
                    "Confidence": 55.5225830078125,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Face"
                        },
                        {
                            "Name": "Head"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                }
            ],
            "LabelModelVersion": "3.0"
        }

        event = {
      "version":"0",
      "id":"c0b7e3c7-4721-3809-e769-65f6ab7d9c9a",
      "detail-type":"Object Created",
      "source":"aws.s3",
      "account":"XXXXXXXXXXXX",
      "time":"2022-11-20T15:35:38Z",
      "region":"us-east-2",
      "resources":[
         "arn:aws:s3:::selfiemssstudent-stack-selfierepositorystackselfi-1lw4vjo4qzdoj"
      ],
      "detail":{
         "version":"0",
         "bucket":{
            "name":"selfiemssstudent-stack-selfierepositorystackselfi-1lw4vjo4qzdoj"
         },
         "object":{
            "key":"foto.png",
            "size":353715,
            "etag":"4ce0ae3aadd8c651e8113d96285ce212",
            "version-id":"rADMHOdgPsTyfqZDjn0eAbiZV07OoG9j",
            "sequencer":"00637A494A5B9942AB"
         },
         "request-id":"XBV3TZ4A7GBAC5AB",
         "requester":"264055331071",
         "source-ip-address":"189.69.5.57",
         "reason":"PutObject"
      },
      "bucketMetadataResult":{
         "AcceptRanges":"bytes",
         "ContentLength":353715,
         "ContentType":"image/png",
         "ETag":"\"4ce0ae3aadd8c651e8113d96285ce212\"",
         "LastModified":"2022-11-20T15:35:39Z",
         "Metadata":{
            "name":"João Vitor Choueri Branco",
            "email":"eusousoller@gmail.com",
            "ra":"2100757"
         },
         "VersionId":"rADMHOdgPsTyfqZDjn0eAbiZV07OoG9j"
      },
        "rekognitionResult":rekognitionResult
    }

        response = lambda_handler(event, None)
        
        assert response == 'Field ra is not valid'
        
    def test_validate_selfie_presenter_missing_rekognition_result(self):
        event = {
      "version":"0",
      "id":"c0b7e3c7-4721-3809-e769-65f6ab7d9c9a",
      "detail-type":"Object Created",
      "source":"aws.s3",
      "account":"XXXXXXXXXXXX",
      "time":"2022-11-20T15:35:38Z",
      "region":"us-east-2",
      "resources":[
         "arn:aws:s3:::selfiemssstudent-stack-selfierepositorystackselfi-1lw4vjo4qzdoj"
      ],
      "detail":{
         "version":"0",
         "bucket":{
            "name":"selfiemssstudent-stack-selfierepositorystackselfi-1lw4vjo4qzdoj"
         },
         "object":{
            "key":"foto.png",
            "size":353715,
            "etag":"4ce0ae3aadd8c651e8113d96285ce212",
            "version-id":"rADMHOdgPsTyfqZDjn0eAbiZV07OoG9j",
            "sequencer":"00637A494A5B9942AB"
         },
         "request-id":"XBV3TZ4A7GBAC5AB",
         "requester":"264055331071",
         "source-ip-address":"189.69.5.57",
         "reason":"PutObject"
      },
      "bucketMetadataResult":{
         "AcceptRanges":"bytes",
         "ContentLength":353715,
         "ContentType":"image/png",
         "ETag":"\"4ce0ae3aadd8c651e8113d96285ce212\"",
         "LastModified":"2022-11-20T15:35:39Z",
         "Metadata":{
            "name":"João Vitor Choueri Branco",
            "email":"eusousoller@gmail.com",
            "ra":"21010757"
         },
         "VersionId":"rADMHOdgPsTyfqZDjn0eAbiZV07OoG9j"
      },

   }
        
        response = lambda_handler(event, None)
    
        assert response == "Field rekognitionResult is missing"
