import tkinter as tk
  
root=tk.Tk()
 
# setting the windows size
root.geometry("600x400")
  
# declaring string variable
# for storing name 
name_var=tk.StringVar()
passw_var=tk.StringVar()
 
  
# defining a function that will
# get the name 
# print them on the screen
def submit():
 
    name=name_var.get()
     
    print("The name is : " + name)
     
    name_var.set("")
     
     
# creating a label for
# name using widget Label
name_label = tk.Label(root, text = 'Movie Name', font=('calibre',10, 'bold'))
  
# creating a entry for input
# name using widget Entry
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
  
# performing an infinite loop
# for the window to display
root.mainloop()
