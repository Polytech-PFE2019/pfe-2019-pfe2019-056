from flask import request, jsonify
from flask_cors import cross_origin
from flask_restful import reqparse, Resource
import random


def get_params():
    parser = reqparse.RequestParser()
    parser.add_argument('user')
    parser.add_argument('activity')
    parser.add_argument('environment')
    args = parser.parse_args()
    return args


def add_instance(params):
    file = open("/home/marjorie/Bureau/uploads/instance.owl", 'r+')
    file_lines = file.readlines()
    file.close()
    new_lines = []
    for line in file_lines:
        if '?USER?' in line:
            new_lines.append(line.replace('?USER?', params['user']))
        elif '?ENVIRONNEMENT?' in line:
            new_lines.append(line.replace('?ENVIRONNEMENT?', params['environment']))
        elif '?ACTIVITY?' in line:
            new_lines.append(line.replace('?ACTIVITY?', params['activity']))
        else:
            new_lines.append(line)
    new_file = open(
        "/home/marjorie/Bureau/uploads/Instance/instance" + str(random.randint(0, 10000)) + ".owl",
        'w+')
    new_file.writelines(new_lines)
    new_file.close()


class instance_params(Resource):
    @cross_origin("*")
    def post(self):
        req = request.values["activity"]
        if not request.values :
            return jsonify('Parameters are empty')
        else :
            add_instance(request.values)
            return jsonify("Success , instance was added!!!")
