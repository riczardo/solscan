vulnerability_name = "Use of deprecated block.blockhash function"
vulnerability_description = """Your contract uses block.blockhash function, which is deprecated since 0.4.22 version of Solidity and was removed in version 0.5.0."""
vulnerability_recommendation = """Use just blockhash instead."""
more_info = ['https://docs.soliditylang.org/en/v0.4.25/miscellaneous.html#global-variables', 'https://docs.soliditylang.org/en/v0.8.17/units-and-global-variables.html']