# Mortgage Calculator Command Line Interface

A command line interface (CLI) for calculating mortgage loan payment information.
The CLI uses three required positional arguments for loan amount, interest rate, 
and loan term (in months) as well as two optional arguments -i: Annual property
insurance premium; and -t: Annual property taxes. The module then calculates the
monthly principal and interest payment and displays the result (along with monthly
tax and insurance payments, if the optional arguments are entered).

The module uses the 'rich' library to format the output to the terminal, allowing
easy customization of the presentation. In particular, the module uses the Table and 
Panel classes from the rich.console module. The mathematical calculations are 
handled by a scratch-written amortization function saved as separate module. 
There are very good amortization libraries in Pypi. However, I decided to write 
my own function to decrease the number of dependencies.

From the help screen 

usage: mortgage_calc_cli.py [-h] [-t TAXES] [-i INSURANCE] loan interest term

A command line mortgage payment calculator

positional arguments:
  loan                  Loan Amount
  interest              Interest Rate
  term                  Term of loan in months

options:
  -h, --help            show this help message and exit
  -t TAXES, --taxes TAXES
                        Annual property tax
  -i INSURANCE, --insurance INSURANCE
                        Annual property insurance