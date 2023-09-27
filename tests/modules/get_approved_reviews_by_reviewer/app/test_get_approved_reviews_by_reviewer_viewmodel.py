from src.modules.get_approved_reviews_by_reviewer.app.get_approved_reviews_by_reviewer_viewmodel import GetApprovedSelfiesByReviewerViewModel
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock


class Test_GetApprovedSelfiesByReviewerViewModel:
    def test_get_approved_selfies_by_reviewer__viewmodel(self):
        repo = StudentRepositoryMock()
        reviews = [repo.reviews[0], repo.reviews[1]] 
        approvedSelfiesViewmodel = GetApprovedSelfiesByReviewerViewModel(reviews, repo.reviews[0].reviewer).to_dict()

        expected = {
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
        assert expected == approvedSelfiesViewmodel