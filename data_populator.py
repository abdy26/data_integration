#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:17:19 2023

@author: manuelgutierrez
"""

from owlready2 import *
import pandas as pd

template_ontology = get_ontology('data_project.owl').load()

def printRowData():
    file_path = 'book4.xlsx'
    df = pd.read_excel(file_path)
    first_two_rows_loc = df.loc[0]
    print(first_two_rows_loc)
    
    #get the title
    
    #get the language 
    en_instance = template_ontology.Language('en')
    ko_instance = template_ontology.Language('ko')
    
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
    
        #instance add 
        movie_instances.hasLanguage.append(en_instance)
        

        #make individuals contry
        list_of_contrys = fourth_element.split(',')
        for contry in list_of_contrys: 
            print("addint contry", contry)
            contry_instance = template_ontology.Contry(contry)
            movie_instances.hasContry.append(contry_instance)
            template_ontology.save(file="data_project.owl")
        
        #make individuals contry
        list_of_production_companies = fifth_element.split(',')
        for production_co in list_of_production_companies: 
            print("addint production company", production_co)
            production_co_instance = template_ontology.Production_CO(production_co)
            #adds hasProductionCO to the movie instance 
            movie_instances.hasProductionCO.append(production_co_instance)
            template_ontology.save(file="data_project.owl")
        
        
        #make individuals actor
        list_of_actors = six_element.split(',')
        for actor in list_of_actors: 
            print("added actor",actor)
            actor_instance = template_ontology.Actor(actor)
            #add has actors to a movie
            movie_instances.hasActor.append(actor_instance)
            template_ontology.save(file="data_project.owl")
            
            
        #make individuals writer
        list_of_writers = seven_element.split(',')
        for writer in list_of_writers: 
            print("added actor",writer)
            writer_instance = template_ontology.Writer(writer)
            #add has actors to a movie
            movie_instances.hasWriter.append(writer_instance)
            template_ontology.save(file="data_project.owl")
        
        
        #make individuals Directors
        list_of_Directos = eight_element.split(',')
        for director in list_of_Directos: 
            print("added actor", director)
            director_instance = template_ontology.Director(director)
            #add has director to a movie
            movie_instances.hasDirector.append(director_instance)
            template_ontology.save(file="data_project.owl")
            
        
        #make individuals Directors
        list_of_producer = nine_element.split(',')
        for producer in list_of_producer: 
            print("added actor", director)
            producer_instance = template_ontology.Producer(producer)
            #add has director to a movie
            movie_instances.hasProducer.append(producer_instance )
            template_ontology.save(file="data_project.owl")

        
                       
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