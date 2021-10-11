# Title: Math Exercises
# Version: 2.0.0
# Author: Seighin Van Hoeserlande & Bo Van Achte
# Description: Simple program created to test basic mathmatical skills of the user. Created as a project for school on 09-30-2021

#TODO: Add GUI (v2.0.0)
#TODO: Optimize?

#TODO: Come up with a name? <-- For what? <-- The program. Just calling it "Wiskunde Oefeningen" doesn't really sound nice
#TODO: Stylize calculation frame
#TODO: Add footer to calculation screen and possibly a header displaying the current type of exercise?
#TODO: Check the answer if the enter key is pressed

from random import randint
import tkinter as tk
import tkinter.font as tkFont

global_padding = (10, 10)

#def check_for_stop(user_input):
#    if user_input.lower() == "stop":
#        return True
#TODO: change to btn x -> replaced with return_to_main_menu function (Remove when read plz)

# Using a class to organize methods that provide the math problems
class operations():

    @staticmethod
    def addition():
        a,b = randint(0,9), randint(0,9)
        lbl_specified_exercise.configure(text=f"{a} + {b} = ")
        return a+b

    @staticmethod
    def subtraction():
        a,b = randint(0,9), randint(0,9)
        while a<b:
            a,b = randint(0,9), randint(0,9)
        lbl_specified_exercise.configure(text=f"{a} - {b} = ")
        return a-b
    
    @staticmethod
    def multiplication():
        a,b = randint(0,9), randint(0,9)
        lbl_specified_exercise.configure(text=f"{a} x {b} = ")
        return a*b

    @staticmethod
    def division():
        a,b = randint(0,10), randint(1,10)
        lbl_specified_exercise.configure(text=f"{a*b} ÷ {b} = ") # Utilizing Bo's method to prevent decimals
        return (a*b)/b

    @staticmethod
    def mixed_problems():
        input_option_dict = {1 : operations.addition, 2: operations.subtraction, 3: operations.multiplication, 4: operations.division, 5: operations.mixed_problems}
        return input_option_dict[randint(1,5)]()


# Defines needed variables and calls the corresponding functions
def game_loop(operation):
    """Defines needed variables and calls the corresponding functions."""
    global correct_answer
    global current_operation
    frm_calculation.lift() # Makes the exercise visible
    current_operation = operation
    correct_answer = operation()

# Using a class to organize methods that handle user actions
class handlers:
    
    # Called when the "check_answer" button is pressed
    @staticmethod
    def check_button_handler():
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
            ent_answer_space.insert(0, "Enkel nummers zijn toegestaan") #* Is there a better way to warn the user?

    # Called when the "end_calculations" button is pressed
    @staticmethod
    def return_to_main_menu():
        """Returns to main menu and resets the calculation screen"""
        frm_calculation.lower() # Hides calculation screen
        # Resets calculation screen
        lbl_wrong_answer.configure(text="")
        counters.reset()
        lbl_count_right.configure(text=f"Juist: {counters.amount_correct}")
        lbl_count_wrong.configure(text=f"Fout: {counters.amount_wrong}")

# A simple class to eliminate the need of global variables and group similar methods related to the counters
class counters:

    amount_wrong, amount_correct = 0, 0

    def reset():
        counters.amount_wrong, counters.amount_correct = 0, 0
    
    def increase_correct_count():
        counters.amount_correct +=1
    
    def increase_wrong_count():
        counters.amount_wrong +=1

# Defining the root window
root = tk.Tk()
root.title("Wiskunde Oefeningen v2.0.0")
root.rowconfigure(1, minsize=825, weight=1)
root.columnconfigure(1, minsize=500, weight=1)
root.resizable(width=False, height=False)

title_font = tkFont.Font(family="Arial", size=36, weight="bold", underline=True, slant="italic") # Font object used for the title

