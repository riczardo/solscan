import click
import re
from modules.utils.parse_contract_util import parse_contract
from modules.utils.printer import *
from vulnerabilities_descriptions.example import *


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
        #print('check smartmath in use')
        r2 = re.compile('.*using SafeMath for.*')
        newlist2 = list(filter(r2.match, parsed_contract_into_list))
        #check if list is empty
        #print(newlist2)
        if newlist2:
            pass
            #no vuln
        else:
            print('Probably int overflow/underflow in contract. The defined pragma is below 0.8.* version and there is no use of safeMath library.')
            
    #if newlist:
    #    print(f"integer found at line {1+parsed_contract_into_list.index(newlist[0])}")
