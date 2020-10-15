from flask import Flask, jsonify,request
from flask_restful import Resource, Api
import sqlite3
import requests

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return jsonify({"Data": "Get Request Suceefull"})

    def post(self):
        with sqlite3.connect('data.db') as conn:
            cur=conn.cursor()
            cur.execute("INSERT INTO data VALUES('hello world','12')")
            conn.commit()
        some_josn=request.get_json()
        print(some_josn)
        return {"Data": "Post request suceessfult"}


api.add_resource(HelloWorld, '/hello')


@app.route('/')
def home():
    return "This is homepage"


if __name__ == '__main__':
    app.run(debug=True)
