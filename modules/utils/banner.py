import pyfiglet
import click
from termcolor import colored

def print_banner(contract_name):
    banner = pyfiglet.figlet_format("solscan")
    print(banner)
    click.echo(f'''smart contracts vulnerability scanner \n

Tool is avaliable under MIT license.
Authors:
@riczardo
@BartekM101
@florkie
''')
    print("Scanning "+colored(f"{contract_name}", attrs=['bold'])+" in progress.\nPlease see results below.\n")

