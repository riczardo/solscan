vulnerability_name = "Unchecked external call"
vulnerability_description = """Using send() external call may be an attack surface."""
more_info = ['https://github.com/KadenZipfel/smart-contract-attack-vectors/blob/master/vulnerabilities/unchecked-call-return-value.md', 'https://coinsbench.com/unchecked-return-value-in-smart-contracts-providing-an-attack-surface-dab2eed64251', 'https://dev.to/kamilpolak/hack-solidity-unchecked-call-return-value-7og']
vulnerability_recommendation = """It is recommended to use transfer rather than send, 
        low level calls like send allow further execution even if the function fails."""