vulnerability_name = "Use of tx.origin for authentication"
vulnerability_description = """Tx.origin should not be used for authentication purposes. 
        It is vulnerable to phishing attacks."""
more_info = ['https://hackernoon.com/hacking-solidity-contracts-using-txorigin-for-authorization-are-vulnerable-to-phishing', 'https://medium.com/coinmonks/solidity-tx-origin-attacks-58211ad95514']
vulnerability_recommendation = """Use msg.sender instead."""