from modules.utils.remove_comments import sanitize

def parse_contract(contract) -> str:
    sanitized_contract = sanitize(contract)
    tmp_file = open("./uncommented.txt", "w")
    tmp_file.write(sanitized_contract)
    tmp_file.close()


    with open("./uncommented.txt", 'r', encoding="utf-8") as f:
        lines = f.readlines()
    return lines
    