
def parse_contract(contract) -> str:
    with open(contract, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    return lines