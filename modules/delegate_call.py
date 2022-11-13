from hashlib import new
import click
import re
from modules.parse_contract_util import parse_contract

# @click.command
# @click.argument('contract', type=click.Path(exists=True), required=1)
def selfdestruct(contract):
    r = re.compile('^.*delegatecall(.*)|^.*callcode(.*)')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    if newlist:
        print(f"Delegatecall found at line {1+parsed_contract_into_list.index(newlist[0])}. Avoid using delegatecall if not nessesary. Otherwise, use ony trusted addresses.")
