import boto3

dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8000", region_name="us-west-2",
                           aws_access_key_id="foo", aws_secret_access_key="foo")

try:
    table = dynamodb.Table("Books")

    response = table.get_item(Key={"Author": "John Smith", "Title": "Alice at school"})
    print(response["Item"])

    table.update_item(
        Key={"Author": "John Smith", "Title": "Alice at school"},
        ExpressionAttributeNames={
            "#formats": "Formats",
            "#audiobook": "Audiobook"
        },
        ExpressionAttributeValues={
            ":id": "759327506"
        },
        UpdateExpression="SET #formats.#audiobook = :id"
    )
    print("the item after update")
    response = table.get_item(Key={"Author": "John Smith", "Title": "Alice at school"})
    print(response["Item"])

except Exception as e:
    print("Error when updating table")
    print(e)