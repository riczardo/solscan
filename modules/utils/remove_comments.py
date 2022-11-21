from modules.utils.parse_contract_util import parse_contract
import re

def sanitize(contract):
    cleaned_from_multiline_comments = remove_multiline_comment(contract)
    #print(cleaned_from_multiline_comments)
    parsed_contract_into_list = parse_contract(cleaned_from_multiline_comments)
    print(parsed_contract_into_list)
    #remove_one_line_comment(contract)

    




def remove_one_line_comment(contract):
    r_newline_comment = re.compile('^.*\/\/.*')
    newlist = list(filter(r_newline_comment.findall, sanitize.parsed_contract_into_list))

    for i in range(len(newlist)):
        line_number = sanitize.parsed_contract_into_list.index(newlist[i])
        sanitize.parsed_contract_into_list[line_number] = "removed singleline comment \n"

def remove_multiline_comment(contract):
    with open(contract, 'r') as f:
        data = f.read()

        r_multiline_comment = re.compile('\/\*(.|[\r\n])*?\*\/')
        comment = r_multiline_comment.search(data)
        x = comment.group()
        r2 = re.findall("\n", x)

        amount_of_lines = len(r2)
        string_to_inject = amount_of_lines*"removed multiline comment\n"
        y = re.sub(r_multiline_comment, string_to_inject, data)
        return y


