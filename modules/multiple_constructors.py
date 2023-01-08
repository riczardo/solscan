import click
import re
from modules.utils.parse_contract_util import parse_contract
from modules.utils.printer import *
from vulnerabilities_descriptions.multiplecons_desc import *


def multiple_constructors(contract):
 
    #Check if there is function with the same name as defined contract
    r1 = re.compile('contract(.*?){', re.IGNORECASE)
    parsed_contract_into_list2 = parse_contract(contract)
    newlist2 = list(filter(r1.match, parsed_contract_into_list2))
    contract_name_b = newlist2[0]
    contract_name_b_2 = contract_name_b.split('{')
    contract_name_b_3 = contract_name_b_2[0]
    contract_name_b_4 = contract_name_b_3.split(' ')
    contract_name = contract_name_b_4[1]

    r = re.compile('^.*function {}\(.*\)'.format(contract_name), re.IGNORECASE)
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))


    if not newlist:
        #check if there is constructor() in use
        r_constructor = re.compile('.* constructor() .*', re.IGNORECASE)
        parsed_contract_into_list_constructor = parse_contract(contract)
        newlist_constructor = list(filter(r_constructor.match, parsed_contract_into_list_constructor))
        if newlist_constructor:
            pass

        else:
            pass

    else:
        #check if there is constructor() in use because if it is it is vulnerability
        r_constructor = re.compile('.*constructor().*', re.IGNORECASE)
        parsed_contract_into_list_constructor = parse_contract(contract)
        newlist_constructor = list(filter(r_constructor.match, parsed_contract_into_list_constructor))
        if newlist_constructor:

            printer_vuln_whole_contract(vulnerability_name, vulnerability_description, vulnerability_recommendation, more_info)
        else:
            pass
            print('There is only constructor in old style - valid')
        
              