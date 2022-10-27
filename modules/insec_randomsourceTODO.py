import click
import re
from modules.parse_contract_util import parse_contract

def randomsource(contract):
    parsed_contract_into_list = parse_contract(contract)
    r = re.compile('blockhash|block\.timestamp|block\.difficulty')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.search, parsed_contract_into_list))
    if newlist:
        i = 0
        for item in newlist:
            print(f"Are you sure these functions aren't used as randomness source in line {1+parsed_contract_into_list.index(newlist[i])}")
            i += 1
