vulnerability_name = "Stored credentials"
vulnerability_description = """It seems that your contract is storing credentials. Although it might be a false positive, be sure to check."""
vulnerability_recommendation = """You should not store credentials in a contract for authentication purposes. Use msg.sender instead."""
more_info = ['https://ludu.co/course/ethereum/metamask-authentication/', 'https://docs.soliditylang.org/en/v0.8.16/introduction-to-smart-contracts.html']