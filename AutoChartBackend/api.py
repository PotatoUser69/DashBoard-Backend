from flask import Flask, jsonify,send_file
from flask_cors import CORS
from flask_restful import Resource, Api
from determine_chart import files ,main

app = Flask(__name__)
api = Api(app)

CORS(app)

dataset_names = []
class Datasets(Resource):
    def get(self):
        dataset_names=files()
        return {'labels': dataset_names}
api.add_resource(Datasets, '/datasets')

class Chart(Resource):
    def get(self,chart):
        data,secondary=main(chart)
        return {'data':data,"secondary":secondary}

api.add_resource(Chart, '/chart/<string:chart>')

class HTMLRead(Resource):
    def get(self,file):
        return send_file(f'C:\\Users\\totti\\VSCodeProjects\\Flask\\AutoChartBackend\\charts\\{file}')

api.add_resource(HTMLRead, '/htmlread/<string:file>')

if __name__ == '__main__':
    app.run(debug=True)