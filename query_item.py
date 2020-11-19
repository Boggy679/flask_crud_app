import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8000", region_name="us-west-2",
                           aws_access_key_id="foo", aws_secret_access_key="foo")

try:
    table = dynamodb.Table("Books")
    respose = table.query(KeyConditionExpression=Key("Author").eq("Lucy Brown"))
    for item in respose["Items"]:
        print(item)

except Exception as ex:
    print("Error when getting an item")
    print(ex)