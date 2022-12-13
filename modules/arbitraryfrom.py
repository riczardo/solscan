import click
import re
from modules.utils.parse_contract_util import parse_contract
from vulnerabilities_descriptions.arbitraryfrom_desc import *


def arbitraryfrom(contract):
    r = re.compile('^.*transferFrom\(.*\).*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    stripped = [s.strip() for s in newlist]
    r2 = re.compile('^.*transferFrom\(msg\.sender.*\).*')
    newlist2 = list(filter(r2.match, stripped))
    newlist_to_print = []
    if not newlist2:
        for i in range(len(newlist)):
            line_number = 1+parsed_contract_into_list.index(newlist[i]) #line number
            line_number_as_str = str(line_number) #line number to string
            newlist_to_print.append(line_number_as_str) #new list without []
        newlist_printable = ', '.join(newlist_to_print) #new list without []
        #Use printer
        printer_vuln(newlist_printable, vulnerability_name, vulnerability_description, vulnerability_recommendation, more_info)