vulnerability_name = "Use of deprecated now global variable"
vulnerability_description = """Your contract uses now global variable, which is disallowed and removed since 0.7.0 version of Solidity."""
vulnerability_recommendation = """Use block.timestamp instead."""
more_info = ['https://docs.soliditylang.org/en/v0.8.15/070-breaking-changes.html', 'https://docs.soliditylang.org/en/v0.8.17/units-and-global-variables.html']