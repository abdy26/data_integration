#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:17:19 2023

@author: manuelgutierrez
"""

from owlready2 import *
import pandas as pd


onto_path.append("./data_project.owl")
template_ontology = get_ontology('data_project.owl').load()


def getInstances():
    print("Ontology IRI:", template_ontology.base_iri)
    print(template_ontology.Movie)
    
    #this is how to get data from there
    for individual in template_ontology.individuals():
        print(individual.name)
        
    print("--------------------------------------------------------------------------------------")
    for indiv in template_ontology.Movie.instances():
        print(indiv.name)
    print("--------------------------------------------------------------------------------------")


def printRowData():
    file_path = 'book4.xlsx'
    df = pd.read_excel(file_path)
    first_two_rows_loc = df.loc[0]
    print(first_two_rows_loc)
    
    #get the title
    
    for row in range(29):
        rows_loc = df.loc[row]
        
        #gets the title
        first_element = rows_loc['original_title']
        second_element = rows_loc['original_language']
        third_element = rows_loc['budget']
        fourth_element = rows_loc['country']
        fifth_element = rows_loc['production_co']
        six_element = rows_loc['cast'] # this needs to be seperated later 
        seven_element = rows_loc['writer'] #this has to be split too 
        eight_element = rows_loc['director']
        nine_element = rows_loc['producer']
        ten_element = rows_loc['critic_score']
        eleven_element = rows_loc['people_score']
        twelve_element = rows_loc['overview']
        thirteen_element = rows_loc['consensus']
        
        print('First element of the first row:', first_element)
        
        #add to instances
        movie_instances = template_ontology.Movie(first_element)
        movie_instances.movie_title.append(first_element)
        movie_instances.movie_budget.append(int(third_element))
        movie_instances.movie_public_score.append(int(eleven_element))
        movie_instances.movie_critic_score.append(int(ten_element))
        movie_instances.movie_overview.append(twelve_element)
        movie_instances.movie_concensus.append(thirteen_element)
    
        template_ontology.save(file="mdata_project.owl")
    #for ind in first_two_rows_loc:
    #    print(ind)
    #print(first_two_rows_loc.loc[0])
    
    
        


#for row in csv file add the data to it so 
# Create a new individual
#run a for loop here 
#individual_spider = template_ontology.Title("E.T.")

# Append the individual to a class
#template_ontology.Title.instances.append(individual_spider)


# Create a new individual and add it to the "Person" class
#spd = template_ontology.Individual("http://www.semanticweb.org/abdycervantes/ontologies/2023/2/ProjectOWL#Spoderman")
#spd.is_a.append(Title)

#template_ontology.save(file_path="/Users/manuelgutierrez/Desktop/dataintegration/python_data_integration_project/project/moviesssss.owl")
print("god help me")

printRowData()