from hashlib import new
import click
import re
from modules.utils.parse_contract_util import parse_contract

<<<<<<< HEAD
# @click.command
# @click.argument('contract', type=click.Path(exists=True), required=1)
def block_timestamp(contract):
=======

def selfdestruct(contract):
>>>>>>> 33503c7b455ee9440537d7d284e98e15563a1f70
    r = re.compile('^.*block\.timestamp.*')
    parsed_contract_into_list = parse_contract(contract)
    newlist = list(filter(r.findall, parsed_contract_into_list))

    if newlist:
<<<<<<< HEAD
        for i in range(len(newlist)):
            print(f"Usage of block.timestamp found at line {1+parsed_contract_into_list.index(newlist[i])}. Avoid using block.timestamp for randomness, as it can be tampered by the miners.")
=======
        i = 0
        for item in newlist:
            print(f"Usage of block.timestamp found at line {1+parsed_contract_into_list.index(newlist[0])}. Avoid using block.timestamp for randomness, as it can be tampered by the miners.")
            i += 1
>>>>>>> 33503c7b455ee9440537d7d284e98e15563a1f70
