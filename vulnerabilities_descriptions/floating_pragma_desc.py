vulnerability_name = "Floating pragma"
vulnerability_description = """Floating pragma was found in the first line of smart contract.
        This can cause contract to compile under compiler version with security bugs."""
vulnerability_recommendation = """Use strict pragma, with version of compiler that is neither too old or too recent"""
more_info = ['https://www.immunebytes.com/blog/floating-pragma/', 'https://blog.solidityscan.com/understanding-solidity-pragma-and-its-security-practices-3b5458763a34']