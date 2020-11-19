import boto3

dynamodb = boto3.client("dynamodb", endpoint_url="http://localhost:8000", region_name="us-west-2",
                           aws_access_key_id="foo", aws_secret_access_key="foo")

response = dynamodb.describe_table(
    TableName="Books"
)

print(response)