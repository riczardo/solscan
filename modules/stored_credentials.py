import click
import re
from modules.utils.parse_contract_util import parse_contract
import ntpath # solves problem off full path or test catalog issue
from modules.utils.printer import *
from vulnerabilities_descriptions.storedcreds_desc import *


def stored_credentials(contract):
    parsed_contract_into_list = parse_contract(contract)
    y = open("1kpasswords.txt", 'r', encoding="utf-8")
    passwords = y.readlines()

    converted_passwds = []
    for line in passwords:
        converted_passwds.append(line.strip())
    newlist = []
    for element in converted_passwds:
        formula = r'^(.*?(\b' + element + r'\b)[^$]*)$'
        r = re.compile(formula)
        newlist += list(filter(r.match, parsed_contract_into_list))
    #print(newlist)
    #if newlist: 
    #    for i in range(len(newlist)):
    #        print("Be sure to check you are not storing credentials in the contract in line:")
    #        print(f"{1+parsed_contract_into_list.index(newlist[i])}" + " - " + newlist[i])
        #make newlist printable 
    newlist_to_print = []
        #=====
    print(len(newlist))
    if newlist:
        for i in range(len(newlist)):
            line_number = 1+parsed_contract_into_list.index(newlist[i]) #line number
            line_number_as_str = str(line_number) #line number to string
            newlist_to_print.append(line_number_as_str) #new list without []
        newlist_printable = ', '.join(newlist_to_print) #new list without []
            #Use printer
        printer_vuln(newlist_printable, vulnerability_name, vulnerability_description, vulnerability_recommendation, more_info)
