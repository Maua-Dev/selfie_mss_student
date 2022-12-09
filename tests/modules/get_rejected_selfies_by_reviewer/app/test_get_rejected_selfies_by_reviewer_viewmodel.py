from src.modules.get_rejected_selfies_by_reviewer.app.get_rejected_selfies_by_reviewer_viewmodel import GetRejectedSelfiesByReviewerViewModel
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock


class Test_GetRejectedSelfiesByReviewerViewModel:
    def test_get_rejected_selfies_by_reviewer__viewmodel(self):
        repo = StudentRepositoryMock()
        reviews = [repo.reviews[7], repo.reviews[9]] 
        rejectedSelfies = GetRejectedSelfiesByReviewerViewModel(reviews, repo.reviews[9].reviewer).to_dict()

        expected = {
   "reviewer":{
      "ra":"04618",
      "name":"Bruno Cambui Marques",
      "email":"bruno.marques@maua.br",
      "active":True
   },
   "rejectedSelfies":[
      {
         "idReview":1,
         "state":"DECLINED",
         "selfie":{
            "idSelfie":2,
            "dateCreated":"2022-10-12T16:01:59.149927",
            "url":"https://i.imgur.com/4ewA19S.png",
            "state":"DECLINED",
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
                  },
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
                  }
               ]
            },
            "student":{
               "ra":"15013103",
               "name":"Little Ronald",
               "email":"iamronald@mageofprogramming.com.br"
            }
         },
         "dateAssigned":"2022-11-01T16:01:59.149927",
         "dateReviewed":"2022-12-02T16:05:59.149927"
      },
      {
         "idReview":1,
         "state":"DECLINED",
         "selfie":{
            "idSelfie":0,
            "dateCreated":"2022-10-12T16:01:59.149927",
            "url":"https://i.imgur.com/4ewA19S.png",
            "state":"DECLINED",
            "rejectionReasons":[
               "NOT_ALLOWED_BACKGROUND"
            ],
            "rejectionDescription":"O brilho dos olhos dela é senscaional",
            "automaticReview":{
               "automaticallyRejected":False,
               "rejectionReasons":[
                  "NONE"
               ],
               "labels":[
                  {
                     "name":"Photography",
                     "coords":{
                        
                     },
                     "confidence":100.0,
                     "parents":[
                        
                     ]
                  },
                  {
                     "name":"Portrait",
                     "coords":{
                        "Width":0.9711952805519104,
                        "Height":0.8659809827804565,
                        "Left":0.012313545681536198,
                        "Top":0.11108686774969101
                     },
                     "confidence":100.0,
                     "parents":[
                        "Face",
                        "Head",
                        "Person",
                        "Photography"
                     ]
                  },
                  {
                     "name":"Head",
                     "coords":{
                        
                     },
                     "confidence":100.0,
                     "parents":[
                        "Person"
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
                     "confidence":100.0,
                     "parents":[
                        "Person",
                        "Head"
                     ]
                  },
                  {
                     "name":"Person",
                     "coords":{
                        "Width":0.9972279071807861,
                        "Height":0.88490229845047,
                        "Left":0.0026419830974191427,
                        "Top":0.11343356966972351
                     },
                     "confidence":99.62065124511719,
                     "parents":[
                        
                     ]
                  }
               ]
            },
            "student":{
               "ra":"21002088",
               "name":"Maluzinha",
               "email":"mvergani.enactusmaua@gmail.com"
            }
         },
         "dateAssigned":"2022-11-01T16:01:59.149927",
         "dateReviewed":"2022-12-02T16:05:59.149927"
      }
   ],
   "message":"the rejected sefies by reviewer were retriven"
}

        assert expected == rejectedSelfies