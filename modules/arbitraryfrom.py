import click
import re
from modules.utils.parse_contract_util import parse_contract


def arbitraryfrom(contract):
    r = re.compile('^.*transferFrom\(.*\).*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    stripped = [s.strip() for s in newlist]
    r2 = re.compile('^.*transferFrom\(msg\.sender.*\).*')
    newlist2 = list(filter(r2.match, stripped))
    if not newlist2:
        for i in range(len(newlist)):
            print(f"It is advisable to use msg.sender as from parameter in transferFrom function in line: {1+parsed_contract_into_list.index(newlist[i])}")