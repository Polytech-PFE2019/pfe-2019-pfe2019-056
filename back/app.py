from flask import Flask
from flask_restful import Api
from resources.upload.uploadFile import UploadFile
from resources.KBqueering.kbqueering import applyQuery

app = Flask(__name__)
api = Api(app)

api.add_resource(UploadFile, '/upload/')
api.add_resource(applyQuery, '/queering/<string:child>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
