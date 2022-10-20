from enum import Enum
import os
from dotenv import load_dotenv


class Config:
    access_key: str
    secret_key: str
    endpoint_url: str
    dynamo_table_name: str
    region: str

    def __init__(self, **kwargs):
        self.access_key = str(kwargs.get("access_key")) if kwargs.get("access_key") else None
        self.secret_key = str(kwargs.get("secret_key")) if kwargs.get("secret_key") else None
        self.endpoint_url = str(kwargs.get("endpoint_url")) if kwargs.get("endpoint_url") else None
        self.dynamo_table_name = str(kwargs.get("dynamo_table_name")) if kwargs.get("dynamo_table_name") else None
        self.region = str(kwargs.get("region")) if kwargs.get("region") else None


class ConfigLocal(Config):
    def __init__(self) -> None:
        load_dotenv()
        super().__init__(access_key="foo",
                         secret_key="bar",
                         endpoint_url="http://localhost:4566",
                         dynamo_table_name=os.getenv("DYNAMO_TABLE_NAME") or "IaCStack-IaCDynamo5EF9A8C0-b18f4594",
                         region=os.getenv("REGION"))


class ConfigDev(Config):
    def __init__(self) -> None:
        load_dotenv()
        super().__init__(access_key=os.getenv("DYNAMO_ACCESS_KEY"),
                         secret_key=os.getenv("DYNAMO_SECRET_KEY"),
                         endpoint_url=os.getenv("DYNAMO_ENDPOINT_URL"),
                         dynamo_table_name=os.getenv("DYNAMO_TABLE_NAME") or "IaCStack-IaCDynamo5EF9A8C0-b18f4594",
                         region=os.getenv("REGION"))


class ConfigProd(Config):
    def __init__(self) -> None:
        load_dotenv()
        super().__init__(access_key=os.getenv("DYNAMO_ACCESS_KEY"),
                         secret_key=os.getenv("DYNAMO_SECRET_KEY"),
                         endpoint_url=os.getenv("DYNAMO_ENDPOINT_URL"),
                         dynamo_table_name=os.getenv("DYNAMO_TABLE_NAME"),
                         region=os.getenv("REGION"))

class EnvEnum(Enum):
    MOCK = 'Mock'
    LOCAL = 'Local'
    DEV = 'Development'
    PROD = 'Production'


class Envs:
    load_dotenv()
    appEnv: EnvEnum = EnvEnum(os.getenv('PYTHON_ENV') or 'Local')

    @staticmethod
    def IsMock():
        return Envs.appEnv == EnvEnum.MOCK

    @staticmethod
    def IsLocal():
        return Envs.appEnv == EnvEnum.LOCAL

    @staticmethod
    def IsDev():
        return Envs.appEnv == EnvEnum.DEV

    @staticmethod
    def IsProd():
        return Envs.appEnv == EnvEnum.PROD

    @staticmethod
    def getConfig() -> Config:
        if (Envs.IsLocal()):
            return ConfigLocal()
        if (Envs.IsDev()):
            return ConfigDev()
        if (Envs.IsProd()):
            return ConfigProd()
        return ConfigLocal()