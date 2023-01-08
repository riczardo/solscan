import click
import re
from modules.utils.parse_contract_util import parse_contract
from modules.utils.printer import *
from vulnerabilities_descriptions.funcdefvis import *


def function_default_visibility(contract):
    r = re.compile('.*function .*\(.*\).*') #
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    #make newlist printable 
    newlist_to_print = []
    # try statement
    for i in range(len(newlist)):

        try:
            found = re.search('function .*(.*?).*', newlist[i]).group(0)

            splited_words = found.split()

            if len(splited_words) < 3:

                line_number = 1+parsed_contract_into_list.index(newlist[i]) #line number
                line_number_as_str = str(line_number) #line number to string
                newlist_to_print.append(line_number_as_str) #new list without []
            else:
                #we have to check
                if splited_words[2] == 'public' or splited_words[2] == 'private' or splited_words[2] == 'external' or splited_words[2] == 'internal' or splited_words[2] == 'public{' or splited_words[2] == 'private{' or splited_words[2] == 'external{' or splited_words[2] == 'internal{':
                    pass

                else:

                    line_number = 1+parsed_contract_into_list.index(newlist[i]) #line number
                    line_number_as_str = str(line_number) #line number to string
                    newlist_to_print.append(line_number_as_str) #new list without []

        except AttributeError:
            pass
        #make newlist printable
    newlist_printable = ', '.join(newlist_to_print) #new list without []
    #    #Use printer
    if newlist_printable:
        printer_vuln(newlist_printable, vulnerability_name, vulnerability_description, vulnerability_recommendation, more_info)
    else:
        pass
