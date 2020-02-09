from flask import Flask
from flask_restful import Api
from resources.upload.uploadFile import UploadFile
from resources.KBqueering.kbqueering import applyQuery, get_query
from resources.QueryBuilding.querybuilder import test_params
from resources.InstanceBuilder.instancebuilder import instance_params
from resources.Conflicts.Conflits import instance_conflicts_params
from resources.Acm.ACM import get_ACM
app = Flask(__name__)
api = Api(app)

api.add_resource(UploadFile, '/upload/')
api.add_resource(applyQuery, '/queering/<string:child>')
api.add_resource(get_query, '/queering/')
api.add_resource(test_params, '/queering/build')
api.add_resource(instance_params, '/add_instance/')
api.add_resource(instance_conflicts_params, '/conflicts/')
api.add_resource(get_ACM, '/ACM')

if __name__ == '__main__':
    app.run()
