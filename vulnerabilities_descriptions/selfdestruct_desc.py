vulnerability_name = "Self destruct"
vulnerability_description = """You should be using self destruct very cautiously.
        Improper implementation may lead to locking funds, or losing them"""
more_info = ['https://github.com/KadenZipfel/smart-contract-attack-vectors/blob/master/vulnerabilities/unprotected-selfdestruct.md', 'https://hackernoon.com/how-to-hack-smart-contracts-self-destruct-and-solidity']
vulnerability_recommendation = """Do not use self destruct, use it only if you feel comfortable using it."""