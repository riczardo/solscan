vulnerability_name = "Use of deprecated throw function"
vulnerability_description = """Your contract uses throw function, which is disallowed in newer versions of Solidity."""
vulnerability_recommendation = """Depending on purpose, use revert, require and assert instead."""
more_info = ['https://docs.soliditylang.org/en/v0.8.17/050-breaking-changes.html#functions', 'https://docs.soliditylang.org/en/v0.8.17/units-and-global-variables.html']