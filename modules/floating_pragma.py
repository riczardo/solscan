import click
import re
from modules.utils.parse_contract_util import parse_contract
from modules.utils.printer import *
from vulnerabilities_descriptions.floating_pragma_desc import *


def floating_pragma(contract):
    r = re.compile('pragma solidity \^')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))

    #make newlist printable 
    newlist_to_print = []
    #=====
    if newlist:
        for i in range(len(newlist)):
            line_number = 1+parsed_contract_into_list.index(newlist[i]) #line number
            line_number_as_str = str(line_number) #line number to string
            newlist_to_print.append(line_number_as_str) #new list without []
        newlist_printable = ', '.join(newlist_to_print) #new list without []
        #Use printer
        printer_vuln(newlist_printable, vulnerability_name, vulnerability_description, vulnerability_recommendation, more_info)