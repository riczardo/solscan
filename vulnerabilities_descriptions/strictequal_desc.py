vulnerability_name = "Strict equality"
vulnerability_description = """Using strict equality to for example check if specific threshold is reached might lead to unintended behaviour."""
vulnerability_recommendation = """Specify which of three available visibilities of variables are appropriate for your contract."""
more_info = ['https://github.com/crytic/slither/wiki/Detector-Documentation#dangerous-strict-equalities',
             'https://github.com/KadenZipfel/smart-contract-attack-vectors/blob/master/vulnerabilities/unexpected-ether-balance.md', 'https://swcregistry.io/docs/SWC-132']
