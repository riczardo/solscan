vulnerability_name = "Arbitrary from in transferfrom"
vulnerability_description = """From parameter in transferFrom is using arbitrary from parameter, this may lead to losing funds."""
vulnerability_recommendation = """Use msg.sender as from parameter in transferFrom."""
more_info = ['https://github.com/crytic/slither/wiki/Detector-Documentation#arbitrary-from-in-transferfrom',
             'https://veridelisi.medium.com/learn-erc20-in-solidity-transferfrom-function-ceb0a304163']
