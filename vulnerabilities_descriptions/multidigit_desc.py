vulnerability_name = "Multidigit numbers"
vulnerability_description = """Your contract contains multi-digit numbers."""
vulnerability_recommendation = """Be sure to check that it is correct, such conversion often lead to mistakes. Solidity has some specific units to specify tokens, time etc."""
more_info = ['https://docs.soliditylang.org/en/latest/units-and-global-variables.html#ether-units',
             'https://github.com/crytic/slither/wiki/Detector-Documentation#too-many-digits']
