import tkinter as tk
from owlready2 import *
from owlready2 import sync_reasoner
from rdflib.plugins.sparql import prepareQuery
from tkinter import * 
import tkinter.messagebox
    
onto_path.append("./data_project.owl")
onto = get_ontology('data_project.owl').load()

##try loading into tkinter window with label 
onto.load()

root=tk.Tk()
 
# setting the windows size
root.geometry("600x400")
  
# declaring string variable
# for storing name 
name_var=tk.StringVar()

def onClick():
   
        tkinter.messagebox.showinfo("Welcome to GFG.",  print_query_format(second_query())) 

def onClick2():
        tkinter.messagebox.showinfo("Welcome to GFG.",  print_query_format(first_query())) 
        
def onClick3():
        tkinter.messagebox.showinfo("Welcome to GFG.",  print_query_format(third_query())) 
        
def onClick4():
        tkinter.messagebox.showinfo("Welcome to GFG.",  print_query_format(fourth_query()))
        
        


def first_query():
    first_query = list(default_world.sparql("""
                SELECT ?movie
                WHERE {
                  ?movie rdf:type data_project:Movie .
                  ?movie data_project:movie_public_score ?public_score .
                  ?movie data_project:movie_critic_score ?people_score .
                  FILTER (?public_score > 70 && ?people_score > 70)
                }
            """))
    return first_query


def second_query(): 
    second_query = list(default_world.sparql("""
                SELECT ?director
                WHERE {
                    ?director rdf:type data_project:Director .
                }
            """))
    return second_query

def third_query():
        
    third_query = list(default_world.sparql("""
                SELECT ?movie
                WHERE {
                    ?movie rdf:type data_project:Movie .
                    ?movie data_project:movie_public_score ?public_score .
                    ?movie data_project:movie_budget ?budget_score .
                    FILTER (?public_score > 75 && ?budget_score > 100000000)
                }
            """))
    return third_query
        
        
def fourth_query():
    fourth_query = list(default_world.sparql("""
                SELECT ?director

                WHERE {
                    ?director rdf:type data_project:Director .

                    ?movie data_project:movie_critic_score ?critic_score .

                    FILTER (?critic_score > 70)
                }
            """))
    return fourth_query
    
    
def print_query_format(query):
    
    format_str = ""
    for i in range(len(query)):
        print(query[i][0].name)
        format_str = format_str + "," + query[i][0].name
        ##print("this is format name so far", format_str)
        
    return format_str
        

if __name__ == '__main__':
    
    print(print_query_format(fourth_query()))

        
     
# creating a label
# Create a Button
directorsLabel = tk.Label(root, text = 'All directors', font=('calibre',15, 'bold'))
button = Button(root, text="Show Directors", command=onClick, height=2, width=8) 

query1Label = tk.Label(root, text = 'What movies have a public score and a critic score of 70 or above ?', font=('calibre',15, 'bold'))
query1Button = Button(root, text="Click here", command=onClick2, height=2, width=10)

query3Label = tk.Label(root, text = 'What movies have a public score over 75 and a budget over 100 M?', font=('calibre',15, 'bold'))
query3Button = Button(root, text="Click here", command=onClick3, height=2, width=10) 

query4Label = tk.Label(root, text = 'What directors have movies with a critic score 70 or above?', font=('calibre',15, 'bold'))
query4Button = Button(root, text="Click here", command=onClick4, height=2, width=10) 
 

  
# grid method
directorsLabel.grid(row=5,column=0)
button.grid(row=6,column=0)
query1Label.grid(row=7, column=0)
query1Button.grid(row=8,column=0)
query3Label.grid(row=9, column=0)
query3Button.grid(row=10,column=0)
query4Label.grid(row=11, column=0)
query4Button.grid(row=12,column=0)


  
# performing an infinite loop
# for the window to display
root.mainloop()





