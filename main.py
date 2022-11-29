import click
import re

from modules.floating_pragma import *
from modules.utils.parse_contract_util import parse_contract
from modules.selfdestruct import selfdestruct
from modules.re_entrancy import * 
from modules.unchecked_external_call import * 
from modules.wrong_constructor_name import * 
from modules.stored_credentials import * 
from modules.insec_randomsource import * 
from modules.tx_origin import * 
from modules.assembly import * 
from modules.delegate_call import *
from modules.block_timestamp import *
from modules.ether_lock import *
from modules.delegate_call import *
from modules.utils.remove_comments import *
from modules.integer_underflow_overflow import *
from modules.rtlo import *
from modules.multiple_constructors import *
from modules.dynamic_array_length import *

@click.group()
def mycommands():
    pass

@click.command()
@click.argument('contract', type=click.Path(exists=True), required=1)
def scan_contract(contract):
    #floating_pragma(contract)
    #selfdestruct(contract)
    reentrancy(contract)
    #unchecked_external_call(contract)
    #wrong_constructor_name(contract)
    #stored_credentials(contract)
    #randomsource(contract)
    #tx_origin(contract)
    #assembly(contract)
    #ether_lock(contract)
    #delegate_call(contract)
    #block_timestamp(contract)
    #sanitize(contract)
    #integer_underflow_overflow(contract)
    #rtlo(contract)
    #multiple_constructors(contract)
    dynamic_array_length(contract)
    


mycommands.add_command(scan_contract)

if __name__ == '__main__':
    mycommands()

#nowa tablica za kazdym razem - nieoptymalnie