# Title: Math Exercises
# Version: 2.0.0
# Author: Seighin Van Hoeserlande & Bo Van Achte
# Description: Simple program created to test basic mathmatical skills of the user. Created as a project for school on 09-30-2021

#TODO: Optimize?
#TODO: Fix the Timer
#TODO: btn that explains what u need to do (calculation frame)
#TODO: btn so u can switch the sound on and off
#TODO: Creating a grade level system
#TODO: Creating an option where u can choose wich excercises u do (ex. only subtractions with 7)
#TODO: Setting the focus immediatly on the entry box (calculation frame)
#TODO: reordering classes???

from random import randint
import tkinter as tk
import tkinter.font as tkFont
import winsound as ws
from time import perf_counter

global_padding = (10, 10)
    
# Defining the root window
root = tk.Tk()
root.title("Oefeningen Wiskunde v3.0.0")
root.rowconfigure(1, minsize=825, weight=1)
root.columnconfigure(1, minsize=500, weight=1)
root.resizable(width=False, height=False)

title_font = tkFont.Font(family="Arial", size=36, weight="bold", underline=True, slant="italic") # Font object used for the title

#frm home
frm_home = tk.Frame(root)
frm_home.rowconfigure(0, weight=1, minsize=175)
frm_home.rowconfigure(1, minsize=500, weight=1)
frm_home.rowconfigure(2, minsize=150, weight=1)
frm_home.columnconfigure(0, weight=1, minsize=500)
frm_home.grid(row=1, column=1, sticky="nesw")

#frm niveau
frm_niveau = tk.Frame(frm_home)
frm_niveau.grid(row=1, column=0, sticky="nesw", pady=global_padding[1])
frm_niveau.rowconfigure([0,1,2], minsize=150, weight=1)
frm_niveau.columnconfigure([0,1,2,3,4,5], minsize=100, weight=1)

#Header
lbl_title = tk.Label(frm_home, text="Oefeningen Wiskunde", bg="#0E86D4", font=title_font, fg="white") 
lbl_title.grid(row=0, column=0, columnspan=4, sticky="nesw", pady=(0, global_padding[1]*2))

#Footer
lbl_copyright = tk.Label(frm_home, text="\u00A9 2021 Seighin Van Hoeserlande & Bo Van Achte", bg="#202020", fg="white")
lbl_copyright.grid(row=2, column=0, sticky="nesw", pady=(global_padding[1]*2, 0))

#Btn Niveau 1-6
btn_grade1 = tk.Button(frm_niveau, text="1ste Leerjaar")
btn_grade1.grid(row=0, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_grade2 = tk.Button(frm_niveau, text="2de Leerjaar")
btn_grade2.grid(row=0, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_grade3 = tk.Button(frm_niveau, text="3de Leerjaar")
btn_grade3.grid(row=1, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_grade4 = tk.Button(frm_niveau, text="4de Leerjaar")
btn_grade4.grid(row=1, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_grade5 = tk.Button(frm_niveau, text="5de Leerjaar")
btn_grade5.grid(row=2, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_grade6 = tk.Button(frm_niveau, text="6de Leerjaar")
btn_grade6.grid(row=2, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

#frm grade1
frm_grade1 = tk.Frame(frm_home)
frm_grade1.grid(row=1, column=0, sticky="nesw", pady=global_padding[1])
frm_grade1.rowconfigure([0,1,2], minsize=150, weight=1)
frm_grade1.columnconfigure([0,1,2,3,4,5], minsize=100, weight=1)
frm_grade1.lower()

#btn operations grade1
btn_optellen10 = tk.Button(frm_grade1, text="Optellen tot 10")
btn_optellen10.grid(row=0, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_optellen20 = tk.Button(frm_grade1, text="Optellen tot 20")
btn_optellen20.grid(row=0, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_aftrekken10 = tk.Button(frm_grade1, text="Aftrekken tot 10")
btn_aftrekken10.grid(row=1, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_aftrekken20 = tk.Button(frm_grade1, text="Aftrekken tot 20")
btn_aftrekken20.grid(row=1, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_gemengdG1 = tk.Button(frm_grade1, text="Gemengde oefeningen")
btn_gemengdG1.grid(row=2, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_back = tk.Button(frm_grade1, text="Terug")
btn_back.grid(row=2, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

#frm grade2
frm_grade2 = tk.Frame(frm_home)
frm_grade2.grid(row=1, column=0, sticky="nesw", pady=global_padding[1])
frm_grade2.rowconfigure([0,1], minsize=150, weight=1)
frm_grade2.columnconfigure([0,1,2,3,4,5], minsize=100, weight=1)
frm_grade2.lower()

#btn operations grade2
btn_optellen100 = tk.Button(frm_grade2, text="Optellen tot 100")
btn_optellen100.grid(row=0, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_aftrekken100 = tk.Button(frm_grade2, text="Aftrekken tot 100")
btn_aftrekken100.grid(row=0, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_gemengdG2 = tk.Button(frm_grade2, text="Gemengde oefeningen")
btn_gemengdG2.grid(row=1, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_back = tk.Button(frm_grade2, text="Terug")
btn_back.grid(row=1, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

#frm grade3
frm_grade3 = tk.Frame(frm_home)
frm_grade3.grid(row=1, column=0, sticky="nesw", pady=global_padding[1])
frm_grade3.rowconfigure([0,1,2], minsize=150, weight=1)
frm_grade3.columnconfigure([0,1,2,3,4,5], minsize=100, weight=1)
#frm_grade3.lower()

#btn operations grade3
btn_vermenigvuldigenST = tk.Button(frm_grade3, text="Maaltafels 1, 2, 3, 4, 5 en 10")
btn_vermenigvuldigenST.grid(row=0, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_verdubbelen = tk.Button(frm_grade3, text="Verdubbelen, het dubbele nemen")
btn_verdubbelen.grid(row=0, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_delenST = tk.Button(frm_grade3, text="Deeltafels 1, 2, 3, 4, 5 en 10")
btn_delenST.grid(row=1, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_halveren = tk.Button(frm_grade3, text="Halveren, de helft nemen")
btn_halveren.grid(row=1, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_gemengdG3 = tk.Button(frm_grade3, text="Gemengde oefeningen")
btn_gemengdG3.grid(row=2, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_back = tk.Button(frm_grade3, text="Terug")
btn_back.grid(row=2, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

#frm grade4
frm_grade4 = tk.Frame(frm_home)
frm_grade4.grid(row=1, column=0, sticky="nesw", pady=global_padding[1])
frm_grade4.rowconfigure([0,1,2], minsize=150, weight=1)
frm_grade4.columnconfigure([0,1,2,3,4,5], minsize=100, weight=1)
frm_grade4.lower()

#frm grade5
frm_grade5 = tk.Frame(frm_home)
frm_grade5.grid(row=1, column=0, sticky="nesw", pady=global_padding[1])
frm_grade5.rowconfigure([0,1,2], minsize=150, weight=1)
frm_grade5.columnconfigure([0,1,2,3,4,5], minsize=100, weight=1)
frm_grade5.lower()

#frm grade6
frm_grade6 = tk.Frame(frm_home)
frm_grade6.grid(row=1, column=0, sticky="nesw", pady=global_padding[1])
frm_grade6.rowconfigure([0,1,2], minsize=150, weight=1)
frm_grade6.columnconfigure([0,1,2,3,4,5], minsize=100, weight=1)
frm_grade6.lower()

# Function called upon runtime as a script
def main():
    root.mainloop()  

# Only runs the script if it is run directly and not imported as an external file
if __name__ == '__main__':
    main()