from enum import Enum
import os


class Config():
    sqlConnection: str


class ConfigLocal(Config):
    def __init__(self) -> None:
        super().__init__()
        self.access_key = "foo"
        self.secret_key = "bar"
        self.endpoint_url = "http://localhost:4566"
        self.dynamo_table_name = os.getenv("DYNAMO_TABLE_NAME") or "IaCStack-IaCDynamo5EF9A8C0-b18f4594"


class ConfigDes(Config):
    def __init__(self) -> None:
        super().__init__()


class ConfigProd(Config):
    def __init__(self) -> None:
        super().__init__()


class EnvEnum(Enum):
    MOCK = 'Mock'
    LOCAL = 'Local'
    DES = 'Development'
    PROD = 'Production'


class Envs:
    appEnv: EnvEnum = EnvEnum(os.getenv('PYTHON_ENV') or 'Local')

    @staticmethod
    def IsMock():
        return Envs.appEnv == EnvEnum.MOCK

    @staticmethod
    def IsLocal():
        return Envs.appEnv == EnvEnum.LOCAL

    @staticmethod
    def IsDes():
        return Envs.appEnv == EnvEnum.DES

    @staticmethod
    def IsProd():
        return Envs.appEnv == EnvEnum.PROD

    @staticmethod
    def getConfig() -> Config:
        if (Envs.IsLocal()):
            return ConfigLocal()
        if (Envs.IsDes()):
            return ConfigDes()
        if (Envs.IsProd()):
            return ConfigProd()
        return ConfigLocal()