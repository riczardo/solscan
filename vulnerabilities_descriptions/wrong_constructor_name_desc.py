vulnerability_name = "Wrong constructor name"
vulnerability_description = """Your contract name seems to differ from constructor name.
        This may lead to contract becoming regular function in compiler versions up to 0.4.22."""
more_info = ['https://github.com/KadenZipfel/smart-contract-attack-vectors/blob/master/vulnerabilities/incorrect-constructor.md', 'https://swcregistry.io/docs/SWC-118']
vulnerability_recommendation = """Although modern versions of Solidity implement constructor keyword for defining, 
        it is still a good practice to name it same as filename."""