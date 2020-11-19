import boto3

dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8000", region_name="us-west-2",
                           aws_access_key_id="foo", aws_secret_access_key="foo")

try:
    table = dynamodb.Table("Books")
    with table.batch_writer() as batch:
        batch.put_item(
            Item={"Author": "John Smith", "Title": "Alice at school", "Category": "Suspense",
                  "Formats": {"Hardcover": "457246", "Paperback": "37593083"}}
        )
        batch.put_item(
            Item={"Author": "Lucy Brown", "Title": "How to be happy", "Category": "Suspense",
                  "Formats": {"Hardcover": "4572", "Paperback": "373083"}
                  }
        )
        batch.put_item(
            Item={"Author": "Lucy Brown", "Title": "How to be happy 2", "Category": "Suspense",
                  "Formats": {"Hardcover": "4572", "Paperback": "373083"}
                  }
        )

except Exception as e:
    print("Error when inserting items")
    print(e)
