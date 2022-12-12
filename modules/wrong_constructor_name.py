import click
import re
from modules.utils.parse_contract_util import parse_contract
import ntpath # solves problem off full path or test catalog issue
from modules.utils.printer import *
from vulnerabilities_descriptions.wrong_constructor_name_desc import *


def wrong_constructor_name(contract):
    #contract_name_with_extension = ntpath.basename(contract) # ./test/Reentrancy.sol -> Reentrancy.sol
    #contract_name = contract_name_with_extension.split('.')[0] # Reentrancy.sol -> Reentrancy   
    #
    r1 = re.compile('contract(.*?){', re.IGNORECASE)
    r3 = re.compile('.*constructor(.*).*', re.IGNORECASE)
    parsed_contract_into_list2 = parse_contract(contract)
    parsed_contract_into_list3 = parse_contract(contract)
    newlist2 = list(filter(r1.match, parsed_contract_into_list2))
    newlist3 = list(filter(r3.match, parsed_contract_into_list3))
    #print(newlist3)
    if newlist3:
        return
    else:
        pass
    if newlist2:
        contract_name_b = newlist2[0]
        contract_name_b_2 = contract_name_b.split('{')
        contract_name_b_3 = contract_name_b_2[0]
        contract_name_b_4 = contract_name_b_3.split(' ')
        contract_name = contract_name_b_4[1]
    else:
        return
    #print(contract_name)
    r = re.compile('^.*function {}\(.*\)'.format(contract_name), re.IGNORECASE)
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    #print(newlist)

    #===================================================================== 
    #check if list is empty == not proper constructor name

    if not newlist:
        #print(f"A contract probably uses bad constructor name - \"{contract_name}()\" function is misssing")
        printer_vuln_whole_contract(vulnerability_name, vulnerability_description, vulnerability_recommendation, more_info)
    else:
        pass

