import json

from boto3.dynamodb.conditions import Key

from src.external.dynamo.dynamo_table import DynamoTable

from decimal import Decimal


class DynamoDatasource:
    """
    Docs:
    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table
    """

    def __init__(self, access_key, secret_key, endpoint_url, dynamo_table_name, region):
        self.dynamoTable = DynamoTable(access_key=access_key, secret_key=secret_key, endpoint_url=endpoint_url,
                                       dynamo_table_name=dynamo_table_name, region=region)

    @staticmethod
    def parseFloatToDecimal(item):
        """
        Parse float to Decimal
        @param item: dict with the keys (Partition and Sort) and data to insert
        """
        item_parsed = json.loads(json.dumps(item), parse_float=Decimal)
        return item_parsed

    async def putItem(self, item: dict):
        """
        Insert a new item into the table or hard update an existing one.
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.put_item
        @param item: dict with the keys (Partition and Sort) and data to insert
        @return: dict with the response from DynamoDB
        """

        with self.dynamoTable as table:
            return table.put_item(Item=DynamoDatasource.parseFloatToDecimal(item))

    async def getItem(self, key):
        """
        Get an item from the table from its keys (Partition and Sort).
        @param key: dict with the keys (Partition and Sort)
        @return: dict with the response from DynamoDB
        """

        with self.dynamoTable as table:
            resp = table.get_item(
                Key=key
            )
            return resp

    async def hardUpdateItem(self, item):
        """
        Hard update an item in the table (must have its keys - Partition and Sort).
        @param item: dict with the keys (Partition and Sort) and data to insert
        @return: dict with the response from DynamoDB
        """

        with self.dynamoTable as table:
            resp = table.put_item(Item=DynamoDatasource.parseFloatToDecimal(item))
            return resp

    async def updateItem(self, key, updateAttributes):
        """
        Update an item in the table with its keys (Partition and Sort) and attributes to update
        If the attribute does not exist, it will be created. It won't change attributes not mentioned.
        @param key: dict with the keys (Partition and Sort)
        @param updateAttributes: dict with the attributes to update
        @return: dict with the response from DynamoDB
        """

        with self.dynamoTable as table:
            resp = table.update_item(
                Key=key,
                AttributeUpdates=updateAttributes
            )
            return resp

    async def deleteItem(self, key):
        """
        Delete an item from the table from its keys (Partition and Sort).
        @param key: dict with the keys (Partition and Sort)
        @return: dict with the response from DynamoDB
        """

        with self.dynamoTable as table:
            resp = table.delete_item(
                Key=key
            )
            return resp


    async def getAllItems(self):
        """
        Get all items from the table.
        @return: dict with the response from DynamoDB
        """

        with self.dynamoTable as table:
            resp = table.scan()
            return resp['Items']

    async def query(self, keyConditionExpression, **kwargs):
        """
        Query the table with the KeyConditionExpression.
        Example: KeyConditionExpression=Key('Partition').eq('partition') & Key('Sort').gte('sort')
        Obs: Key de boto3.dynamodb.conditions.Key
        Ref:https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/dynamodb.html#ref-dynamodb-conditions
        @param keyConditionExpression: string with the KeyConditionExpression
        @return: dict with the response from DynamoDB
        """

        with self.dynamoTable as table:
            resp = table.query(
                KeyConditionExpression=keyConditionExpression,
                **kwargs
            )
            return resp['Items']

    async def batchWriteItems(self, items):
        """
        Write a list of items to the table. Each item must have the keys (Partition and Sort).
        @param items: list of dicts with the keys (Partition and Sort) and data to insert
        """

        with self.dynamoTable as table:
            with table.batch_writer() as batch:
                for i in items:
                    batch.put_item(Item=DynamoDatasource.parseFloatToDecimal(i))

    async def batchDeleteItems(self, keys):
        """
        Delete a list of items from the table. Each item must have only the keys (Partition and Sort).
        @param keys: list of dicts with the keys (Partition and Sort)
        Example: keys=[ {'Partition': 'partition1', 'Sort': 'sort2'}, {'Partition': 'partition1', 'Sort': 'sort2'} ]
        """

        with self.dynamoTable as table:
            with table.batch_writer() as batch:
                for k in keys:
                    batch.delete_item(Key=k)