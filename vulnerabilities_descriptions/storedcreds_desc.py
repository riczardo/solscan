vulnerability_name = "Probably stored credentials"
vulnerability_description = """It seems that your contract might be storing credentials. Be sure to check."""
vulnerability_recommendation = """You should not store credentials in a contract for authentication purposes. Use msg.sender instead. 
        This check scans your code for 1000 most popular passwords, so it may result in false positives."""
more_info = ['https://ludu.co/course/ethereum/metamask-authentication/', 'https://docs.soliditylang.org/en/v0.8.16/introduction-to-smart-contracts.html']