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


class EnvEnum(Enum):
    MOCK = 'Mock'
    LOCAL = 'Local'
    DEV = 'Development'
    PROD = 'Production'


class Envs:
    appEnv: EnvEnum = EnvEnum(os.getenv('PYTHON_ENV') or 'Mock')

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
        load_dotenv()
        if (Envs.IsLocal()):
            return Config(access_key="foo",
                          secret_key="bar",
                          endpoint_url="http://localhost:4566",
                          dynamo_table_name=os.getenv(
                              "DYNAMO_TABLE_NAME_LOCAL") or "IaCStack-IaCDynamo5EF9A8C0-b18f4594",
                          region=os.getenv("REGION_LOCAL"))
        if (Envs.IsDev()):
            return Config(access_key=os.getenv("DYNAMO_ACCESS_KEY_DEV"),
                          secret_key=os.getenv("DYNAMO_SECRET_KEY_DEV"),
                          endpoint_url=os.getenv("DYNAMO_ENDPOINT_URL_DEV"),
                          dynamo_table_name=os.getenv("DYNAMO_TABLE_NAME_DEV") or "IaCStack-IaCDynamo5EF9A8C0-b18f4594",
                          region=os.getenv("REGION_DEV"))
        if (Envs.IsProd()):
            return Config(access_key=os.getenv("DYNAMO_ACCESS_KEY"),
                          secret_key=os.getenv("DYNAMO_SECRET_KEY"),
                          endpoint_url=os.getenv("DYNAMO_ENDPOINT_URL"),
                          dynamo_table_name=os.getenv("DYNAMO_TABLE_NAME"),
                          region=os.getenv("REGION"))
        return Config()  # Config de MOCK
