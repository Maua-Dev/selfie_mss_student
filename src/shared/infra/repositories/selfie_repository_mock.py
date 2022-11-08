import datetime
import uuid
from src.shared.domain.repositories.selfie_repository_interface import ISelfieRepository


class SelfieRepositoryMock(ISelfieRepository):

        
    def uuid_pic_generator_generate(self, ra: str):

        object_name = f"{ra}/selfie-{datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}-{str(uuid.uuid4())[:5]}.jpeg"
        return object_name


    def request_upload_selfie(self, ra: str, name: str, email: str, url: str) -> dict:
        return {
                "url":"https://test-selfie-bucket.s3.amazonaws.com/",
                "fields":{
                    "x-amz-meta-ra":f"{ra}",
                    "x-amz-meta-name":f"{name}",
                    "x-amz-meta-email":f"{email}",
                    "key":self.uuid_pic_generator_generate(ra),
                    "AWSAccessKeyId":f"ACCESSKEY-{ra}",
                    "policy":f"POLICY-{ra}",
                    "signature":f"SIGNATURE-{ra}"
                }
              }