# Frame containing the main menu widgets
frm_home = tk.Frame(root)
frm_home.rowconfigure(0, weight=1, minsize=175)
frm_home.rowconfigure(1, minsize=500, weight=1)
frm_home.rowconfigure(2, minsize=150, weight=1)
frm_home.columnconfigure(0, weight=1, minsize=500)
frm_home.grid(row=1, column=1, sticky="nesw")

# Creating frame for the menu
frm_menu = tk.Frame(frm_home) #frm == frame
frm_menu.grid(row=1, column=0, sticky="nesw", pady=global_padding[1])
frm_menu.rowconfigure([0,1,2], minsize=150, weight=1)
frm_menu.columnconfigure([0,1,2,3,4,5], minsize=100, weight=1)

# Creating header
lbl_title = tk.Label(frm_home, text="Wiskunde Oefeningen", bg="#0E86D4", font=title_font, fg="white") 
lbl_title.grid(row=0, column=0, sticky="nesw", pady=(0, global_padding[1]*2))

# Creating addition button
btn_addition = tk.Button(frm_menu, text="Optellen", command=lambda: game_loop(operations.addition))
btn_addition.grid(row=0, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

# Creating subtraction button
btn_subtraction = tk.Button(frm_menu, text="Aftrekken", command=lambda: game_loop(operations.subtraction))
btn_subtraction.grid(row=0, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

# Creating multiplication button
btn_multiplication = tk.Button(frm_menu, text="Vermenigvuldigen", command=lambda: game_loop(operations.multiplication))
btn_multiplication.grid(row=1, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

# Creating division button
btn_division = tk.Button(frm_menu, text="Delen", command=lambda: game_loop(operations.division))
btn_division.grid(row=1, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

# Creating mixed_problems button
btn_mixed_problems = tk.Button(frm_menu, text="Gemengde Problemen", command=lambda: game_loop(operations.mixed_problems))
btn_mixed_problems.grid(row=2, column=1, columnspan=4, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

# Creating footer
lbl_copyright = tk.Label(frm_home, text="\u00A9 2021 Seighin Van Hoeserlande & Bo Van Achte", bg="#202020", fg="white")
lbl_copyright.grid(row=2, column=0, sticky="nesw", pady=(global_padding[1]*2, 0))

# Creating calculation frame
frm_calculation = tk.Frame(root)
frm_calculation.rowconfigure([0,1,2,3,4], minsize=100, weight=1)
frm_calculation.columnconfigure([0,1,2,3], minsize=100, weight=1)
frm_calculation.grid(row=1, column=1, sticky="nesw")
frm_calculation.lower() # Hides frame initially

# Creating end_calculations button
btn_end_calculations = tk.Button(frm_calculation, text="Terug naar menu", command=handlers.return_to_main_menu)
btn_end_calculations.grid(row=0, column=3, sticky="nesw", padx= global_padding[1], pady=global_padding[1])

# Creating count_right and count_wrong labels
lbl_count_right = tk.Label(frm_calculation, text="Juist: 0", fg="dark green")
lbl_count_right.grid(row=1, column=0, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

lbl_count_wrong = tk.Label(frm_calculation, text="Fout: 0", fg="dark red")
lbl_count_wrong.grid(row=1, column=1, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

# Creating specified_exercise label and ent_answer_space entry box
lbl_specified_exercise =tk.Label(frm_calculation)
lbl_specified_exercise.grid(row=2, column=0, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

ent_answer_space = tk.Entry(frm_calculation)
ent_answer_space.grid(row=2, column=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

# Creating check_answer button
btn_check_answer = tk.Button(frm_calculation, text="Controleer het antwoord", command=handlers.check_button_handler)
btn_check_answer.grid(row=3, column=0, columnspan=3, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

# Creating wrong_answer label
lbl_wrong_answer = tk.Label(frm_calculation, fg="red")
lbl_wrong_answer.grid(row=4, column=0, columnspan=3, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

# Function called upon runtime as a script
def main():
    root.mainloop()  

# Only runs the script if it is run directly and not imported as an external file
if __name__ == '__main__':
    main()