# Laguting, Maricon Jane G.
# Task: Create a Simple App Calculator that applies the Exception handling lesson.

# Opening
from pyfiglet import Figlet
from termcolor import colored
s_a_c = Figlet(font = "digital")
print()
print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆" * 10)
print()
print(colored(s_a_c.renderText("Simple App Calculator"), "yellow"))
print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆" * 10)
# Welcome
s_a_c = Figlet(font = "banner3-D")
print()
print(colored(s_a_c.renderText(" Welcome"), "green"))
print("\33[35m          ┻┳|              \33[0m")
print("\33[35m          ┳┻| _\33[0m")
print("\33[35m          ┻┳|•.•) i'm watching.....\33[0m")
print("\33[35m          ┳┻|  ⊂ﾉ)\33[0m")
print("\33[35m          ┻┳|\33[0m")
print()
print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆" * 10)
  # Ask the user for any inputs
def process():
    with open("calc_history.text", "w") as calculatorhistory_file: # Open text file that will hold the history of inputs
        while True:
     # ask for another inputs
          again_usr = input("\n\33[36m Would you like to try again: Enter 'Y' if yes and 'N' if no: \33[0m")
     # If yes call process
          if again_usr.upper() == "Y":
            try:
               ask_usr = input("\n\n\33[1m\33[34m What operation would you like to perform? Enter Add = '+'; Subtraction = '-'; Multiplication = '*'; Division = '/': \33[0m")
               if ask_usr not in ["+", "-", "*", "/"]:
                   raise ValueError
            except ValueError:
                print("Invalid Operation. Try again.")
                process()
            try:
                number_1 = float(input("\n\33[43m1st number: \33[0m"))
                number_2 = float(input("\n\33[43m2nd number: \33[0m"))
            except ValueError:
                print("\n\33[1m\33[31mThis calculator only accepts numbers\33[0m") 
                process()
  # Perform the calculations
    # Add
            if ask_usr == "+": 
                add = number_1 + number_2
                result1 = (f"\n\33[7m{number_1} {ask_usr} {number_2} = {add}\33[0m")
                print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆" * 10)
                print("\n", result1, "\n")
                print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆" * 10)
                calculatorhistory_file.write(f"{number_1} {ask_usr} {number_2} = {add}" + '\n')
    # Subtract
            elif ask_usr == "-":
                sub_tract = number_1 - number_2
                result2 = (f"\n\33[7m{number_1} {ask_usr} {number_2} = {sub_tract}\33[0m")
                print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆" * 10)
                print("\n", result2, "\n")
                print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆" * 10)
                calculatorhistory_file.write(f"{number_1} {ask_usr} {number_2} = {sub_tract}" + '\n')
    # Multiplication
            elif ask_usr == "*":
                multi_ply = number_1 * number_2
                result3 = (f"\n\33[7m{number_1} {ask_usr} {number_2} = {multi_ply}\33[0m")
                print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆" * 10)
                print("\n", result3, "\n")
                print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆" * 10)
                calculatorhistory_file.write(f"{number_1} {ask_usr} {number_2} = {multi_ply}" + '\n')
    # Division
            elif ask_usr == "/":
                divi_sion = number_1 / number_2
                result4 = (f"\n\33[7m{number_1} {ask_usr} {number_2} = {divi_sion}\33[0m")
                print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆" * 10)
                print("\n", result4, "\n")
                print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆" * 10)
                calculatorhistory_file.write(f"{number_1} {ask_usr} {number_2} = {divi_sion}" + '\n')
            else:
                break
            calculatorhistory_file.close()
     # If no, Display "Thank you" and exit
          else:
            exit_1 = Figlet(font = "slant")
            print(colored(exit_1.renderText("Thank you! <3"), "magenta"))
            print("\n\33[3m Until next time!...\33[0m")            
# Closing
process()