vulnerability_name = "Variable default visibility"
vulnerability_description = """Not defining visibility of a function results in using default value - public.
        This might allow malicious users to make unintended state changes to the contract."""
vulnerability_recommendation = """Specify which of three available visibilities of variables are appropriate for your contract."""
more_info = ['https://medium.com/coinmonks/visibility-in-solidity-e758a4739c95',
             'https://github.com/KadenZipfel/smart-contract-attack-vectors/blob/master/vulnerabilities/state-variable-default-visibility.md', 'https://www.alchemy.com/overviews/solidity-function-visibility']
