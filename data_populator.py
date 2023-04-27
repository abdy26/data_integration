#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:17:19 2023

@author: manuelgutierrez
"""

from owlready2 import *
onto_path.append("./moviesssss.owl")
# template_ontology = get_ontology("http://www.semanticweb.org/stefi/ontologies/2021/10/21/untitled-ontology-56")
template_ontology = get_ontology('moviesssss.owl').load()
print("Ontology IRI:", template_ontology.base_iri)

print(template_ontology.Title)

#this is how to get data from there
for individual in template_ontology.individuals():
    print(individual.name)
    
print("yeet")
#this i show you print all the instances of a class
for indiv in template_ontology.Title.instances():
    print(indiv.name)
    
    
#for row in csv file add the data to it so 

# Create a new individual
#run a for loop here 
individual_spider = template_ontology.Title("E.T.")

# Append the individual to a class
#template_ontology.Title.instances.append(individual_spider)


# Create a new individual and add it to the "Person" class
#spd = template_ontology.Individual("http://www.semanticweb.org/abdycervantes/ontologies/2023/2/ProjectOWL#Spoderman")
#spd.is_a.append(Title)

#template_ontology.save(file_path="/Users/manuelgutierrez/Desktop/dataintegration/python_data_integration_project/project/moviesssss.owl")
template_ontology.save(file="moviesssss.owl")
print("god help me")