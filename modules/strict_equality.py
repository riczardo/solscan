from hashlib import new
import click
import re
from modules.utils.parse_contract_util import parse_contract


def strict_equality(contract):
    r = re.compile('^.*\.balance *== *\d*\.?\d*.*(ether|wei|gwei)')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.findall, parsed_contract_into_list))

    if newlist:
        for i in range(len(newlist)):
            print(f"Dangerous strict equality found at lines {1+parsed_contract_into_list.index(newlist[i])}. Do not use strict equality in order to check if account/contract has enought Ether.")
