import os
from flask import jsonify, request
from flask_cors import cross_origin

from flask_restful import Resource
from owlready2 import default_world, get_ontology

INSTANCES_FOLDER = "/home/marjorie/Bureau/uploads/Instance/"


def get_files():
    files_name = os.listdir(INSTANCES_FOLDER)
    onto_base = get_ontology("/home/marjorie/Bureau/uploads/ontology/Tbox.owl").load()
    if len(files_name) != 0:
        for instance in files_name:
            onto_base = get_ontology(INSTANCES_FOLDER + instance).load()
            continue

class applyQuery(Resource):
    @cross_origin("*")
    def get(self, child):
        graph = default_world.as_rdflib_graph()

        testreq = request.query_string
        print(testreq)
        req1 = child.replace("!", "?")
        req = req1.replace("$", "#")
        print(req)
        res = list(graph.query(str(req)))

        return jsonify(res)


class get_query(Resource):
    @cross_origin("*")
    def post(self):
        req = request.values["value"]
        get_files()
        graph = default_world.as_rdflib_graph()
        res = list(graph.query(str(req)))
        graph.close()
        return jsonify(res)

# @kbquering.errorhandler(404)
# def not_found(error):
#   return make_response(jsonify({'error': 'Bad Query'}), 404)
