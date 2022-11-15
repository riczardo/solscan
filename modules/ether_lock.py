import click
import re
from modules.utils.parse_contract_util import parse_contract

# @click.command
# @click.argument('contract', type=click.Path(exists=True), required=1)
def ether_lock(contract):
    r = re.compile('^.*function.*payable.*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    print(newlist)
    if newlist:
        r2 = re.compile('\.transfer\(.*\)|\.call\(.*\)|\.send\(.*\)')
        withdrawal_functions = list(filter(r2.match, parsed_contract_into_list))
        if not withdrawal_functions:
            for i in range(len(newlist)):
                print(f"It appears that contract has payable function at line {1+parsed_contract_into_list.index(newlist[0])}, but has no functionality to withdraw it. That causes indefinetly locking up your Ether. ")



        