vulnerability_name = "Ethereum lock"
vulnerability_description = """It appears your contract has a payable function, but no withdrawal."""
vulnerability_recommendation = """Implement withdrawal function, or don't use payable attribute."""
more_info = ['https://github.com/crytic/slither/wiki/Detector-Documentation#contracts-that-lock-ether', 'https://ethereum.stackexchange.com/questions/134323/if-the-smart-contract-does-not-include-the-withdrawal-function-will-that-ether']