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
print("          ┻┳|              ")
print("          ┳┻| _")
print("          ┻┳|•.•) i'm watching.....")
print("          ┳┻|  ⊂ﾉ)")
print("          ┻┳|")
print()
print("⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆" * 10)
  # Ask the user for any inputs
def process():
    with open("calc_history.text", "w") as calculatorhistory_file: # Open text file that will hold the history of inputs
        while True:
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
            calculatorhistory_file.close()            
process()
  # ask for another inputs
     # If no, Display "Thank you" and exit
# Closing