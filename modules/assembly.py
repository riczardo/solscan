import click
import re
from modules.utils.parse_contract_util import parse_contract

# @click.command
# @click.argument('contract', type=click.Path(exists=True), required=1)
def assembly(contract):
    r = re.compile('^.*assembly.*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))

    if newlist:
        for i in range(len(newlist)):
            print(f"Assembly usage in line {1+parsed_contract_into_list.index(newlist[i])}. This function bypasses several safety features and checks of Solidity ")
        
