from typing import List
import os
import boto3

from src.domain.entities._class import Class
from src.domain.repositories.class_repository_interface import IClassRepository


class SubjectRepositoryDynamo(IClassRepository):

    def __init__(self):
        s = boto3.Session(
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])
        self.dynamo = s.resource('dynamodb', endpoint_url=os.environ.get('AWS_ENDPOINT_URL'))
        self.table = self.dynamo.Table(os.environ['DYNAMO_TABLE_NAME'])

    async def get_student_week_classes(self, ra: str) -> List[Class]:
        # todo implement method
        pass
