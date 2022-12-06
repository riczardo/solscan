vulnerability_name = "Function default visibility"
vulnerability_description = """Not defining visibility of a function results in using default value - public.
        This might allow malicious users to make unintended state changes to the contract."""
vulnerability_recommendation = """Specify which of four available visibilities of function are appropriate for yours."""
more_info = ['https://github.com/sigp/solidity-security-blog#visibility',
             'https://www.ajaypalcheema.com/function-visibility-in-solidty/', 'https://www.alchemy.com/overviews/solidity-function-visibility']
