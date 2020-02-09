import os
import random

from flask import request, jsonify
from flask_cors import cross_origin
from flask_restful import Resource
from owlready2 import get_ontology, default_world

INSTANCES_FOLDER = "/home/marjorie/Bureau/uploads/Instance/"

def get_files():
    files_name = os.listdir(INSTANCES_FOLDER)
    onto_base = get_ontology("/home/marjorie/Bureau/uploads/ontology/Tbox.owl").load()
    if len(files_name) != 0:
        for instance in files_name:
            onto_base = get_ontology(INSTANCES_FOLDER + instance).load()
            continue


def get_query_results():
    get_files()
    graph = default_world.as_rdflib_graph()
    res = list(graph.query("""select distinct ?user ?environement ?activity ?prefreneces where {
 ?user a <http://www.semanticweb.org/ayoubpc/ontologies/2019/11/untitled-ontology-15#User> ;<http://elite.polito.it/ontologies/dogont.owl#LocatedIn> ?environement ; <http://elite.polito.it/ontologies/dogont.owl#Performs> ?activity.

?activity <http://elite.polito.it/ontologies/dogont.owl#hasPrefrences> ?prefreneces.

 ?user1 a <http://www.semanticweb.org/ayoubpc/ontologies/2019/11/untitled-ontology-15#User> ;<http://elite.polito.it/ontologies/dogont.owl#LocatedIn>  ?environement1; <http://elite.polito.it/ontologies/dogont.owl#Performs> ?activity1.

?activity1 <http://elite.polito.it/ontologies/dogont.owl#hasPrefrences> ?prefreneces1.

filter(?user != ?user1 && ?environement = ?environement1 && ?prefreneces != ?prefreneces1)
}
    """))
    graph.close()
    inst_dict = {}
    for r in res:
        # print(str(r[0]).split('#')[1], str(r[1]).split('#')[1], str(r[2]).split('#')[1], str(r[3]).split('#')[1])
        inst_dict[str(r[0]).split('#')[1]] = {'environment': str(r[1]).split('#')[1],
                                              'activity': str(r[2]).split('#')[1],
                                              'preference': str(r[3]).split('#')[1]}
    return inst_dict


def get_environement():
    get_files()
    graph = default_world.as_rdflib_graph()
    res = list(graph.query("""select distinct ?environement where {
         ?user a <http://www.semanticweb.org/ayoubpc/ontologies/2019/11/untitled-ontology-15#User> ;<http://elite.polito.it/ontologies/dogont.owl#LocatedIn> ?environement .
        }
        """))
    graph.close()
    environement = []
    for r in res:
        environement.append(str(r[0]).split('#')[1])
    return environement


def get_conflicts_params():
    conflicts = {}

    inst_dictionnary = get_query_results()
    environements = get_environement()
    for env in environements:
        instances = []
        for inst in inst_dictionnary:
            if str(env) == str(inst_dictionnary[inst]["environment"]):
                # print(env,inst_dictionnary[inst])
                instances.append({inst: inst_dictionnary[inst]})
        conflicts[env] = instances
    return conflicts


print(get_conflicts_params())


def get_conflicts():
    conflicts_params = get_conflicts_params()
    list_conflicts = []
    for conflict_env in conflicts_params:
        if conflicts_params[conflict_env]:
            list_conflicts.append('Conflict_' + str(conflict_env) + '_' +
                                  conflicts_params[conflict_env][0][list(conflicts_params[conflict_env][0].keys())[0]][
                                      "preference"].split("_")[0])
    return list_conflicts


print(get_conflicts())


def add_instance(params):
    file = open("/home/marjorie/Bureau/uploads/conflict-instance.owl", 'r+')
    file_lines = file.readlines()
    file.close()
    new_lines = []
    conflict_params = params.split('_')
    for line in file_lines:
        if '?Conflict?' in line:
            new_lines.append(line.replace('?Conflict?', params))
        elif '?Conflict_type?' in line:
            new_lines.append(line.replace('?Conflict_type?', conflict_params[2].capitalize() + '_conflict'))
        elif '?Conflict_zone?' in line:
            new_lines.append(line.replace('?Conflict_zone?', conflict_params[1]))
        elif 'ACM?' in line:
            new_lines.append(line.replace('?ACM?', conflict_params[2] + '_ACM'))
        else:
            new_lines.append(line)
    new_file = open(
        "/home/marjorie/Bureau/uploads/Conflict instances/Conflict_instance" + str(
            random.randint(0, 10000)) + ".owl",
        'w+')
    new_file.writelines(new_lines)
    new_file.close()


class instance_conflicts_params(Resource):
    @cross_origin("*")
    def get(self):
        conflict_list = get_conflicts()
        if not conflict_list:
            return jsonify('No conflict detected')
        else:
            for i in conflict_list:
                add_instance(i)
            return jsonify(conflict_list)
