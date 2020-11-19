import boto3

dynamodb = boto3.client("dynamodb", endpoint_url="http://localhost:8000", region_name="us-west-2",
                           aws_access_key_id="foo", aws_secret_access_key="foo")
try:
    response = dynamodb.delete_table(
        TableName="Books"
    )
except Exception as e:
    print("Error when deleting db")
    print(e)