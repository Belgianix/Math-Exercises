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
# Using a class to organize methods that provide the math problems
class operations():
    "Decorative class used to group respective methods visually"

    @staticmethod
    def addition() -> int:
        "Adds two random integers and returns the sum"
        a,b = randint(0,9), randint(0,9)
        lbl_specified_exercise.configure(text=f"{a} + {b} = ")
        return a+b

    @staticmethod
    def subtraction() -> int:
        "Subtracts two random integers and returns the difference"
        a,b = randint(0,9), randint(0,9)
        while a<b:
            a,b = randint(0,9), randint(0,9)
        lbl_specified_exercise.configure(text=f"{a} - {b} = ")
        return a-b
    
    @staticmethod
    def multiplication() -> int:
        "Multiplies two random integers and returns the product"
        a,b = randint(0,9), randint(0,9)
        lbl_specified_exercise.configure(text=f"{a} x {b} = ")
        return a*b

    @staticmethod
    def division() -> int:
        "Divides two random integers and returns the quotient"
        a,b = randint(0,10), randint(1,10)
        lbl_specified_exercise.configure(text=f"{a*b} : {b} = ")
        return (a*b)/b

    @staticmethod
    def mixed_problems():
        "Calls a random operation method and returns its output"
        input_option_dict = {1 : operations.addition, 2: operations.subtraction, 3: operations.multiplication, 4: operations.division, 5: operations.mixed_problems}
        return input_option_dict[randint(1,5)]()
    
#! WIP!!!

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self, countdown_time):
        self.countdown_time = countdown_time

    def start(self):
        """Start a new timer"""
        if self.countdown_time is not None:
            raise TimerError("Timer is running. Use .stop() to stop it")

        self._start_time = perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError("Timer is not running. Use .start() to start it")

        elapsed_time = perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.2f} seconds")

t = Timer(5)



# Sets the title on the calculation screen
def title_set(name: str):
    lbl_title_calculation.configure(text=name)

# Defines needed variables and calls the corresponding functions
def game_loop(operation, operation_str:str=None):
    "Defines needed variables and calls the corresponding functions."
    global correct_answer
    global current_operation
    frm_calculation.lift() # Makes the exercise visible
    if operation_str != None:
        title_set(operation_str)
    current_operation = operation
    correct_answer = operation()

# Using a class to organize methods that handle user actions
class handlers:
    
    # Called when the "check_answer" button is pressed
    @staticmethod
    def check_button_handler(event=None):
        "Checks if the answer is correct, updates counters accordingly and reruns the gameloop function"
        try:
            user_input = int(ent_answer_space.get()) # Checks if the inputted answer is an integer
            lbl_wrong_answer.configure(text="")
            if correct_answer == user_input: # Checks if the answer is correct or not and updates the counters accordingly
                counters.increase_correct_count()
                lbl_count_right.configure(text=f"Juist: {counters.amount_correct}")
            else:
                counters.increase_wrong_count()
                lbl_count_wrong.configure(text=f"Fout: {counters.amount_wrong}")
                lbl_wrong_answer.configure(text=f"Het juiste antwoord was {int(correct_answer)}")
            ent_answer_space.delete(0, "end") # Clears entry box
            game_loop(current_operation)
        except ValueError: # Warns user that only numbers are permitted
                lbl_wrong_answer.configure(text="Alleen nummers zijn toegestaan!")
                ent_answer_space.delete(0, "end") # Clears entry box

    # Called when the "end_calculations" button is pressed
    @staticmethod
    def return_to_main_menu():
        "Returns to main menu and resets the calculation screen"
        t.stop()
        frm_calculation.lower() # Hides calculation screen
        # Resets calculation screen
        lbl_wrong_answer.configure(text="")
        counters.reset()
        lbl_count_right.configure(text=f"Juist: {counters.amount_correct}")
        lbl_count_wrong.configure(text=f"Fout: {counters.amount_wrong}")
        root.focus() # Prevents the entry box from receiving input while in the menu screen

