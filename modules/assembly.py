import click
import re
from modules.parse_contract_util import parse_contract


def assembly(contract):
    r = re.compile('^.*assembly')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    if newlist:
        i = 0
        for item in newlist:
            print(f"Assembly usage in line {1+parsed_contract_into_list.index(newlist[0])}, this function bypasses several safety features and check of Solidity ")
            i += 1
