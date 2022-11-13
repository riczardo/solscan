import click
from modules.floating_pragma import *
from modules.parse_contract_util import parse_contract
import re

from modules.selfdestruct import selfdestruct
from modules.re_entrancy import * 
from modules.unchecked_external_call import * 
from modules.wrong_constructor_name import * 
from modules.stored_credentialsTODO import * 
from modules.insec_randomsourceTODO import * 
from modules.tx_origin import * 
from modules.assembly import * 

@click.group()
def mycommands():
    pass

@click.command()
@click.argument('contract', type=click.Path(exists=True), required=1)
def scan_contract(contract):
    #floating_pragma(contract)
    #selfdestruct(contract)
    #reentrancy(contract)
    #unchecked_external_call(contract)
    #wrong_constructor_name(contract)
    #stored_credentials(contract)
    #randomsource(contract)
    #tx_origin(contract)
    assembly(contract)

mycommands.add_command(scan_contract)

if __name__ == '__main__':
    mycommands()