from datetime import datetime
import uuid
from src.shared.domain.repositories.selfie_repository_interface import ISelfieRepository


class SelfieRepositoryMock(ISelfieRepository):

        
    def generate_uuid_key(self, ra: str) -> str:
        object_name = f"{ra}/selfie-{datetime.today().strftime('%Y-%m-%d-%H:%M:%S')}-{str(uuid.uuid4())[:5]}.jpeg"
        return object_name


    def request_upload_selfie(self, ra: str, name: str, email: str) -> dict:
        return {
                "url":"https://test-selfie-bucket.s3.amazonaws.com/",
                "metadata":{
                    "ra":f"{ra}",
                    "name":f"{name}",
                    "email":f"{email}"
                }
              }