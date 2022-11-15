import click
import re
from modules.utils.parse_contract_util import parse_contract


def reentrancy(contract):
    r = re.compile('^.*call\.value\(.*\).*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    if newlist:
        for i in newlist:
            print(f"Re-entrancy found at line {1+parsed_contract_into_list.index(newlist[i])}")

