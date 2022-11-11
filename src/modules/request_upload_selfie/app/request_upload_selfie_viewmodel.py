
class RequestUploadSelfieViewModel:
    presignedPost: dict

    def __init__(self, presignedPost: dict):
      self.presignedPost = presignedPost

    def to_dict(self) -> dict:
        return {
          "url":self.presignedPost["url"],
          "fields":{
              "key":self.presignedPost["fields"]["key"],
              "x-amz-meta-ra": self.presignedPost["fields"]["x-amz-meta-ra"],
              "x-amz-meta-name":self.presignedPost["fields"]["x-amz-meta-name"],
              "x-amz-meta-email": self.presignedPost["fields"]["x-amz-meta-email"],
              "AWSAccessKeyId":self.presignedPost["fields"]["AWSAccessKeyId"],
              "policy":self.presignedPost["fields"]["policy"],
              "signature":self.presignedPost["fields"]["signature"]
          }
        }