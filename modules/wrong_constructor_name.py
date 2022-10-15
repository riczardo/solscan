import click
import re
from modules.parse_contract_util import parse_contract
import ntpath # solves problem off full path or test catalog issue

# @click.command
# @click.argument('contract', type=click.Path(exists=True), required=1)
def wrong_constructor_name(contract):
    contract_name_with_extension = ntpath.basename(contract) # ./test/Reentrancy.sol -> Reentrancy.sol
    contract_name = contract_name_with_extension.split('.')[0] # Reentrancy.sol -> Reentrancy   
    print(contract_name)
    r = re.compile('^.*{}\(.*\)'.format(contract_name), re.IGNORECASE)
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))

    #===================================================================== 
    #check if list is empty == not proper constructor name

    if newlist:
        pass
    else:
        print(f"A contract probably uses bad constructor name - \"{contract_name}()\" function is misssing")


