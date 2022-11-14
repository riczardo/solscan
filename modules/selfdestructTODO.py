from hashlib import new
import click
import re
from modules.parse_contract_util import parse_contract


def selfdestruct(contract):
    r = re.compile('^.*selfdestruct(.*);|suicide(.*);')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    if newlist:
        for item in newlist:
            print(f"Selfdestruct/suicide function found at line {1+parsed_contract_into_list.index(newlist[0])}")
