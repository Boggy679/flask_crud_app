from flask import Flask, request
import boto3
from boto3.dynamodb.conditions import Key
from dynamo.insert_items import table

dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8000", region_name="us-west-2",
                          aws_access_key_id="foo", aws_secret_access_key="foo")

app = Flask(__name__)


@app.route("/")
def get_hello():
    return "hello!"


@app.route("/books")
def get_books():
    author = request.args.get("author")
    title = request.args.get("title")

    try:
        table = dynamodb.Table("Books")
        response = table.query(KeyConditionExpression=Key("Author").eq(author))
        results = []
        for item in response["Items"]:
            results.append(item)
            return item

    except Exception as ex:
        print("Error when getting an item")
        print(ex)

@app.route("/add_book")
def add_books():
    author = request.args.get("author")
    title = request.args.get("title")
    category = request.args.get("category")

    table.put_item(Item={
        "Author": author,
        "Title": title,
        "Category": category
    })
    return "Item is already in!"


app.run(port=5000)