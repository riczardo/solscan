vulnerability_name = "Insecure randomness source"
vulnerability_description = """Be sure you do not use functions blockhash, block.timestamp and block.difficulty as source of your randomness.
        These function aren't supposed to be used that way."""
vulnerability_recommendation = """You can use Chainlink VRF for example."""
more_info = ['https://docs.chain.link/vrf/v2/introductionc',
             'https://coinsbench.com/insecure-source-of-randomness-hack-solidity-6-96860bd88ed3']
