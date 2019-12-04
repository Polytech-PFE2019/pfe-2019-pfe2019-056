from flask import Blueprint, jsonify, make_response
from flask_cors import cross_origin

from flask_restful import Resource
from owlready2 import default_world, get_ontology

# @kbquering.route('/queering/<string:child>', methods=['GET'])
onto = get_ontology("C:/Users/Ayoub Pc/Desktop/human.rdf").load()


class applyQuery(Resource):
    @cross_origin("*")
    def get(self, child):
        graph = default_world.as_rdflib_graph()

        res = list(graph.query("""select distinct ?x where {
        ?x <http://www.inria.fr/2007/09/11/humans.rdfs#""" + child + """> ?y
        }"""))

        return jsonify(res)

# @kbquering.errorhandler(404)
# def not_found(error):
#   return make_response(jsonify({'error': 'Bad Query'}), 404)
