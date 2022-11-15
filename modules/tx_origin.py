import click
import re
from modules.utils.parse_contract_util import parse_contract

# @click.command
# @click.argument('contract', type=click.Path(exists=True), required=1)
def tx_origin(contract):
    r = re.compile('^.*tx.origin == owner.*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    if newlist:
        for i in range(len(newlist)):
            print(f"Do not use tx.origin for authentication purposes in line {1+parsed_contract_into_list.index(newlist[i])}, use msg.sender instead")
        
