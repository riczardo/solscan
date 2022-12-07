import click
import re
from modules.utils.parse_contract_util import parse_contract
from modules.utils.printer import *
from vulnerabilities_descriptions.blockhash_desc import *


def blockhash(contract):
    r = re.compile('^.*block\.blockhash.*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    #if newlist:
    #    for i in range(len(newlist)):
    #        print(f"Do not use tx.origin for authentication purposes in line {1+parsed_contract_into_list.index(newlist[i])}, use msg.sender instead")
    #make newlist printable 
    #
    newlist_to_print = []
    #=====
    #https://docs.soliditylang.org/en/v0.4.25/miscellaneous.html#global-variables
    if newlist:
        for i in range(len(newlist)):
            line_number = 1+parsed_contract_into_list.index(newlist[i]) #line number
            line_number_as_str = str(line_number) #line number to string
            newlist_to_print.append(line_number_as_str) #new list without []
        newlist_printable = ', '.join(newlist_to_print) #new list without []
        #Use printer
        printer_vuln(newlist_printable, vulnerability_name, vulnerability_description, vulnerability_recommendation, more_info) 