vulnerability_name = "Assert violation"
vulnerability_description = """Assert function found in contract. This might lead to bugs and unexpected behaviours."""
vulnerability_recommendation = """Assert function should be unreachable by code. Assert() should only check invariant conditions, if the condition is not invariant, use require()."""
more_info = ['https://swcregistry.io/docs/SWC-110?fbclid=IwAR0auxuUGdQCJ1ginFbNWqOVvVM85q5apxXj-xktNRLfFoeG3BkMOFScpTo',
             'https://media.consensys.net/when-to-use-revert-assert-and-require-in-solidity-61fb2c0e5a57']
