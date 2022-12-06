vulnerability_name = "Multiple constructor schemes"
vulnerability_description = """Contract uses multiple constructors. 
        In Solidity version 0.4.22 contract with eg. 2 constructos. will compile, 
        and the first constructor will overtake precedence over the first one."""
vulnerability_recommendation = """Declare only one constructor, using new scheme."""
more_info = ['https://www.tutorialspoint.com/solidity/solidity_constructors.htm',
             'https://www.geeksforgeeks.org/solidity-constructors/']
