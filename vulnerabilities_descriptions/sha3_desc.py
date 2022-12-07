vulnerability_name = "Use of deprecated sha3 function"
vulnerability_description = """Your contract uses sha3 function, which was removed in 0.5.0 version of Solidity."""
vulnerability_recommendation = """Use keccak256 instead."""
more_info = ['https://docs.soliditylang.org/en/v0.8.17/050-breaking-changes.html', 'https://docs.soliditylang.org/en/v0.8.17/units-and-global-variables.html']