from hashlib import new
import click
import re
from modules.parse_contract_util import parse_contract


def selfdestruct(contract):
    r = re.compile('^.*block\.timestamp.*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    if newlist:
        i = 0
        for item in newlist:
            print(f"Usage of block.timestamp found at line {1+parsed_contract_into_list.index(newlist[0])}. Avoid using block.timestamp for randomness, as it can be tampered by the miners.")
            i += 1