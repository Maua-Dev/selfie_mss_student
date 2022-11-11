import pytest
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.validate_selfie.app.validate_selfie_controller import ValidateSelfieController
from src.modules.validate_selfie.app.validate_selfie_usecase import ValidateSelfieUsecase
from src.shared.helpers.http.http_models import HttpRequest


 
class Test_ValidateSelfieController:
    def test_validate_selfie_controller(self):
        repo = StudentRepositoryMock()
        usecase = ValidateSelfieUsecase(repo=repo)
        controller = ValidateSelfieController(usecase=usecase)
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

        request = HttpRequest(body={
            "ra": "21014443",
            "rekognitionResult": rekognitionResult,
            "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q"
        })
        response = controller(request=request)


        assert response.status_code == 200
        assert response.body['ra'] == "21014443"
        assert response.body['url']== "https://www.youtube.com/watch?v=5IpYOF4Hi6Q"
        assert response.body["automaticallyRejected"] == False
        assert response.body["labels"][0]["confidence"] == 100.0
        assert response.body['message'] == "Selfie has been validated"
        
    def test_validate_selfie_controller_invalid_ra(self):
        repo = StudentRepositoryMock()
        usecase = ValidateSelfieUsecase(repo=repo)
        controller = ValidateSelfieController(usecase=usecase)
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

        request = HttpRequest(body={
            "ra": "21.01444-3",
            "rekognitionResult": rekognitionResult,
            "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q"
        })
        response = controller(request=request)


        assert response.status_code == 400
        assert response.body == 'Field ra is not valid'
        
    def test_validate_selfie_controller_invalid_url(self):
        repo = StudentRepositoryMock()
        usecase = ValidateSelfieUsecase(repo=repo)
        controller = ValidateSelfieController(usecase=usecase)
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

        request = HttpRequest(body={
            "ra": "21014443",
            "rekognitionResult": rekognitionResult,
            "url": "http://www.youtube.com/watch?v=5IpYOF4Hi6Q"
        })
        response = controller(request=request)


        assert response.status_code == 400
        assert response.body == 'Field url is not valid'
        
    def test_validate_selfie_controller_invalid_rekognition_result(self):
        repo = StudentRepositoryMock()
        usecase = ValidateSelfieUsecase(repo=repo)
        controller = ValidateSelfieController(usecase=usecase)
        
        request = HttpRequest(body={
            "ra": "21014443",
            "rekognitionResult": None,
            "url": "https://www.youtube.com/watch?v=5IpYOF4Hi6Q"
        })
        response = controller(request=request)


        assert response.status_code == 400
        assert response.body == 'Field rekognitionResult is not valid'