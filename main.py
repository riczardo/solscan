import click
import re
import time
import random
import pyfiglet
import os

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
#from modules.block_timestamp import *
from modules.ether_lock import *
from modules.delegate_call import *
from modules.utils.remove_comments import *
from modules.integer_underflow_overflow import *
from modules.rtlo import *
from modules.multiple_constructors import *
from modules.dynamic_array_length import *
from modules.utils.banner import *
from modules.looped_calls import *
from modules.hash_colission import *
from modules.functions_default_visibility import *
from modules.assert_violation import *
from modules.arbitraryfrom import *
from modules.bad_assignment_operator import *
from modules.depr_blockhash import *
from modules.depr_msggas import *
from modules.depr_now import *
from modules.depr_now import *
from modules.depr_sha3 import *
from modules.depr_throw import *
from modules.multidigits import *
from modules.strict_equality import *


@click.group()
def mycommands():
    pass

def update_bar(progress_bar_iterator):
    progress_bar_iterator.update(1)
    print("\n")
    time.sleep(0.1)

@click.command('scan', help="scan contract")
@click.argument('contract', type=click.Path(exists=True), required=1)
def scan_contract(contract):  
    print_banner(contract)  
    with click.progressbar(length=30, label="Running checks") as bar:
        print("\n")
        for i in range(30):
            pass
            update_bar(bar)
        print('''
======================================
              RESULTS
======================================
        ''')
        try:
            arbitraryfrom(contract)
        except:
            print("An error occured while checking arbitrary form. This vulnerability class was NOT checked.")

        try:
            assembly(contract)
        except:
            print("An error occured while checking assembly. This vulnerability class was NOT checked.")

        try:
            assert_violation(contract)
        except:
            print("An error occured while checking assert violation. This vulnerability class was NOT checked.")

        try:
            bad_assignment_operator(contract)
        except:
            print("An error occured while checking bad assignment operator. This vulnerability class was NOT checked.")

        try:
            block_timestamp(contract)
        except:
            print("An error occured while checking block timestamp. This vulnerability class was NOT checked.")

        try:
            delegate_call(contract)
        except:
            print("An error occured while checking delegate call. This vulnerability class was NOT checked.")

        try:
            blockhash(contract)
        except:
            print("An error occured while checking blockhash. This vulnerability class was NOT checked.")

        try:
            callcode(contract)
        except:
            print("An error occured while checking callcode. This vulnerability class was NOT checked.")

        try:
            msggas(contract)
        except:
            print("An error occured while checking msggas. This vulnerability class was NOT checked.")

        try:
            now(contract)
        except:
            print("An error occured while checking now. This vulnerability class was NOT checked.")

        try:
            sha3(contract)
        except:
            print("An error occured while checking sha3. This vulnerability class was NOT checked.")

        try:
            throw(contract)
        except:
            print("An error occured while checking throw. This vulnerability class was NOT checked.")

        try:
            dynamic_array_length(contract)
        except:
            print("An error occured while checking dynamic array length. This vulnerability class was NOT checked.")
        
        try:
            ether_lock(contract)
        except:
            print("An error occured while checking integer ether lock. This vulnerability class was NOT checked.")

        try:
            floating_pragma(contract)
        except:
            print("An error occured while checking floating pragma. This vulnerability class was NOT checked.")

        try:
            function_default_visibility(contract)
        except:
            print("An error occured while checking function default visibility. This vulnerability class was NOT checked.")

        try:
            hash_colission(contract)
        except:
            print("An error occured while checking hash colission. This vulnerability class was NOT checked.")
        
        try:
            insec_randomsource(contract)
        except:
            print("An error occured while checking insec randomsource. This vulnerability class was NOT checked.")

        try:
            integer_underflow_overflow(contract)
        except:
            print("An error occured while checking integer under/overflow. This vulnerability class was NOT checked.")

        try:
            looped_calls(contract)
        except:
            print("An error occured while checking looped calls. This vulnerability class was NOT checked.")

        try:
            multidigit(contract)
        except:
            print("An error occured while checking multidigit. This vulnerability class was NOT checked.")


        try:
            multiple_constructors(contract)
        except:
            print("An error occured while checking multiple constructors. This vulnerability class was NOT checked.")     
        
        try:
            re_entrancy(contract)
        except:
            print("An error occured while checking reentrancy. This vulnerability class was NOT checked.")
        

        try:
            rtlo(contract)
        except:
            print("An error occured while checking rtlo. This vulnerability class was NOT checked.")        
        
        try:
            selfdestruct(contract)
        except:
            print("An error occured while checking selfdestruct. This vulnerability class was NOT checked.")       
        
        try:
            stored_credentials(contract)
        except:
            print("An error occured while checking stored credentials. This vulnerability class was NOT checked.")

        try:
            strict_equality(contract)
        except:
            print("An error occured while checking strict equality This vulnerability class was NOT checked.")

        try:
            tx_origin(contract)
        except:
            print("An error occured while checking tx origin. This vulnerability class was NOT checked.")

        try:
            unchecked_external_call(contract)
        except:
            print("An error occured while checking unchecked external call. This vulnerability class was NOT checked.")

        try:
            wrong_constructor_name(contract)
        except:
            print("An error occured while checking wrong constructor name. This vulnerability class was NOT checked.")
            
        click.echo("Scan completed. See results above.")



mycommands.add_command(scan_contract)

if __name__ == '__main__':
    mycommands()

