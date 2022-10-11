import click
import re
from modules.parse_contract_util import parse_contract

@click.command
@click.argument('contract', type=click.Path(exists=True), required=1)
def floating_pragma(contract):
    r = re.compile('pragma solidity \^')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    print(1+parsed_contract_into_list.index(newlist[0]))
