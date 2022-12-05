import click
import re
from modules.utils.parse_contract_util import parse_contract
from modules.utils.printer import *
from vulnerabilities_descriptions.dynamic_array_desc import *


def dynamic_array_length(contract):
    r = re.compile('.*uint\[\].*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    #print(len(newlist))
    #if newlist:
    #    for i in range(len(newlist)):
    #        #print(f"Re-entrancy found at line {1+parsed_contract_into_list.index(newlist[i])}")
    #        #linijka ponizej musi zostac dodana (wprowadza numer lini wystpujcej podatnosci):
    #        line_number = 1+parsed_contract_into_list.index(newlist[i])
    #        print('dynamic array is declared at line ' + str(line_number))
    #        #printer_vuln(line_number, vulnerability_name, vulnerability_description, vulnerability_more_info_links, vulnerability_recommendation, vulnerability__description_more_info_links)
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