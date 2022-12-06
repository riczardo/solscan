vulnerability_name = "Integer overflow/underflow"
vulnerability_description = """In Solidity up to 0.8 version it is possible to underflow or overflow integers.
        That means if you add 1 to 255, it will come up as 0. Similarly, decreasing 255 by 1 will output 0."""
more_info = ['https://hackernoon.com/hack-solidity-integer-overflow-and-underflow', 'https://valid.network/post/integer-overflow-in-ethereum']
vulnerability_recommendation = """Use newer compiler version (since 0.8 version overflows/underflows are automatically checked)."""