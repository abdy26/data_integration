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

##show all directors in the datasets
directors = onto.search(is_a = onto.Director)
directorsList= list(directors)

# print(list(default_world.sparql_query("""
#            PREFIX example: http://www.semanticweb.org/manuelgutierrez/ontologies/2023/3/project
#            SELECT ?movie 
#            WHERE {
#                 ?movie rdf:type example:Movie .
#                 ?movie example:hasBudget ?budget .
#             FILTER (?budget <= 200000000)
  
#            }
#     """)))

first_query = list(default_world.sparql("""
            SELECT ?movie
            WHERE {
              ?movie rdf:type data_project:Movie .
              ?movie data_project:movie_public_score ?public_score .
              ?movie data_project:movie_critic_score ?people_score .
              FILTER (?public_score > 70 && ?people_score > 70)
            }
        """))
        

second_query = list(default_world.sparql("""
            SELECT ?director
            WHERE {
                ?director rdf:type data_project:Director .
            }
        """))
        
third_query = list(default_world.sparql("""
            SELECT ?movie
            WHERE {
                ?movie rdf:type data_project:Movie .
                ?movie data_project:movie_public_score ?public_score .
                ?movie data_project:movie_budget ?budget_score .
                FILTER (?public_score > 75 && ?budget_score > 100000000)
            }
        """))
print(third_query)


root=tk.Tk()
 
# setting the windows size
root.geometry("600x400")
  
# declaring string variable
# for storing name 
name_var=tk.StringVar()
budget_var=tk.StringVar()
 
  
# defining a function that will
# get the name 
# print them on the screen
def submit():
 
    name=name_var.get()
     
    print("The name is : " + name)
     
    name_var.set("")

def onClick():
   
        tkinter.messagebox.showinfo("Welcome to GFG.",  second_query) 

def onClick2():
        tkinter.messagebox.showinfo("Welcome to GFG.",  first_query) 

        
     
# creating a label
name_label = tk.Label(root, text = 'Movie Name', font=('calibre',10, 'bold'))
# Create a Button
button = Button(root, text="Show Directors", command=onClick, height=2, width=8) 
query1Button = Button(root, text="public score and a critic score of 70 or above", command=onClick2, height=2, width=8) 


  
# creating a entry for input
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
    
# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)
  
# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
sub_btn.grid(row=2,column=1)
button.grid(row=6,column=0)
query1Button.grid(row=8,column=0)

  
# performing an infinite loop
# for the window to display
root.mainloop()