def SoundEffect(RandInt):
    """
    Plays sound effect when called. Numbers under 3 will play a random "correct" effect sound while
    anything above 3 will result in a random "wrong" sound effect
    """
    sounds = {1:'Sound1Correct.wav', 2:'Sound2Correct.wav', 3:'Sound3Correct.wav', 4:"Sound4Wrong.wav"}
    ws.PlaySound("Sound Effects\\" + sounds[RandInt], ws.SND_FILENAME)

class counters:
    """
    A simple class to eliminate the need of global variables and group similar methods related to
    the counters
    """

    amount_wrong, amount_correct = 0, 0

    def reset():
        "Resets counters on calculation screen"
        counters.amount_wrong, counters.amount_correct = 0, 0
    
    def increase_correct_count():
        "Increases correct counter by one on calculation screen"
        counters.amount_correct +=1
        SoundEffect(randint(1,3))
    
    def increase_wrong_count():
        "Decreases correct counter by one on calculation screen"
        counters.amount_wrong +=1
        SoundEffect(4)

#Changing frm
class changeFrm:
    @staticmethod
    def toFrmGrade1():
        frm_niveau.lower()
        frm_grade1.lift()
    @staticmethod
    def toFrmGrade2():
        frm_niveau.lower()
        frm_grade2.lift()
    @staticmethod
    def toFrmGrade3():
        frm_niveau.lower()
        frm_grade3.lift()
    @staticmethod
    def toFrmGrade4():
        frm_niveau.lower()
        frm_grade4.lift()
    @staticmethod
    def toFrmGrade5():
        frm_niveau.lower()
        frm_grade5.lift()
    @staticmethod
    def toFrmGrade6():
        frm_niveau.lower()
        frm_grade6.lift()
    @staticmethod
    def toFrmNiveaus():
        frm_niveau.lift()
        frm_grade1.lower()
        frm_grade2.lower()
        frm_grade3.lower()
        frm_grade4.lower()
        frm_grade5.lower()
        frm_grade6.lower()
    
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
btn_grade1 = tk.Button(frm_niveau, text="1ste Leerjaar", command=changeFrm.toFrmGrade1)
btn_grade1.grid(row=0, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_grade2 = tk.Button(frm_niveau, text="2de Leerjaar", command=changeFrm.toFrmGrade2)
btn_grade2.grid(row=0, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_grade3 = tk.Button(frm_niveau, text="3de Leerjaar", command=changeFrm.toFrmGrade3)
btn_grade3.grid(row=1, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_grade4 = tk.Button(frm_niveau, text="4de Leerjaar", command=changeFrm.toFrmGrade4)
btn_grade4.grid(row=1, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_grade5 = tk.Button(frm_niveau, text="5de Leerjaar", command=changeFrm.toFrmGrade5)
btn_grade5.grid(row=2, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_grade6 = tk.Button(frm_niveau, text="6de Leerjaar", command=changeFrm.toFrmGrade6)
btn_grade6.grid(row=2, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

#frm grade1
frm_grade1 = tk.Frame(frm_home)
frm_grade1.grid(row=1, column=0, sticky="nesw", pady=global_padding[1])
frm_grade1.rowconfigure([0,1,2], minsize=150, weight=1)
frm_grade1.columnconfigure([0,1,2,3,4,5], minsize=100, weight=1)
frm_grade1.lower()

#btn operations grade1
btn_optellen10 = tk.Button(frm_grade1, text="Optellen tot 10", command=lambda: game_loop(operations.addition, "Optellen"))
btn_optellen10.grid(row=0, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_optellen20 = tk.Button(frm_grade1, text="Optellen tot 20", command=lambda: game_loop(operations.addition, "Optellen"))
btn_optellen20.grid(row=0, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_aftrekken10 = tk.Button(frm_grade1, text="Aftrekken tot 10", command=lambda: game_loop(operations.subtraction, "Aftrekken"))
btn_aftrekken10.grid(row=1, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_aftrekken20 = tk.Button(frm_grade1, text="Aftrekken tot 20", command=lambda: game_loop(operations.subtraction, "Aftrekken"))
btn_aftrekken20.grid(row=1, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_gemengdG1 = tk.Button(frm_grade1, text="Gemengde oefeningen", command=lambda: game_loop(operations.mixed_problems, "Gemengde Oefeningen"))
btn_gemengdG1.grid(row=2, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_back = tk.Button(frm_grade1, text="Terug", command=changeFrm.toFrmNiveaus)
btn_back.grid(row=2, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

#frm grade2
frm_grade2 = tk.Frame(frm_home)
frm_grade2.grid(row=1, column=0, sticky="nesw", pady=global_padding[1])
frm_grade2.rowconfigure([0,1], minsize=150, weight=1)
frm_grade2.columnconfigure([0,1,2,3,4,5], minsize=100, weight=1)
frm_grade2.lower()

#btn operations grade2
btn_optellen100 = tk.Button(frm_grade2, text="Optellen tot 100", command=lambda: game_loop(operations.addition, "Optellen"))
btn_optellen100.grid(row=0, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_aftrekken100 = tk.Button(frm_grade2, text="Aftrekken tot 100", command=lambda: game_loop(operations.subtraction, "Aftrekken"))
btn_aftrekken100.grid(row=0, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_gemengdG2 = tk.Button(frm_grade2, text="Gemengde oefeningen", command=lambda: game_loop(operations.mixed_problems, "Gemengde Oefeningen"))
btn_gemengdG2.grid(row=1, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_back = tk.Button(frm_grade2, text="Terug", command=changeFrm.toFrmNiveaus)
btn_back.grid(row=1, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

#frm grade3
frm_grade3 = tk.Frame(frm_home)
frm_grade3.grid(row=1, column=0, sticky="nesw", pady=global_padding[1])
frm_grade3.rowconfigure([0,1,2], minsize=150, weight=1)
frm_grade3.columnconfigure([0,1,2,3,4,5], minsize=100, weight=1)
frm_grade3.lower()

#btn operations grade3
btn_vermenigvuldigenST = tk.Button(frm_grade3, text="Maaltafels 1, 2, 3, 4, 5 en 10", command=lambda: game_loop(operations.multiplication, "Vermenigvuldigen"))
btn_vermenigvuldigenST.grid(row=0, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_verdubbelen = tk.Button(frm_grade3, text="Verdubbelen, het dubbele nemen", command=lambda: game_loop(operations.multiplication, "Vermenigvuldigen"))
btn_verdubbelen.grid(row=0, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_delenST = tk.Button(frm_grade3, text="Deeltafels 1, 2, 3, 4, 5 en 10", command=lambda: game_loop(operations.division, "Delen"))
btn_delenST.grid(row=1, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_halveren = tk.Button(frm_grade3, text="Halveren, de helft nemen", command=lambda: game_loop(operations.division, "Delen"))
btn_halveren.grid(row=1, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_gemengdG3 = tk.Button(frm_grade3, text="Gemengde oefeningen", command=lambda: game_loop(operations.mixed_problems, "Gemengde Oefeningen"))
btn_gemengdG3.grid(row=2, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_back = tk.Button(frm_grade3, text="Terug", command=changeFrm.toFrmNiveaus)
btn_back.grid(row=2, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

#frm grade4
frm_grade4 = tk.Frame(frm_home)
frm_grade4.grid(row=1, column=0, sticky="nesw", pady=global_padding[1])
frm_grade4.rowconfigure([0,1,2,3], minsize=150, weight=1)
frm_grade4.columnconfigure([0,1,2,3,4,5], minsize=100, weight=1)
frm_grade4.lower()

#btn operations grade4
btn_optellenKomma = tk.Button(frm_grade4, text="Optellen van eenvoudige kommagetalen", command=lambda: game_loop(operations.addition, "Optellen"))
btn_optellenKomma.grid(row=0, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_optellenGBreuken = tk.Button(frm_grade4, text="Optellen van gelijknamige breuken", command=lambda: game_loop(operations.addition, "Optellen"))
btn_optellenGBreuken.grid(row=0, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_aftrekkenKomma = tk.Button(frm_grade4, text="Aftrekken van eenvoudige kommagetalen", command=lambda: game_loop(operations.subtraction, "Aftrekken"))
btn_aftrekkenKomma.grid(row=1, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_aftrekkenGBreuken = tk.Button(frm_grade4, text="Aftrekken van gelijknamige breuken", command=lambda: game_loop(operations.subtraction, "Aftrekken"))
btn_aftrekkenGBreuken.grid(row=1, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_vermenigvuldigenMT = tk.Button(frm_grade4, text="Maaltafels 6, 7, 8, 9, 10, 100, 1000 en 10000", command=lambda: game_loop(operations.multiplication, "Vermenigvuldigen"))
btn_vermenigvuldigenMT.grid(row=2, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_delenMT = tk.Button(frm_grade4, text="Deeltafels 6, 7, 8, 9, 10, 100, 1000 en 10000", command=lambda: game_loop(operations.division, "Delen"))
btn_delenMT.grid(row=2, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_gemengdG4 = tk.Button(frm_grade4, text="Gemengde oefeningen", command=lambda: game_loop(operations.mixed_problems, "Gemengde Oefeningen"))
btn_gemengdG4.grid(row=3, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_back = tk.Button(frm_grade4, text="Terug", command=changeFrm.toFrmNiveaus)
btn_back.grid(row=3, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

#frm grade5
frm_grade5 = tk.Frame(frm_home)
frm_grade5.grid(row=1, column=0, sticky="nesw", pady=global_padding[1])
frm_grade5.rowconfigure([0,1,2,3], minsize=150, weight=1)
frm_grade5.columnconfigure([0,1,2,3,4], minsize=100, weight=1)
frm_grade5.lower()

#btn operations grade4
btn_optellenOGBreuken = tk.Button(frm_grade5, text="Optellen OG breuken", command=lambda: game_loop(operations.addition, "Optellen"))
btn_optellenOGBreuken.grid(row=0, column=1, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_aftrekkenOGBreuken = tk.Button(frm_grade5, text="Aftrekken OG breuken", command=lambda: game_loop(operations.subtraction, "Aftrekken"))
btn_aftrekkenOGBreuken.grid(row=0, column=2,  sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_Vermenigvuldigen50 = tk.Button(frm_grade5, text="Maaltafels 5, 50", command=lambda: game_loop(operations.multiplication, "Vermenigvuldigen"))
btn_Vermenigvuldigen50.grid(row=0, column=3, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_VermenigvuldigenBreuken = tk.Button(frm_grade5, text="Maal breuken", command=lambda: game_loop(operations.multiplication, "Vermenigvuldigen"))
btn_VermenigvuldigenBreuken.grid(row=1, column=1, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_VermenigvuldigenKomma = tk.Button(frm_grade5, text="Maal kommagetallen", command=lambda: game_loop(operations.multiplication, "Vermenigvuldigen"))
btn_VermenigvuldigenKomma.grid(row=1, column=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_Delen50 = tk.Button(frm_grade5, text="Deeltafels 5, 50", command=lambda: game_loop(operations.division, "Delen"))
btn_Delen50.grid(row=1, column=3, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_Delenbreuken = tk.Button(frm_grade5, text="Delen breuken", command=lambda: game_loop(operations.division, "Delen"))
btn_Delenbreuken.grid(row=2, column=1, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_DelenKomma = tk.Button(frm_grade5, text="Delen kommagetallen", command=lambda: game_loop(operations.division, "Delen"))
btn_DelenKomma.grid(row=2, column=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_gemengdG5 = tk.Button(frm_grade5, text="Gemengde oefeningen", command=lambda: game_loop(operations.mixed_problems, "Gemengde Oefeningen"))
btn_gemengdG5.grid(row=2, column=3, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_back = tk.Button(frm_grade5, text="Terug", command=changeFrm.toFrmNiveaus)
btn_back.grid(row=3, column=1, columnspan=3, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

#frm grade6
frm_grade6 = tk.Frame(frm_home)
frm_grade6.grid(row=1, column=0, sticky="nesw", pady=global_padding[1])
frm_grade6.rowconfigure([0,1], minsize=150, weight=1)
frm_grade6.columnconfigure([0,1,2,3,4,5], minsize=100, weight=1)
frm_grade6.lower()

#btn operations grade6
btn_VermenigvuldigenKommaKomma = tk.Button(frm_grade6, text="Kommagetal maal kommagetal", command=lambda: game_loop(operations.multiplication, "Vermenigvuldigen"))
btn_VermenigvuldigenKommaKomma.grid(row=0, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_DelenKommaKomma = tk.Button(frm_grade6, text="Kommagetal delen door kommagetal", command=lambda: game_loop(operations.division, "Delen"))
btn_DelenKommaKomma.grid(row=0, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_gemengdG6 = tk.Button(frm_grade6, text="Gemengde oefeningen", command=lambda: game_loop(operations.mixed_problems, "Gemengde Oefeningen"))
btn_gemengdG6.grid(row=1, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_back = tk.Button(frm_grade6, text="Terug", command=changeFrm.toFrmNiveaus)
btn_back.grid(row=1, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

# Creating calculation frame
frm_calculation = tk.Frame(root)
frm_calculation.rowconfigure([0,1,2,3,4,5], minsize=100, weight=1)
frm_calculation.rowconfigure(0, weight=1, minsize=175)
frm_calculation.rowconfigure(5, minsize=150, weight=1)
frm_calculation.columnconfigure([0,1,2,3], minsize=100, weight=1)
frm_calculation.grid(row=1, column=1, sticky="nesw")
frm_calculation.lower()

# Creating header
lbl_title_calculation = tk.Label(frm_calculation, text="Oefeningen Wiskunde", bg="#0E86D4", font=title_font, fg="white") 
lbl_title_calculation.grid(row=0, column=0, columnspan=5, sticky="nesw", pady=(0, global_padding[1]*2))

# Creating end_calculations button
btn_end_calculations = tk.Button(frm_calculation, text="Terug", command=handlers.return_to_main_menu, width=10, height=3)
btn_end_calculations.grid(row=1, column=3, sticky="ne", padx= global_padding[1], pady=global_padding[1])

# Creating specified_exercise label, ent_answer_space entry box and check_answer btn
lbl_specified_exercise =tk.Label(frm_calculation, font=("Arial",30))
lbl_specified_exercise.grid(row=2, column=0, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

ent_answer_space = tk.Entry(frm_calculation, borderwidth= 3, relief="groove",font=("Arial", 25), width=5)
ent_answer_space.grid(row=2, column=2, sticky="ns", padx= global_padding[0], pady=global_padding[1])

#add photoimage
photo = tk.PhotoImage(file="btn.png")
btn_check_answer = tk.Button(frm_calculation, borderwidth= 0, image = photo, border=None, command=handlers.check_button_handler)
btn_check_answer.grid(row=2, column=3, padx= global_padding[0], pady=global_padding[1])

# Creating wrong_answer label
lbl_wrong_answer = tk.Label(frm_calculation, fg="red", font=("Arial", 15))
lbl_wrong_answer.grid(row=3, column=0, columnspan=4, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

# Creating count_right and count_wrong labels
lbl_count_right = tk.Label(frm_calculation, text="Juist: 0", fg="dark green", bg="DarkOliveGreen1", borderwidth=1, relief="sunken")
lbl_count_right.grid(row=4, column=0,columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

lbl_count_wrong = tk.Label(frm_calculation, text="Fout: 0", fg="dark red", bg="Indianred1", borderwidth=1, relief="sunken")
lbl_count_wrong.grid(row=4, column=2,columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

# Creating footer
lbl_copyright = tk.Label(frm_calculation, text="\u00A9 2021 Seighin Van Hoeserlande & Bo Van Achte", bg="#202020", fg="white")
lbl_copyright.grid(row=5, column=0, columnspan=5, sticky="nesw", pady=(global_padding[1]*2, 0))

ent_answer_space.bind("<Return>", handlers.check_button_handler)


# Function called upon runtime as a script
def main():
    root.mainloop()  

# Only runs the script if it is run directly and not imported as an external file
if __name__ == '__main__':
    main()