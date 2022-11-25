from hashlib import new
import click
import re
from modules.utils.parse_contract_util import parse_contract

# @click.command
# @click.argument('contract', type=click.Path(exists=True), required=1)
def block_timestamp(contract):
    r = re.compile('^.*\d{7,}.*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.findall, parsed_contract_into_list))

    if newlist:
        for i in range(len(newlist)):
            print(f"Multidigit number found at line {1+parsed_contract_into_list.index(newlist[i])}. Make sure that it is correct, as such literal conversions are prone to mistakes.")
