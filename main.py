import click
from modules.floating_pragma import *
from modules.parse_contract_util import parse_contract
import re

from modules.selfdestruct import selfdestruct

@click.group
def mycommands():
    pass

@click.command()
@click.argument('contract', type=click.Path(exists=True), required=1)
def scan_contract(contract):
    floating_pragma(contract)
    selfdestruct(contract)

mycommands.add_command(scan_contract)

if __name__ == '__main__':
    mycommands()