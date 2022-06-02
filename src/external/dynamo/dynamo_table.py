import boto3

from src.envs import Envs


class DynamoTable:

    def __init__(self):
        self.access_key = Envs.getConfig().access_key
        self.secret_key = Envs.getConfig().secret_key
        self.endpoint_url = Envs.getConfig().endpoint_url
        self.dynamo_table_name = Envs.getConfig().dynamo_table_name


    def __enter__(self):
        s = boto3.Session(
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key)
        dynamo = s.resource('dynamodb', endpoint_url=self.endpoint_url)
        table = dynamo.Table(self.dynamo_table_name)
        return table

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass