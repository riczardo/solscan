import click
import re
from modules.utils.parse_contract_util import parse_contract

def randomsource(contract):
    r = re.compile('^.*blockhash.*|^.*block\.timestamp.*|^.*block\.difficulty.*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.search, parsed_contract_into_list))
    if newlist:
        for i in newlist:
            print(f"Are you sure these functions aren't used as randomness source at line {1+parsed_contract_into_list.index(newlist[i])}?")
