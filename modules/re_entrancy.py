import click
import re
from modules.parse_contract_util import parse_contract

# @click.command
# @click.argument('contract', type=click.Path(exists=True), required=1)
def reentrancy(contract):
    r = re.compile('^.*call\.value(.*)')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    if newlist:
        i = 0
        for item in newlist:
            print(f"Re-entrancy found at line {1+parsed_contract_into_list.index(newlist[i])}")
            i +=1
