import click
import re
from modules.utils.parse_contract_util import parse_contract
from modules.utils.printer import *
from vulnerabilities_descriptions.funcdefvis import *


def function_default_visibility(contract):
    r = re.compile('.*function .*\(.*\).*') # teraz nie sprawdza czy np. address[3] calldata admins, czaddress[] calldata admins, bo jak [] to jest vuln
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    #make newlist printable 
    newlist_to_print = []
    # try statement
    for i in range(len(newlist)):
        #if czy jest zdefiniowany rodzaj funkcji
        #print(len(newlist[0]))
        #if 
        try:
            found = re.search('function .*(.*?).*', newlist[i]).group(0)
            #print(found)
            splited_words = found.split()
            #if czy zdefiniowano rodzaj funkcji
            #print(len(splited_words))
            if len(splited_words) < 3:
                #print ('jest vuln na 100%')
                line_number = 1+parsed_contract_into_list.index(newlist[i]) #line number
                line_number_as_str = str(line_number) #line number to string
                newlist_to_print.append(line_number_as_str) #new list without []
            else:
                #print('good')
                #print(splited_words[2])
                #we have to check
                if splited_words[2] == 'public' or splited_words[2] == 'private' or splited_words[2] == 'external' or splited_words[2] == 'internal' or splited_words[2] == 'public{' or splited_words[2] == 'private{' or splited_words[2] == 'external{' or splited_words[2] == 'internal{':
                    pass
                    #print('good defined')
                else:
                    #print('jest vuln')
                    line_number = 1+parsed_contract_into_list.index(newlist[i]) #line number
                    line_number_as_str = str(line_number) #line number to string
                    newlist_to_print.append(line_number_as_str) #new list without []
            #print(splited_words)
            #print(splited_words[2])
        except AttributeError:
            pass
        #make newlist printable
    newlist_printable = ', '.join(newlist_to_print) #new list without []
    #    #Use printer
    if newlist_printable:
        printer_vuln(newlist_printable, vulnerability_name, vulnerability_description, vulnerability_recommendation, more_info)
    else:
        pass
