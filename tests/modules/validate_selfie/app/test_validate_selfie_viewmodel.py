from src.modules.validate_selfie.app.validate_selfie_viewmodel import ValidateSelfieViewModel

class Test_ValidateSelfieViewModel:
    def test_validate_selfie_viewmodel(self):
        data = {
   "automaticallyRejected":False,
   "rejectionReasons":[
      "NONE"
   ],
   "labels":[
      {
         "name":"Photography",
         "confidence":100,
         "coords":[
            
         ],
         "parents":[
            
         ]
      },
      {
         "name":"Portrait",
         "confidence":100,
         "coords":[
            
         ],
         "parents":[
            "Face",
            "Head",
            "Person",
            "Photography"
         ]
      },
      {
         "name":"Head",
         "confidence":100,
         "coords":[
            
         ],
         "parents":[
            "Person"
         ]
      },
      {
         "name":"Face",
         "confidence":100,
         "coords":[
            
         ],
         "parents":[
            "Head",
            "Person"
         ]
      },
      {
         "name":"Person",
         "confidence":100,
         "coords":{
            "Width":0.9972279071807861,
            "Height":0.88490229845047,
            "Left":0.0026419830974191427,
            "Top":0.11343356966972351
         },
         "parents":[
            
         ]
      },
      {
         "name":"Neck",
         "confidence":99.97637939453125,
         "coords":[
            
         ],
         "parents":[
            "Body Part",
            "Face",
            "Head",
            "Person"
         ]
      },
      {
         "name":"Body Part",
         "confidence":99.97637939453125,
         "coords":[
            
         ],
         "parents":[
            
         ]
      },
      {
         "name":"Woman",
         "confidence":99.62065124511719,
         "coords":{
            "Width":0.9972279071807861,
            "Height":0.88490229845047,
            "Left":0.0026419830974191427,
            "Top":0.11343356966972351
         },
         "parents":[
            "Adult",
            "Female",
            "Person"
         ]
      },
      {
         "name":"Adult",
         "confidence":99.62065124511719,
         "coords":{
            "Width":0.9972279071807861,
            "Height":0.88490229845047,
            "Left":0.0026419830974191427,
            "Top":0.11343356966972351
         },
         "parents":[
            "Person"
         ]
      },
      {
         "name":"Female",
         "confidence":99.62065124511719,
         "coords":{
            "Width":0.9972279071807861,
            "Height":0.88490229845047,
            "Left":0.0026419830974191427,
            "Top":0.11343356966972351
         },
         "parents":[
            "Person"
         ]
      },
      {
         "name":"Smile",
         "confidence":99.51373291015625,
         "coords":[
            
         ],
         "parents":[
            "Face",
            "Happy",
            "Head",
            "Person"
         ]
      },
      {
         "name":"Happy",
         "confidence":99.51373291015625,
         "coords":[
            
         ],
         "parents":[
            "Face",
            "Head",
            "Person"
         ]
      }
   ]
}
        viewmodel = ValidateSelfieViewModel(data=data)
        
        assert viewmodel.to_dict() == {'automaticallyRejected': False, 'rejectionReasons': ['NONE'], 'labels': [{'name': 'Photography', 'confidence': 100, 'coords': [], 'parents': []}, {'name': 'Portrait', 'confidence': 100, 'coords': [], 'parents': ['Face', 'Head', 'Person', 'Photography']}, {'name': 'Head', 'confidence': 100, 'coords': [], 'parents': ['Person']}, {'name': 'Face', 'confidence': 100, 'coords': [], 'parents': ['Head', 'Person']}, {'name': 'Person', 'confidence': 100, 'coords': {'Width': 0.9972279071807861, 'Height': 0.88490229845047, 'Left': 0.0026419830974191427, 'Top': 0.11343356966972351}, 'parents': []}, {'name': 'Neck', 'confidence': 99.97637939453125, 'coords': [], 'parents': ['Body Part', 'Face', 'Head', 'Person']}, {'name': 'Body Part', 'confidence': 99.97637939453125, 'coords': [], 'parents': []}, {'name': 'Woman', 'confidence': 99.62065124511719, 'coords': {'Width': 0.9972279071807861, 'Height': 0.88490229845047, 'Left': 0.0026419830974191427, 'Top': 0.11343356966972351}, 'parents': ['Adult', 'Female', 'Person']}, {'name': 'Adult', 'confidence': 99.62065124511719, 'coords': {'Width': 0.9972279071807861, 'Height': 0.88490229845047, 'Left': 0.0026419830974191427, 'Top': 0.11343356966972351}, 'parents': ['Person']}, {'name': 'Female', 'confidence': 99.62065124511719, 'coords': {'Width': 0.9972279071807861, 'Height': 0.88490229845047, 'Left': 0.0026419830974191427, 'Top': 0.11343356966972351}, 'parents': ['Person']}, {'name': 'Smile', 'confidence': 99.51373291015625, 'coords': [], 'parents': ['Face', 'Happy', 'Head', 'Person']}, {'name': 'Happy', 'confidence': 99.51373291015625, 'coords': [], 'parents': ['Face', 'Head', 'Person']}]}