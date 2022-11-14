import click
import re
from modules.parse_contract_util import parse_contract
import ntpath # solves problem off full path or test catalog issue


def stored_credentials(contract):
    parsed_contract_into_list = parse_contract(contract)
    y = open("10kpasswords.txt", 'r', encoding="utf-8")
    passwords = y.readlines()
    #for line in passwords:
    converted_passwds = []
    for line in passwords:
        converted_passwds.append(line.strip())
    #print(converted_passwds)
    #z = '|'.join(converted_passwds)
    #print(z)
    for element in converted_passwds:
        formula = r'^(.*?(\b' + element + r'\b)[^$]*)$'
        print(parsed_contract_into_list)
