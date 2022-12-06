vulnerability_name = "Use of deprecated callcode function"
vulnerability_description = """Your contract uses callcode function, which is disallowed since 0.5.0 version of Solidity."""
vulnerability_recommendation = """Use delegatecall instead (but still be cautious)."""
more_info = ['https://docs.soliditylang.org/en/v0.8.17/050-breaking-changes.html', 'https://docs.soliditylang.org/en/v0.8.17/units-and-global-variables.html']