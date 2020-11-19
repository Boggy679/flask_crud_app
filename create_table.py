import boto3

dynamdodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8000", region_name="us-west-2",
                           aws_access_key_id="foo", aws_secret_access_key="foo")
print(dynamdodb)


try:
    table = dynamdodb.create_table(
        TableName="Books",
        KeySchema=[
            {
                "AttributeName": "Author",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "Title",
                "KeyType": "RANGE"
            }],
        AttributeDefinitions=[
            {
                "AttributeName": "Author",
                "AttributeType": "S"
            },
            {
                "AttributeName": "Title",
                "AttributeType": "S"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        }
    )

except Exception as e:
    print("Error when creating table")
    print(e)
