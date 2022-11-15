import click
import re
<<<<<<< HEAD
from modules.utils.parse_contract_util import parse_contract

def randomsource(contract):
    r = re.compile('^.*blockhash.*|^.*block\.timestamp.*|^.*block\.difficulty.*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.search, parsed_contract_into_list))
    if newlist:
        for i in newlist:
            print(f"Are you sure these functions aren't used as randomness source at line {1+parsed_contract_into_list.index(newlist[i])}?")
=======
from modules.parse_contract_util import parse_contract

def randomsource(contract):
    parsed_contract_into_list = parse_contract(contract)
    r = re.compile('^.*blockhash|block\.timestamp|block\.difficulty.*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.search, parsed_contract_into_list))
    if newlist:
        i = 0
        for item in newlist:
            print(f"Are you sure these functions aren't used as randomness source in line {1+parsed_contract_into_list.index(newlist[i])}")
            i += 1
>>>>>>> 33503c7b455ee9440537d7d284e98e15563a1f70
