import click
import re
from modules.utils.parse_contract_util import parse_contract
from modules.utils.printer import *
from vulnerabilities_descriptions.integer_underflow_overflow_desc import *


def integer_underflow_overflow(contract):
    r = re.compile('pragma solidity .*(.*)')
    parsed_contract_into_list = parse_contract(contract)
    #print(parsed_contract_into_list)
    newlist = list(filter(r.match, parsed_contract_into_list))
    #print(newlist[0])
    match = re.findall("([0-9]+[.]+[0-9]+[.]+[0-9]+)", newlist[0])
    #print(match[0])
    version = match[0]
    #print(version)
    if int(version[2]) >= 8:
        pass
    else:
        r2 = re.compile('.*using SafeMath for.*')
        newlist2 = list(filter(r2.match, parsed_contract_into_list))
        #check if list is empty

        if newlist2:
            pass
        else:
            printer_vuln_whole_contract(vulnerability_name, vulnerability_description, vulnerability_recommendation, more_info)
            

