import click
import re
from modules.utils.parse_contract_util import parse_contract
import ntpath # solves problem off full path or test catalog issue


def stored_credentials(contract):
    parsed_contract_into_list = parse_contract(contract)
    y = open("1kpasswords.txt", 'r', encoding="utf-8")
    passwords = y.readlines()

    converted_passwds = []
    for line in passwords:
        converted_passwds.append(line.strip())

    for element in converted_passwds:
        formula = r'^(.*?(\b' + element + r'\b)[^$]*)$'
        r = re.compile(formula)
        newlist = list(filter(r.match, parsed_contract_into_list))
        if newlist: 
            for i in range(len(newlist)):
                print("Be sure to check you are not storing credentials in the contract in line:")
                print(f"{1+parsed_contract_into_list.index(newlist[i])}" + " - " + newlist[i])

