vulnerability_name = "Use of deprecated msg.gas function"
vulnerability_description = """Your contract uses msg.gas function, which is disallowed since 0.4.21 version of Solidity."""
vulnerability_recommendation = """Use gasleft() instead."""
more_info = ['https://docs.soliditylang.org/en/v0.4.25/miscellaneous.html#global-variables', 'https://docs.soliditylang.org/en/v0.8.17/units-and-global-variables.html']