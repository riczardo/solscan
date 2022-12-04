vulnerability_name = "Use of delegate call"
vulnerability_description = """Delegate call allows other contracts to modify your contracts storage."""
more_info = ['https://github.com/KadenZipfel/smart-contract-attack-vectors/blob/master/vulnerabilities/delegatecall-untrusted-callee.md', 'https://swcregistry.io/docs/SWC-112']
vulnerability_recommendation = """Avoid using delegate call, or use it only with trusted addresses."""