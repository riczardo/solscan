from hashlib import new
import click
import re
from modules.utils.parse_contract_util import parse_contract


def bad_assignment_operator(contract):
    r = re.compile('^.*(\=\+|\=\-|\=\\|\=\*).*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.findall, parsed_contract_into_list))

    if newlist:
        for i in range(len(newlist)):
            print(f"Unary typo found at lines {1+parsed_contract_into_list.index(newlist[i])}. Given value will not update when executed. Implement unary expression properly.")
