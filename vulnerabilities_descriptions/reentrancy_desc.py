vulnerability_name = "Reentrancy"
vulnerability_description = """Reentrancy attack happens, when a function makes an external call to untrusted contracts.
        Attacker may simply call the withdraw function before contract updates its state."""
vulnerability_recommendation = """Avoid using call.value, update bookkeeping state variables before transferring execution to external contract"""
more_info = ['https://consensys.github.io/smart-contract-best-practices/attacks/reentrancy/', 'https://github.com/crytic/not-so-smart-contracts/tree/master/reentrancy','https://hackernoon.com/hack-solidity-reentrancy-attack', 'https://www.securing.pl/pl/reentrancy-attack-in-smart-contracts-is-it-still-a-problem/']