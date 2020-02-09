from flask import jsonify, request
from flask_cors import cross_origin
from flask_restplus import reqparse

from flask_restful import Resource



def get_params():
    parser = reqparse.RequestParser()
    parser.add_argument('prop')
    parser.add_argument('nbr', type=int)
    args = parser.parse_args()
    return args


class test_params(Resource):
    @cross_origin("*")
    def get(self):
        PARAMS = request.args
        for i in PARAMS:
            print(i,PARAMS.get(i))
        return jsonify(PARAMS)


