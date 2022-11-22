
class RequestUploadSelfieViewModel:
    presignedPost: dict

    def __init__(self, presignedPost: dict):
      self.presignedPost = presignedPost

    def to_dict(self) -> dict:
        return {
          "url":self.presignedPost["url"],
          "fields":{
              "x-amz-meta-ra": self.presignedPost["metadata"].get("ra", "NONE"),
              "x-amz-meta-name":self.presignedPost["metadata"].get("name", "NONE"),
              "x-amz-meta-email": self.presignedPost["metadata"].get("email", "NONE"),
          }
        }