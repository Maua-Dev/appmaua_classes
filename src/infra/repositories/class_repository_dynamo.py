from typing import List
from boto3.dynamodb.conditions import Attr

from src.infra.dtos.class_dynamo_dto import ClassDynamoDTO
from src.domain.entities._class import Class
from src.domain.repositories.class_repository_interface import IClassRepository
from src.external.dynamo.datasources.dynamo_datasource import DynamoDatasource
from src.envs import Envs


class ClassRepositoryDynamo(IClassRepository):
    dynamo: DynamoDatasource

    def __init__(self):
        self.dynamo = DynamoDatasource(access_key=Envs.getConfig().access_key,
                                       secret_key=Envs.getConfig().secret_key, endpoint_url=None,
                                       dynamo_table_name=Envs.getConfig().dynamo_table_name,
                                       region=Envs.getConfig().region)

    async def get_student_week_classes(self, ra: str) -> List[Class]:
        data = await self.dynamo.scanItems(filterExpression=Attr("studentRA").eq(ra))

        return [ClassDynamoDTO.fromDynamo(item).toEntity() for item in data]


