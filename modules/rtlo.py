from hashlib import new
import click
import re
from modules.utils.parse_contract_util import parse_contract


def rtlo(contract):
    r = re.compile(".*\u202e.*")
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    if newlist:
        for i in range(len(newlist)):
            print(f"Right-to-left-override found at line/s {1+parsed_contract_into_list.index(newlist[i])}. Make sure to disallow special characters that pose security concerns.")
