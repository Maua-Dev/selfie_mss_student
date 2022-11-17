import boto3


class DynamoTable:

    def __init__(self, access_key, secret_key, endpoint_url, dynamo_table_name, region):
        self.access_key = access_key
        self.secret_key = secret_key
        self.endpoint_url = endpoint_url
        self.dynamo_table_name = dynamo_table_name
        self.region = region


    def __enter__(self):
        s = boto3.Session(
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            region_name=self.region)
        dynamo = s.resource('dynamodb', endpoint_url=self.endpoint_url)
        table = dynamo.Table(self.dynamo_table_name)
        return table

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass