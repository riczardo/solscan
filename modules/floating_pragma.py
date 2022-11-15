import click
import re
from modules.utils.parse_contract_util import parse_contract


def floating_pragma(contract):
    r = re.compile('pragma solidity \^')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    print(f"Floating pragma found at line {1+parsed_contract_into_list.index(newlist[0])}")
