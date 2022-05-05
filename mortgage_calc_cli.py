# mortgage_calc.py 
    
"""
    A terminal-based program for amortizing and displaying loan payment information.
    The program takes user input for loan amount, interest rate, 
    loan term (in months) and optionally, homeowners insurance and property tax 
    amounts, calculates both the principal and interest payment amount and total 
    payment amount (if amounts for taxes and insurance are provided) and displays 
    the result in a terminal panel. Further, the user is given the option to view a full 
    amortization schedule and, if they chose to do so, are given the further option 
    to save the amortization table (which is saved as a text file).
    
    The module uses the `rich` library to format the output to the terminal, allowing
    easy customization of the presentation. In particular, the module uses the Table and 
    Panel classes from the rich.console module. The mathematical calculations are 
    handled by a scratch-written amortization function saved as separate module. 
    There are very good amortization libraries in Pypi. However, I decided to write 
    my own function to decrease the number of dependencies.
"""

import os
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt, FloatPrompt, Confirm
from rich.table import Table
from amortization_function import amortization
import argparse



# Instantiate a Console object. `record` set to True in order to use .export_text()
console = Console(record=True)


def clear():
    """A cross platform function to clear the terminal screen"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


clear()

parser = argparse.ArgumentParser(
                                description="A command line mortgage payment calculator"
)

parser.add_argument("loan",
                    help="Loan Amount",
                    type=float)
parser.add_argument("interest",
                    help="Interest Rate",
                    type=float)
parser.add_argument("term",
                    type=int,
                    help="Term of loan in months")
parser.add_argument("-t", "--taxes",
                    help="Annual property tax",
                    type=float,
                    default=0)
parser.add_argument("-i", "--insurance",
                    help="Annual property insurance",
                    type=float,
                    default=0)

args = parser.parse_args()


# User Input
# p = FloatPrompt.ask("Loan Amount")  # Principal amount of loan
# i = FloatPrompt.ask("Interest Rate") # Interest rate entered as float > 0
# n = IntPrompt.ask("Loan term (in months)")  # Loan term in months
# tx = FloatPrompt.ask("Annual taxes", default=0) / 12  
# ie = FloatPrompt.ask("Annual insurance", default=0) / 12  

# Call amortization function from amortization_function.py using loan amount, interest rate, and term as arguments
data = amortization(args.loan, args.interest, args.term)

# Monthly payment comes from the [1] index position of the [0] tuple returned by the amortization function
monthly_pi_payment = data[0][1]

# Content for summary panel containing monthly payment breakdown
display_text = f"""Principal and Interest: [bright_green]${monthly_pi_payment:,.2f}[/bright_green]
Property Taxes: [bright_green]${args.taxes / 12:.2f}[/bright_green]
Insurance: [bright_green]${args.insurance/ 12:.2f}[/bright_green]

Total Payment: [bright_green bold]${monthly_pi_payment + (args.taxes / 12) + (args.insurance / 12):.2f}[/bright_green bold]"""

print()
print()
rprint(Panel.fit(display_text, title="Monthly Payment Information", padding=(1,4), border_style="bold"))
print()
print()
#-----------------------------------------------------------------
# # Amortization Table
# table = Table(title=f"""Loan Summary With Amortization Schedule
# Loan Amount: {p:.2f}\tInterest Rate: {i}
# Term: {n} months ({n/12} years)""", title_justify="left")
# table.add_column("Number", justify="right")
# table.add_column("Payment", justify="right")
# table.add_column("Interest", justify="right")
# table.add_column("Principal", justify="right")
# table.add_column("Balance", justify="right")

# # iterate through `data` to build table 
# for number, amount, interest, principal, balance in data:
#     table.add_row(f"{number}", f"{amount:,.2f}", f"{interest:,.2f}", f"{principal:,.2f}", f"{balance:,.2f}")
# #-----------------End Panel______________________________

# print_am = Confirm.ask("Do you want to see an amortization schedule now?")
# if print_am:
#     print()
#     console.print(table)

#     # Option to save amortization table as txt file. The file maintains its form but loses its
#     # escape code formatting. Saved in the currently open directory.
#     save_am = Confirm.ask("Would you like to save a copy?")
#     if save_am:
#         save_table = console.export_text()
#         with open("loan_summary.txt", mode="w") as file:
#             file.write(save_table)
#         print()

# print()
# print()
# console.rule("Thanks!")
# print()
# print()



