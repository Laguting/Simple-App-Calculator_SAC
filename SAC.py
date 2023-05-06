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
while True:
    ask_usr = input("\n\n\33[1m\33[34m What operation would you like to perform? Enter Add = '+'; Subtraction = '-'; Multiplication = '*'; Division = '/': \33[0m")
    try:
        number_1 = float(input("1st number: "))
        number_2 = float(input("2nd number: "))
    except ValueError:
        print("This calculator only accepts numbers") 
  # Perform the calculations
  # ask for another inputs
     # If no, Display "Thank you" and exit
# Closing