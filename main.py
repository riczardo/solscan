import click
from modules.floating_pragma import *
from modules.utils.parse_contract_util import parse_contract
import re

<<<<<<< HEAD
#from modules.selfdestruct import selfdestruct
#from modules.re_entrancy import * 
#from modules.unchecked_external_call import * 
#from modules.wrong_constructor_name import * 
#from modules.stored_credentials import * 
#from modules.insec_randomsource import * 
#from modules.tx_origin import * 
#from modules.assembly import * 
from modules.delegate_call import *
from modules.block_timestamp import *
from modules.utils.remove_comments import *
=======
from modules.selfdestructTODO import selfdestruct
from modules.re_entrancy import * 
from modules.unchecked_external_call import * 
from modules.wrong_constructor_name import * 
from modules.stored_credentialsTODO import * 
from modules.insec_randomsource import * 
from modules.tx_origin import * 
from modules.assembly import * 
>>>>>>> 33503c7b455ee9440537d7d284e98e15563a1f70

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
    randomsource(contract)
    #tx_origin(contract)
    #assembly(contract)
    #ether_lock(contract)
<<<<<<< HEAD
    #delegate_call(contract)
    #block_timestamp(contract)
    sanitize(contract)
    

=======
>>>>>>> 33503c7b455ee9440537d7d284e98e15563a1f70

mycommands.add_command(scan_contract)

if __name__ == '__main__':
    mycommands()

#nowa tablica za kazdym razem - nieoptymalnie