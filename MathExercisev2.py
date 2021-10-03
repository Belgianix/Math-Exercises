# Title: Math Exercises
# Version: 2.0.0
# Author: Seighin Van Hoeserlande & Bo Van Achte
# Description: Simple program created to test basic mathmatical skills of the user. Created as a project for school on 09-30-2021

#TODO: Add GUI (v2.0.0)
#TODO: Optimize?
#TODO: Bo -> Fixing while loops, add hide/show functions
#TODO: Seighin -> Create menu GUI, stylize main menu: how?
#TODO: Come up with a name?

from random import randint
import tkinter as tk
import tkinter.font as tkFont

global_padding = (10, 10)

root = tk.Tk()
root.title("Wiskunde Oefeningen v2.0.0")
root.rowconfigure(0, weight=1, minsize=175)
root.rowconfigure(1, minsize=500, weight=1)
root.rowconfigure(2, minsize=100, weight=1)
root.columnconfigure(0, weight=1, minsize=500)
root.resizable(width=False, height=False)

title_font = tkFont.Font(family="Arial", size=36, weight="bold", underline=True, slant="italic")

frm_menu = tk.Frame(root)
frm_menu.grid(row=1, column=0, sticky="nesw", pady=global_padding[1])
frm_menu.rowconfigure([0,1,2], minsize=150, weight=1)
frm_menu.columnconfigure([0,1,2,3,4,5], minsize=100, weight=1)

lbl_title = tk.Label(root, text="Wiskunde Oefeningen", bg="#0E86D4", font=title_font, fg="white")
lbl_title.grid(row=0, column=0, sticky="nesw", pady=(0, global_padding[1]*2))

btn_addition = tk.Button(frm_menu, text="Optellen")
btn_addition.grid(row=0, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])
btn_subtraction = tk.Button(frm_menu, text="Aftrekken")
btn_subtraction.grid(row=0, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_multiplication = tk.Button(frm_menu, text="Vermenigvuldigen")
btn_multiplication.grid(row=1, column=1, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])
btn_division = tk.Button(frm_menu, text="Delen")
btn_division.grid(row=1, column=3, columnspan=2, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

btn_mixed_problems = tk.Button(frm_menu, text="Gemengde Problemen")
btn_mixed_problems.grid(row=2, column=1, columnspan=4, sticky="nesw", padx= global_padding[0], pady=global_padding[1])

lbl_copyright = tk.Label(root, text="\u00A9 2021 Seighin Van Hoeserlande & Bo Van Achte", bg="#202020", fg="white")
lbl_copyright.grid(row=2, column=0, sticky="nesw", pady=(global_padding[1]*2, 0))

# Using a class to organize methods used for checking the validity of inputs
class operation_checks(): 

    # Simply checks if user has entered "stop"
    @staticmethod
    def check_for_stop(user_input):
        if user_input.lower() == "stop":
            return True

    # Checks if the inputted value is an integer. If not, handles exception
    @staticmethod
    def viability_check(user_input): 
        try:
            if int(user_input): # Ignored if the input is a valid integer. Otherwise throws ValueError
                pass
        except ValueError:
            print("\nEnkel nummers of \"stop\" zijn toegestaan\n")
            return False
        return True

# Using a class to organize methods that provide the math problems
class operations():

    @staticmethod
    def addition():
        a,b = randint(0,9), randint(0,9)
        while True:
            user_input = input(f"{a} + {b} = ")
            if operation_checks.check_for_stop(user_input):
                return True
            elif not(operation_checks.viability_check(user_input)):
                pass
            elif a+b == int(user_input):
                print("Je hebt het juist!")
                break
            else:
                print("Probeer opnieuw")

    @staticmethod
    def subtraction():
        a,b = randint(0,9), randint(0,9)
        while a<b:
            a,b = randint(0,9), randint(0,9)
        while True:
            user_input = input(f"{a} - {b} = ")
            if operation_checks.check_for_stop(user_input):
                return True
            elif not(operation_checks.viability_check(user_input)):
                pass
            elif a-b == int(user_input):
                print("Je hebt het juist!")
                break
            else:
                print("Probeer opnieuw")
    
    @staticmethod
    def multiplication():
        a,b = randint(0,9), randint(0,9)
        while True:
            user_input = input(f"{a} x {b} = ")
            if operation_checks.check_for_stop(user_input):
                return True
            elif not(operation_checks.viability_check(user_input)):
                pass
            elif a*b == int(user_input):
                print("Je hebt het juist!")
                break
            else:
                print("Probeer opnieuw")

    @staticmethod
    def division():
        a,b = randint(0,10), randint(1,10)
        product = a*b
        while True:
            user_input = input(f"{product} / {b} = ") # Utilizing Bo's method to prevent decimals
            if operation_checks.check_for_stop(user_input):
                return True
            elif not(operation_checks.viability_check(user_input)):
                pass
            elif a == int(user_input):
                print("Je hebt het juist!")
                break
            else:
                print("Probeer opnieuw")

    @staticmethod
    def mixed_problems():
        while True:
            random_operation = input_option_dict[randint(1,5)]
            if random_operation():
                return True

# Sorts user input and calls the corresponding function with a continuous loop
def game_loop(user_input):
    global input_option_dict
    input_option_dict = {1 : operations.addition, 2: operations.subtraction, 3: operations.multiplication, 4: operations.division, 5: operations.mixed_problems}
    user_choice = input_option_dict.get(user_input)
    print("Geef \"stop\" in als je terug naar het menu wilt\n")
    while True: # Game loop that continues unless True is returned singlaling the user wants to return to the main menu
        if user_choice():
            break

# Function called upon runtime as a script
def main():
    while True:
        root.mainloop()
        selection = int(input("""
---------------------------
1.) Optellen
2.) Aftrekken
3.) Vermenigvuldigen
4.) Delen
5.) Gemengd
6.) Afsluiten
---------------------------
\nGeef het getal in dat overeenkomt met de keuze dat je wilt: """))

        # Error handling for main menu
        try:
            if selection < 1 or selection > 6:
                print("\nEnkel waardes tussen 1-6 worden geaccepteerd.")
            elif selection == 6:
                quit()
            else:
                game_loop(selection)
        except ValueError:
            print("\nEnkel waardes tussen 1-6 worden geaccepteerd.")

if __name__ == '__main__': # Only runs the script if it is run directly and not imported as an external file
    main()

