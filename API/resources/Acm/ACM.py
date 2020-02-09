import os

from flask import request, jsonify
from flask_restful import Resource
from flask_cors import cross_origin
from owlready2 import get_ontology, default_world

INSTANCES_FOLDER = "/home/marjorie/Bureau/uploads/Conflict instances/"


def get_files():
    files_name = os.listdir(INSTANCES_FOLDER)
    if len(files_name) != 0:
        for instance in files_name:
            onto_base = get_ontology(INSTANCES_FOLDER + instance).load()
            continue


def get_query_results():
    get_files()
    graph = default_world.as_rdflib_graph()
    res = list(graph.query("""select ?conflict  ?ACM where { 
    ?conflict <http://www.semanticweb.org/ayoubpc/ontologies/2019/11/untitled-ontology-15#resolved_by> ?ACM.
}
    """))
    graph.close()
    return res


for i in set(get_query_results()):
    print(i)


class get_ACM(Resource):
    @cross_origin("*")
    def get(self):
        queryresults = set(get_query_results())
        arg = request.args
        for i in queryresults:
            if i[0].split("#")[1] == arg["conflict"]:
                return jsonify(i[1].split("#")[1])
            else:
                return jsonify('No ACM founded!!!!')
