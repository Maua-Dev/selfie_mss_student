from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.validate_selfie.app.validate_selfie_usecase import ValidateSelfieUsecase


class Test_ValidateSelfieUsecase:
    def test_validate_selfie_usecase(self):
        repo = StudentRepositoryMock()
        usecase = ValidateSelfieUsecase(repo=repo)
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

        automaticRekognition = usecase(rekognitionResult=rekognitionResult)
        assert automaticRekognition.automaticallyRejected == False
        assert automaticRekognition.labels[-1].name == "Happy" 
        assert automaticRekognition.labels[0].parents == [] 
        assert automaticRekognition.labels[0].coords == {} 
        
        
    def test_validate_selfie_usecase_auto_rejected_1(self):
        repo = StudentRepositoryMock()
        usecase = ValidateSelfieUsecase(repo=repo)
        rekognitionResult = {
            "Labels": [
                {
                    "Name": "Cap",
                    "Confidence": 99.99784088134766,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Clothing"
                        },
                        {
                            "Name": "Hat"
                        }
                    ]
                },
                {
                    "Name": "Hat",
                    "Confidence": 99.99784088134766,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Clothing"
                        }
                    ]
                },
                {
                    "Name": "Clothing",
                    "Confidence": 99.99784088134766,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Portrait",
                    "Confidence": 99.93478393554688,
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
                    "Name": "Photography",
                    "Confidence": 99.93478393554688,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Person",
                    "Confidence": 99.93478393554688,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.6901699304580688,
                                "Height": 0.8336241245269775,
                                "Left": 0.008156394585967064,
                                "Top": 0.16374839842319489
                            },
                            "Confidence": 96.26411437988281
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.16842180490493774,
                                "Height": 0.1986818015575409,
                                "Left": 0.6872493624687195,
                                "Top": 0.4688829779624939
                            },
                            "Confidence": 93.93721008300781
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.07226812839508057,
                                "Height": 0.12989842891693115,
                                "Left": 0.0796172097325325,
                                "Top": 0.5177081227302551
                            },
                            "Confidence": 92.71702575683594
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.040458910167217255,
                                "Height": 0.03787947818636894,
                                "Left": 0.3206922709941864,
                                "Top": 0.43125995993614197
                            },
                            "Confidence": 73.47802734375
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.06557127833366394,
                                "Height": 0.065212182700634,
                                "Left": 0.20524637401103973,
                                "Top": 0.4425712823867798
                            },
                            "Confidence": 66.32945251464844
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.05885731056332588,
                                "Height": 0.0889701172709465,
                                "Left": 0.1525610089302063,
                                "Top": 0.4537288546562195
                            },
                            "Confidence": 61.89244842529297
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.06854302436113358,
                                "Height": 0.27467817068099976,
                                "Left": 0.0000998234681901522,
                                "Top": 0.5196669101715088
                            },
                            "Confidence": 61.405670166015625
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.09334466606378555,
                                "Height": 0.15933287143707275,
                                "Left": 0.056017324328422546,
                                "Top": 0.46881210803985596
                            },
                            "Confidence": 60.94859313964844
                        }
                    ],
                    "Parents": []
                },
                {
                    "Name": "Head",
                    "Confidence": 99.93478393554688,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Face",
                    "Confidence": 99.93478393554688,
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
                    "Name": "Coat",
                    "Confidence": 99.61935424804688,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Clothing"
                        }
                    ]
                },
                {
                    "Name": "Man",
                    "Confidence": 96.26411437988281,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.6901699304580688,
                                "Height": 0.8336241245269775,
                                "Left": 0.008156394585967064,
                                "Top": 0.16374839842319489
                            },
                            "Confidence": 96.26411437988281
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.16842180490493774,
                                "Height": 0.1986818015575409,
                                "Left": 0.6872493624687195,
                                "Top": 0.4688829779624939
                            },
                            "Confidence": 87.93721008300781
                        }
                    ],
                    "Parents": [
                        {
                            "Name": "Adult"
                        },
                        {
                            "Name": "Male"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Adult",
                    "Confidence": 96.26411437988281,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.6901699304580688,
                                "Height": 0.8336241245269775,
                                "Left": 0.008156394585967064,
                                "Top": 0.16374839842319489
                            },
                            "Confidence": 96.26411437988281
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.16842180490493774,
                                "Height": 0.1986818015575409,
                                "Left": 0.6872493624687195,
                                "Top": 0.4688829779624939
                            },
                            "Confidence": 87.93721008300781
                        }
                    ],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Male",
                    "Confidence": 96.26411437988281,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.6901699304580688,
                                "Height": 0.8336241245269775,
                                "Left": 0.008156394585967064,
                                "Top": 0.16374839842319489
                            },
                            "Confidence": 96.26411437988281
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.16842180490493774,
                                "Height": 0.1986818015575409,
                                "Left": 0.6872493624687195,
                                "Top": 0.4688829779624939
                            },
                            "Confidence": 87.93721008300781
                        }
                    ],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Arena",
                    "Confidence": 79.83932495117188,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Architecture"
                        },
                        {
                            "Name": "Building"
                        }
                    ]
                },
                {
                    "Name": "Building",
                    "Confidence": 79.83932495117188,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Architecture"
                        }
                    ]
                },
                {
                    "Name": "Architecture",
                    "Confidence": 79.83932495117188,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Jacket",
                    "Confidence": 75.57364654541016,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Clothing"
                        },
                        {
                            "Name": "Coat"
                        }
                    ]
                },
                {
                    "Name": "Selfie",
                    "Confidence": 72.04155731201172,
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
                    "Name": "Fortress",
                    "Confidence": 61.40546798706055,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Architecture"
                        },
                        {
                            "Name": "Building"
                        },
                        {
                            "Name": "Castle"
                        }
                    ]
                },
                {
                    "Name": "Castle",
                    "Confidence": 61.40546798706055,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Architecture"
                        },
                        {
                            "Name": "Building"
                        }
                    ]
                },
                {
                    "Name": "Backpack",
                    "Confidence": 58.60300827026367,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.11376999318599701,
                                "Height": 0.12154988944530487,
                                "Left": 0.7035405039787292,
                                "Top": 0.5414784550666809
                            },
                            "Confidence": 58.60300827026367
                        }
                    ],
                    "Parents": [
                        {
                            "Name": "Bag"
                        }
                    ]
                },
                {
                    "Name": "Bag",
                    "Confidence": 58.60300827026367,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Smile",
                    "Confidence": 57.86575698852539,
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
                    "Confidence": 57.86575698852539,
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
                    "Name": "People",
                    "Confidence": 57.819393157958984,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Teeth",
                    "Confidence": 57.401981353759766,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Body Part"
                        },
                        {
                            "Name": "Mouth"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Mouth",
                    "Confidence": 57.401981353759766,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Body Part"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Body Part",
                    "Confidence": 57.401981353759766,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Rock",
                    "Confidence": 57.15266036987305,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Baseball Cap",
                    "Confidence": 56.797725677490234,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Cap"
                        },
                        {
                            "Name": "Clothing"
                        },
                        {
                            "Name": "Hat"
                        }
                    ]
                },
                {
                    "Name": "Amphitheatre",
                    "Confidence": 56.33184051513672,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Architecture"
                        },
                        {
                            "Name": "Arena"
                        },
                        {
                            "Name": "Building"
                        }
                    ]
                },
                {
                    "Name": "Glasses",
                    "Confidence": 55.7895393371582,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.19773507118225098,
                                "Height": 0.059735007584095,
                                "Left": 0.440632164478302,
                                "Top": 0.32708939909935
                            },
                            "Confidence": 55.15669631958008
                        }
                    ],
                    "Parents": [
                        {
                            "Name": "Accessories"
                        }
                    ]
                },
                {
                    "Name": "Accessories",
                    "Confidence": 55.7895393371582,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Tourist",
                    "Confidence": 55.636043548583984,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Fun"
                        },
                        {
                            "Name": "Person"
                        },
                        {
                            "Name": "Vacation"
                        }
                    ]
                },
                {
                    "Name": "Vacation",
                    "Confidence": 55.636043548583984,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Fun"
                        }
                    ]
                },
                {
                    "Name": "Fun",
                    "Confidence": 55.636043548583984,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Crowd",
                    "Confidence": 55.22445297241211,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Street",
                    "Confidence": 55.067928314208984,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "City"
                        },
                        {
                            "Name": "Road"
                        },
                        {
                            "Name": "Urban"
                        }
                    ]
                },
                {
                    "Name": "Urban",
                    "Confidence": 55.067928314208984,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Road",
                    "Confidence": 55.067928314208984,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "City",
                    "Confidence": 55.067928314208984,
                    "Instances": [],
                    "Parents": []
                }
            ],
            "LabelModelVersion": "3.0"
          }

        automaticRekognition = usecase(rekognitionResult=rekognitionResult)
        assert automaticRekognition.automaticallyRejected == True
        assert automaticRekognition.labels[-1].name == "Male" 

        
    def test_validate_selfie_usecase_auto_rejected_2(self):
        repo = StudentRepositoryMock()
        usecase = ValidateSelfieUsecase(repo=repo)
        rekognitionResult = {
            "Labels": [
                {
                    "Name": "Cap",
                    "Confidence": 99.99784088134766,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Clothing"
                        },
                        {
                            "Name": "Hat"
                        }
                    ]
                },
                {
                    "Name": "Hat",
                    "Confidence": 99.99784088134766,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Clothing"
                        }
                    ]
                },
                {
                    "Name": "Clothing",
                    "Confidence": 99.99784088134766,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Portrait",
                    "Confidence": 99.93478393554688,
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
                    "Name": "Photography",
                    "Confidence": 99.93478393554688,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Person",
                    "Confidence": 99.93478393554688,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.6901699304580688,
                                "Height": 0.8336241245269775,
                                "Left": 0.008156394585967064,
                                "Top": 0.16374839842319489
                            },
                            "Confidence": 96.26411437988281
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.16842180490493774,
                                "Height": 0.1986818015575409,
                                "Left": 0.6872493624687195,
                                "Top": 0.4688829779624939
                            },
                            "Confidence": 93.93721008300781
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.07226812839508057,
                                "Height": 0.12989842891693115,
                                "Left": 0.0796172097325325,
                                "Top": 0.5177081227302551
                            },
                            "Confidence": 92.71702575683594
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.040458910167217255,
                                "Height": 0.03787947818636894,
                                "Left": 0.3206922709941864,
                                "Top": 0.43125995993614197
                            },
                            "Confidence": 73.47802734375
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.06557127833366394,
                                "Height": 0.065212182700634,
                                "Left": 0.20524637401103973,
                                "Top": 0.4425712823867798
                            },
                            "Confidence": 66.32945251464844
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.05885731056332588,
                                "Height": 0.0889701172709465,
                                "Left": 0.1525610089302063,
                                "Top": 0.4537288546562195
                            },
                            "Confidence": 61.89244842529297
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.06854302436113358,
                                "Height": 0.27467817068099976,
                                "Left": 0.0000998234681901522,
                                "Top": 0.5196669101715088
                            },
                            "Confidence": 61.405670166015625
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.09334466606378555,
                                "Height": 0.15933287143707275,
                                "Left": 0.056017324328422546,
                                "Top": 0.46881210803985596
                            },
                            "Confidence": 60.94859313964844
                        }
                    ],
                    "Parents": []
                },
                {
                    "Name": "Head",
                    "Confidence": 99.93478393554688,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Face",
                    "Confidence": 99.93478393554688,
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
                    "Name": "Coat",
                    "Confidence": 99.61935424804688,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Clothing"
                        }
                    ]
                },
                {
                    "Name": "Man",
                    "Confidence": 96.26411437988281,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.6901699304580688,
                                "Height": 0.8336241245269775,
                                "Left": 0.008156394585967064,
                                "Top": 0.16374839842319489
                            },
                            "Confidence": 96.26411437988281
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.16842180490493774,
                                "Height": 0.1986818015575409,
                                "Left": 0.6872493624687195,
                                "Top": 0.4688829779624939
                            },
                            "Confidence": 87.93721008300781
                        }
                    ],
                    "Parents": [
                        {
                            "Name": "Adult"
                        },
                        {
                            "Name": "Male"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Adult",
                    "Confidence": 96.26411437988281,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.6901699304580688,
                                "Height": 0.8336241245269775,
                                "Left": 0.008156394585967064,
                                "Top": 0.16374839842319489
                            },
                            "Confidence": 96.26411437988281
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.16842180490493774,
                                "Height": 0.1986818015575409,
                                "Left": 0.6872493624687195,
                                "Top": 0.4688829779624939
                            },
                            "Confidence": 87.93721008300781
                        }
                    ],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Male",
                    "Confidence": 96.26411437988281,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.6901699304580688,
                                "Height": 0.8336241245269775,
                                "Left": 0.008156394585967064,
                                "Top": 0.16374839842319489
                            },
                            "Confidence": 96.26411437988281
                        },
                        {
                            "BoundingBox": {
                                "Width": 0.16842180490493774,
                                "Height": 0.1986818015575409,
                                "Left": 0.6872493624687195,
                                "Top": 0.4688829779624939
                            },
                            "Confidence": 87.93721008300781
                        }
                    ],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Arena",
                    "Confidence": 79.83932495117188,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Architecture"
                        },
                        {
                            "Name": "Building"
                        }
                    ]
                },
                {
                    "Name": "Building",
                    "Confidence": 79.83932495117188,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Architecture"
                        }
                    ]
                },
                {
                    "Name": "Architecture",
                    "Confidence": 79.83932495117188,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Jacket",
                    "Confidence": 75.57364654541016,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Clothing"
                        },
                        {
                            "Name": "Coat"
                        }
                    ]
                },
                {
                    "Name": "Selfie",
                    "Confidence": 72.04155731201172,
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
                    "Name": "Fortress",
                    "Confidence": 61.40546798706055,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Architecture"
                        },
                        {
                            "Name": "Building"
                        },
                        {
                            "Name": "Castle"
                        }
                    ]
                },
                {
                    "Name": "Castle",
                    "Confidence": 61.40546798706055,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Architecture"
                        },
                        {
                            "Name": "Building"
                        }
                    ]
                },
                {
                    "Name": "Backpack",
                    "Confidence": 58.60300827026367,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.11376999318599701,
                                "Height": 0.12154988944530487,
                                "Left": 0.7035405039787292,
                                "Top": 0.5414784550666809
                            },
                            "Confidence": 58.60300827026367
                        }
                    ],
                    "Parents": [
                        {
                            "Name": "Bag"
                        }
                    ]
                },
                {
                    "Name": "Bag",
                    "Confidence": 58.60300827026367,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Smile",
                    "Confidence": 57.86575698852539,
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
                    "Confidence": 57.86575698852539,
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
                    "Name": "People",
                    "Confidence": 57.819393157958984,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Teeth",
                    "Confidence": 57.401981353759766,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Body Part"
                        },
                        {
                            "Name": "Mouth"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Mouth",
                    "Confidence": 57.401981353759766,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Body Part"
                        },
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Body Part",
                    "Confidence": 57.401981353759766,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Rock",
                    "Confidence": 57.15266036987305,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Baseball Cap",
                    "Confidence": 56.797725677490234,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Cap"
                        },
                        {
                            "Name": "Clothing"
                        },
                        {
                            "Name": "Hat"
                        }
                    ]
                },
                {
                    "Name": "Amphitheatre",
                    "Confidence": 56.33184051513672,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Architecture"
                        },
                        {
                            "Name": "Arena"
                        },
                        {
                            "Name": "Building"
                        }
                    ]
                },
                {
                    "Name": "Glasses",
                    "Confidence": 55.7895393371582,
                    "Instances": [
                        {
                            "BoundingBox": {
                                "Width": 0.19773507118225098,
                                "Height": 0.059735007584095,
                                "Left": 0.440632164478302,
                                "Top": 0.32708939909935
                            },
                            "Confidence": 55.15669631958008
                        }
                    ],
                    "Parents": [
                        {
                            "Name": "Accessories"
                        }
                    ]
                },
                {
                    "Name": "Accessories",
                    "Confidence": 55.7895393371582,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Tourist",
                    "Confidence": 55.636043548583984,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Fun"
                        },
                        {
                            "Name": "Person"
                        },
                        {
                            "Name": "Vacation"
                        }
                    ]
                },
                {
                    "Name": "Vacation",
                    "Confidence": 55.636043548583984,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Fun"
                        }
                    ]
                },
                {
                    "Name": "Fun",
                    "Confidence": 55.636043548583984,
                    "Instances": [],
                    "Parents": []
                },
                {
                    "Name": "Crowd",
                    "Confidence": 55.22445297241211,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "Person"
                        }
                    ]
                },
                {
                    "Name": "Street",
                    "Confidence": 55.067928314208984,
                    "Instances": [],
                    "Parents": [
                        {
                            "Name": "City"
                        },
                        {
                            "Name": "Road"
                        },
                        {
                            "Name": "Urban"
                        }
                    ]
                }
            ],
            "LabelModelVersion": "3.0"
          }

        automaticRekognition = usecase(rekognitionResult=rekognitionResult)
        assert automaticRekognition.automaticallyRejected == True
        assert automaticRekognition.labels[-1].name == "Male" 
        assert automaticRekognition.labels[-1].coords["Width"] == 0.6901699304580688
        
        
    def test_validate_selfie_usecase_auto_rejected_3(self):
        repo = StudentRepositoryMock()
        usecase = ValidateSelfieUsecase(repo=repo)
        rekognitionResult = {
    "Labels": [
        {
            "Name": "Strap",
            "Confidence": 99.99072265625,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Accessories"
                }
            ]
        },
        {
            "Name": "Accessories",
            "Confidence": 99.99072265625,
            "Instances": [],
            "Parents": []
        },
        {
            "Name": "Dog",
            "Confidence": 98.91767883300781,
            "Instances": [
                {
                    "BoundingBox": {
                        "Width": 0.4189898669719696,
                        "Height": 0.5533494353294373,
                        "Left": 0.29500433802604675,
                        "Top": 0.1943594515323639
                    },
                    "Confidence": 98.91767883300781
                }
            ],
            "Parents": [
                {
                    "Name": "Animal"
                },
                {
                    "Name": "Canine"
                },
                {
                    "Name": "Mammal"
                },
                {
                    "Name": "Pet"
                }
            ]
        },
        {
            "Name": "Canine",
            "Confidence": 98.91767883300781,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Animal"
                },
                {
                    "Name": "Mammal"
                }
            ]
        },
        {
            "Name": "Pet",
            "Confidence": 98.91767883300781,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Animal"
                }
            ]
        },
        {
            "Name": "Mammal",
            "Confidence": 98.91767883300781,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Animal"
                }
            ]
        },
        {
            "Name": "Animal",
            "Confidence": 98.91767883300781,
            "Instances": [
                {
                    "BoundingBox": {
                        "Width": 0.4189898669719696,
                        "Height": 0.5533494353294373,
                        "Left": 0.29500433802604675,
                        "Top": 0.1943594515323639
                    },
                    "Confidence": 98.91767883300781
                },{
                    "BoundingBox": {
                        "Width": 0.4189898669719696,
                        "Height": 0.5533494353294373,
                        "Left": 0.29500433802604675,
                        "Top": 0.1943594515323639
                    },
                    "Confidence": 98.90
                }],
            "Parents": []
        },
        {
            "Name": "Leash",
            "Confidence": 61.22441864013672,
            "Instances": [],
            "Parents": []
        },
        {
            "Name": "Puppy",
            "Confidence": 57.59462356567383,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Animal"
                },
                {
                    "Name": "Canine"
                },
                {
                    "Name": "Dog"
                },
                {
                    "Name": "Mammal"
                },
                {
                    "Name": "Pet"
                }
            ]
        },
        {
            "Name": "Vest",
            "Confidence": 57.53041458129883,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Clothing"
                }
            ]
        },
        {
            "Name": "Clothing",
            "Confidence": 57.53041458129883,
            "Instances": [],
            "Parents": []
        },
        {
            "Name": "Affenpinscher",
            "Confidence": 57.20996856689453,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Animal"
                },
                {
                    "Name": "Canine"
                },
                {
                    "Name": "Dog"
                },
                {
                    "Name": "Mammal"
                },
                {
                    "Name": "Pet"
                }
            ]
        },
        {
            "Name": "Terrier",
            "Confidence": 56.393096923828125,
            "Instances": [],
            "Parents": [
                {
                    "Name": "Animal"
                },
                {
                    "Name": "Canine"
                },
                {
                    "Name": "Dog"
                },
                {
                    "Name": "Mammal"
                },
                {
                    "Name": "Pet"
                }
            ]
        }
    ],
    "LabelModelVersion": "3.0"
}
        automaticRekognition = usecase(rekognitionResult=rekognitionResult)
        


        assert automaticRekognition.labels[-1].name == "Animal" 
        assert automaticRekognition.labels[-1].confidence == 98.90
        assert automaticRekognition.automaticallyRejected == True

    def test_validate_selfie_usecase_auto_rejected_4(self):
        repo = StudentRepositoryMock()
        usecase = ValidateSelfieUsecase(repo=repo)
        rekognitionResult = {
        "Labels": [
            {
                "Name": "Hair",
                "Confidence": 99.82501220703125,
                "Instances": [],
                "Parents": [
                    {
                        "Name": "Person"
                    }
                ]
            },
            {
                "Name": "Person",
                "Confidence": 99.82501220703125,
                "Instances": [
                    {
                        "BoundingBox": {
                            "Width": 0.9560412168502808,
                            "Height": 0.9275450706481934,
                            "Left": 0.03678623214364052,
                            "Top": 0.07245491445064545
                        },
                        "Confidence": 89.74848937988281
                    }
                ],
                "Parents": []
            },
            {
                "Name": "Mobile Phone",
                "Confidence": 94.71910858154297,
                "Instances": [
                    {
                        "BoundingBox": {
                            "Width": 0.36574506759643555,
                            "Height": 0.17807289958000183,
                            "Left": 0.5576263666152954,
                            "Top": 0.36066752672195435
                        },
                        "Confidence": 94.71910858154297
                    }
                ],
                "Parents": [
                    {
                        "Name": "Electronics"
                    },
                    {
                        "Name": "Phone"
                    }
                ]
            },
            {
                "Name": "Phone",
                "Confidence": 94.71910858154297,
                "Instances": [],
                "Parents": [
                    {
                        "Name": "Electronics"
                    }
                ]
            },
            {
                "Name": "Head",
                "Confidence": 83.61711120605469,
                "Instances": [],
                "Parents": [
                    {
                        "Name": "Person"
                    }
                ]
            },
            {
                "Name": "Face",
                "Confidence": 82.2411117553711,
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
                "Name": "Pink Hair",
                "Confidence": 76.5530776977539,
                "Instances": [],
                "Parents": [
                    {
                        "Name": "Hair"
                    },
                    {
                        "Name": "Person"
                    }
                ]
            }
        ],
        "LabelModelVersion": "3.0"
    }
        
        automaticRekognition = usecase(rekognitionResult=rekognitionResult)
        assert automaticRekognition.labels[-1].name == "Phone" 
        assert automaticRekognition.automaticallyRejected == True
        
        
