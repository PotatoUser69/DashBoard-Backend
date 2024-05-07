from flask import Flask, jsonify,send_file
from flask_cors import CORS
from flask_restful import Resource, Api
from determine_chart import files ,main
from flask_appbuilder.api import BaseApi, expose,rison
from . import appbuilder


dataset_names = []

class Datasets(BaseApi):
    @expose('/')
    def get(self):
        dataset_names=files()
        return {'labels': dataset_names}

class Chart(BaseApi):
    @expose('/')
    @rison()
    def get(self,**kwargs):
        data=main(kwargs['rison']['chart'])
        return {'data':data}


class HTMLRead(BaseApi):
    @expose('/')
    @rison()
    def get(self,**kwargs):
        file=kwargs['rison']['file']
        return send_file(f'C:\\Users\\totti\\VSCodeProjects\\Flask\\AutoChartBackend\\charts\\{file}')

appbuilder.add_api(Datasets)
appbuilder.add_api(Chart)
appbuilder.add_api(HTMLRead)