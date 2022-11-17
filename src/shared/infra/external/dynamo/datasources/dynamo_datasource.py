import json

from boto3.dynamodb.conditions import Key

from decimal import Decimal

from src.shared.infra.external.dynamo.dynamo_table import DynamoTable


class DynamoDatasource:
    """
    Docs:
    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table
    """
    dynamo_table: DynamoTable
    partition_key: str
    sort_key: str

    def __init__(self, access_key: str, secret_key: str, endpoint_url: str, dynamo_table_name: str, region: str,
                 partition_key: str, sort_key: str = None):

        self.dynamo_table = DynamoTable(access_key=access_key, secret_key=secret_key, endpoint_url=endpoint_url,
                                        dynamo_table_name=dynamo_table_name, region=region)

        self.partition_key = partition_key
        self.sort_key = sort_key

    @staticmethod
    def _parse_float_to_decimal(item):
        """
        Parse float to Decimal
        @param item: dict with the keys (Partition and Sort) and data to insert
        """
        item_parsed = json.loads(json.dumps(item), parse_float=Decimal)
        return item_parsed

    def put_item(self, item: dict, partition_key: str, sort_key: str = None):
        """
        Insert a new item into the table or hard update an existing one.
        Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.put_item
        @param item: dict with the keys (Partition and Sort) and data to insert
        @param partition_key: string with the partition key
        @param sort_key: string with the sort key (optional)
        @return: dict with the response from DynamoDB
        """

        with self.dynamo_table as table:
            item[self.partition_key] = partition_key
            if sort_key:
                item[self.sort_key] = sort_key
            return table.put_item(Item=DynamoDatasource._parse_float_to_decimal(item))

    def get_item(self, partition_key: str, sort_key: str = None):
        """
        Get an item from the table from its keys (Partition and Sort).
        @param partition_key: string with the partition key
        @param sort_key: string with the sort key (optional)
        @return: dict with the response from DynamoDB
        """

        with self.dynamo_table as table:
            resp = table.get_item(
                Key={self.partition_key: partition_key, self.sort_key: sort_key if sort_key else None}
            )
            return resp

    def hard_update_item(self, partition_key: str, sort_key: str, item: dict):
        """
        Hard update an item in the table (must have its keys - Partition and Sort).
        @param partition_key: string with the partition key
        @param sort_key: string with the sort key (optional)
        @param item: dict with data to insert
        @return: dict with the response from DynamoDB
        """

        item[self.partition_key] = partition_key

        if sort_key:
            item[self.sort_key] = sort_key

        with self.dynamo_table as table:
            resp = table.put_item(Item=DynamoDatasource._parse_float_to_decimal(item))
            return resp

    def update_item(self, key, update_attributes):
        """
        Update an item in the table with its keys (Partition and Sort) and attributes to update
        If the attribute does not exist, it will be created. It won't change attributes not mentioned.
        @param key: dict with the keys (Partition and Sort)
        @param update_attributes: dict with the attributes to update
        @return: dict with the response from DynamoDB
        """

        with self.dynamo_table as table:
            resp = table.update_item(
                Key=key,
                AttributeUpdates=update_attributes
            )
            return resp

    def delete_item(self, key):
        """
        Delete an item from the table from its keys (Partition and Sort).
        @param key: dict with the keys (Partition and Sort)
        @return: dict with the response from DynamoDB
        """

        with self.dynamo_table as table:
            resp = table.delete_item(
                Key=key
            )
            return resp

    def get_all_items(self):
        """
        Get all items from the table.
        @return: dict with the response from DynamoDB
        """

        with self.dynamo_table as table:
            resp = table.scan()
            return resp['Items']

    def scan_items(self, filter_expression):
        """
        Scan items from the table.
        @return: dict with the response from DynamoDB
        """

        with self.dynamo_table as table:
            resp = table.scan(FilterExpression=filter_expression)
            return resp['Items']

    def query(self, key_condition_expression, **kwargs):
        """
        Query the table with the KeyConditionExpression.
        Example: KeyConditionExpression=Key('Partition').eq('partition') & Key('Sort').gte('sort')
        Obs: Key de boto3.dynamodb.conditions.Key
        Ref:https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/dynamodb.html#ref-dynamodb-conditions
        @param key_condition_expression: string with the KeyConditionExpression
        @return: dict with the response from DynamoDB
        """

        with self.dynamo_table as table:
            resp = table.query(
                KeyConditionExpression=key_condition_expression,
                **kwargs
            )
            return resp['Items']

    def batch_write_items(self, items):
        """
        Write a list of items to the table. Each item must have the keys (Partition and Sort).
        @param items: list of dicts with the keys (Partition and Sort) and data to insert
        """

        with self.dynamo_table as table:
            with table.batch_writer() as batch:
                for i in items:
                    batch.put_item(Item=DynamoDatasource._parse_float_to_decimal(i))

    def batch_delete_items(self, keys):
        """
        Delete a list of items from the table. Each item must have only the keys (Partition and Sort).
        @param keys: list of dicts with the keys (Partition and Sort)
        Example: keys=[ {'Partition': 'partition1', 'Sort': 'sort2'}, {'Partition': 'partition1', 'Sort': 'sort2'} ]
        """

        with self.dynamo_table as table:
            with table.batch_writer() as batch:
                for k in keys:
                    batch.delete_item(Key=k)


if __name__ == '__main__':
    dynamo = DynamoDatasource(access_key="foobar", secret_key="foobar", endpoint_url="http://localhost:8000",
                              dynamo_table_name="selfie_mss_student-table", region="foobar",
                              partition_key="PK", sort_key="SK")

    print(dynamo.get_item("student#19003315", "selfie#19003315#0"))
