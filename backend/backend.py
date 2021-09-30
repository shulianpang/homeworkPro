
from flask import Flask, request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

testcases =[]

class TestCase(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        testcase = request.json
        testcases.append(testcase)
        app.logger.info(testcases)
        app.logger.info(testcases)
        return testcase

    def put(self):
        pass

    def delete(self):
        name = request.json['name']
        for item in testcases:
            if item['name'] == name:
                testcases.remove(item)

        app.logger.info({'testcases:':testcases})


api.add_resource(TestCase,'/testcase')


# @app.route('/')
# def hello_world():
#     return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
