import os
from flask import Flask, request, jsonify
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
from flask_restful import Resource

UPLOAD_FOLDER = "/home/marjorie/Bureau/uploads/Instance"

ALLOWED_EXTENSIONS = set(['rdfs', 'xml', 'ttl', 'owl', 'rdf'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




class UploadFile(Resource):
    @cross_origin("*")
    def post(self):
        if 'file' not in request.files:
            resp = jsonify({'message': 'No file part in the request'})
            resp.status_code = 400
            return resp
        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message': 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            resp = jsonify({'message': 'File successfully uploaded'})
            resp.status_code = 201
            return resp
        else:
            resp = jsonify({'message': 'Allowed file types are rdf, ttl, owl, xml'})
            resp.status_code = 400
            return resp
