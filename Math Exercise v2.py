# Title: Math Exercises
# Version: 2.0.0
# Author: Seighin Van Hoeserlande & Bo Van Achte
# Description: Simple program created to test basic mathmatical skills of the user. Created as a project for school on 09-30-2021

#// TODO: Make game loop
#TODO: Add GUI (v2.0.0)
#TODO: Optimize?
#// TODO: Add comments

from random import randint, choice

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