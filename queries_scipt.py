#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 04:22:31 2023

@author: manuelgutierrez
"""

from owlready2 import *
from owlready2 import sync_reasoner
from rdflib.plugins.sparql import prepareQuery

onto_path.append("./data_project.owl")
onto = get_ontology('data_project.owl').load()


def get_basic_Info():
    #sync_reasoner(onto)

    # Printing basic information of our ontology
    print("These are our classes:", list(onto.classes()))
    print("\nThese are our individuals:", list(onto.individuals()))
    print("\nThese are our object properties:", list(onto.object_properties()))
    print("\nThese are our data properties:", list(onto.data_properties()))
    
    
def get_Individuals_based_on_class(str_class):
    str_class = str_class.lower()
    if str_class == "movie":
        instances = onto.Movie.instances()
    elif str_class == "actor":
        instances = onto.Actor.instances()
    elif str_class == "contry":
        instances = onto.Contry.instances()
    elif str_class == "director":
        instances = onto.Director.instances()
    elif str_class == "producer":
        instances = onto.Producer.instances()
    elif str_class == "writer":
        instances = onto.Writer.instances()    
    elif str_class == "language":
        instances = onto.Language.instances()
    elif str_class == "production_co":
        instances = onto.Production_CO.instances()
    else:
        print(str_class," Not found")
        return "Class not found"
    # Loop over the instances and print their names
    for instance in instances:
        print(str_class," ",instance.name)
        
        

    
if __name__ == '__main__':
    #get_basic_Info()
    get_Individuals_based_on_class("dtrfyguhi")

