import click
import re
import time
import random
import pyfiglet

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
from modules.utils.banner import *
from modules.looped_calls import *

@click.group()
def mycommands():
    pass

def update_bar(progress_bar_iterator):
    progress_bar_iterator.update(1)
    print("\n")
    time.sleep(random.uniform(0.5,1.0))

@click.command('scan', help="scan contract")
@click.argument('contract', type=click.Path(exists=True), required=1)
def scan_contract(contract):  
    print_banner()  
    with click.progressbar(length=17, label="Running checks") as bar:
        print("\n")
        for i in range(16):
            pass
            #update_bar(bar)
        print('''======================================
        RESULTS
        ====================================
        ''')
        
        try:
            floating_pragma(contract)
            #update_bar(bar)
        except:
            print("An error occured while checking floating pragma. This vulnerability class was NOT checked.")

        try:
            selfdestruct(contract)
            #update_bar(bar)
        except:
            print("An error occured while checking selfdestruct. This vulnerability class was NOT checked.")

        try:
            reentrancy(contract)
            #update_bar(bar)
        except:
            print("An error occured while checking reentrancy. This vulnerability class was NOT checked.")

        try:
            unchecked_external_call(contract)
            #update_bar(bar)
        except:
            print("An error occured while checking unchecked external call. This vulnerability class was NOT checked.")

        try:
            wrong_constructor_name(contract)
            #update_bar(bar)
        except:
            print("An error occured while checking wrong constructor name. This vulnerability class was NOT checked.")

        try:
            pass
            stored_credentials(contract)
            #update_bar(bar)
        except:
            print("An error occured while checking stored credentials. This vulnerability class was NOT checked.")

        try:
            pass
            #randomsource(contract)
            #update_bar(bar)
        except:
            print("An error occured while checking random source. This vulnerability class was NOT checked.")

        try:
            tx_origin(contract)
            #update_bar(bar)
        except:
            print("An error occured while checking transaction origin. This vulnerability class was NOT checked.")

        try:
            assembly(contract)
            #update_bar(bar)
        except:
            print("An error occured while checking assembly. This vulnerability class was NOT checked.")

        try:
            ether_lock(contract)
            #update_bar(bar)
        except:
            print("An error occured while checking ether lock. This vulnerability class was NOT checked.")

        try:
            delegate_call(contract)
            #update_bar(bar)
        except:
            print("An error occured while checking delegate call. This vulnerability class was NOT checked.")

        try:
            pass
            #block_timestamp(contract)
            #update_bar(bar)
        except:
            print("An error occured while checking block timestamp. This vulnerability class was NOT checked.")

        #sanitize(contract)
        #update_bar(bar)
        
        try:
            integer_underflow_overflow(contract)
            #update_bar(bar)
        except:
            print("An error occured while checking integer under/overflow. This vulnerability class was NOT checked.")

        try:
            pass
            #rtlo(contract)
            #update_bar(bar)
        except:
            print("An error occured while checking RTLO. This vulnerability class was NOT checked.")

        try:
            pass
            #multiple_constructors(contract)
            #update_bar(bar)
        except:
            print("An error occured while checking multiple constructors. This vulnerability class was NOT checked.")

        try:
            pass
            dynamic_array_length(contract)
            #update_bar(bar)
        except:
            print("An error occured while checking dynamic array length. This vulnerability class was NOT checked.")
        
        try:
        
            looped_calls(contract)
        except:
            print("An error occured while checking looped calls. This vulnerability class was NOT checked.")
        
        click.echo("Scan completed. See results above.")
    


mycommands.add_command(scan_contract)

if __name__ == '__main__':
    mycommands()

#nowa tablica za kazdym razem - nieoptymalnie