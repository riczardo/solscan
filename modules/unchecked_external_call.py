import click
import re
from modules.utils.parse_contract_util import parse_contract

# @click.command
# @click.argument('contract', type=click.Path(exists=True), required=1)
def unchecked_external_call(contract):
    r = re.compile('^.*\.send\(.*\).*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.match, parsed_contract_into_list))
    if newlist:
        for i in range(len(newlist)):
            print(f"A contract uses an unchecked send() external call at line {1+parsed_contract_into_list.index(newlist[i])}")

