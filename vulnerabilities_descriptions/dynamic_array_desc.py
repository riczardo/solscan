vulnerability_name = "Dynamic array length"
vulnerability_description = """Dynamic array length is declared in the conract. This may lead to bugs in execution."""
vulnerability_recommendation = """Do not allow array length to be set. Instead, add values ass needed."""
more_info = ['https://blog.soliditylang.org/2020/10/07/solidity-dynamic-array-cleanup-bug/', 'https://hackernoon.com/maliciously-manipulate-storage-variables-in-solidity-a-how-to-guide-489r320e']