import re

def sanitize(contract):
    contract_without_multiline_comments = remove_multiline_comments(contract) #put contract into multiline function

    contract_without_any_comments = remove_oneline_comments(contract_without_multiline_comments) #put partialy sanitized contract through next function
    return contract_without_any_comments




    


def remove_oneline_comments(contract_without_multiline_comments):
    updated_contract = contract_without_multiline_comments
    r_newline_comment = re.compile('\/\/.*')
    contract_without_singleline_comments = re.sub(r_newline_comment, "singleline comment", updated_contract)

    return contract_without_singleline_comments





def remove_multiline_comments(contract):
    with open(contract, 'r') as f:
        updated_contract = f.read()
        #we need flag specifing that contract has multiline comments. If it doesnt, we skip the process.
        while True:
            r_multiline_comment_check = re.compile('\/\*(.|[\r\n])*?\*\/')
            comment_isthere = r_multiline_comment_check.search(updated_contract)

            if comment_isthere:
                it_there_a_multiline_comment = True
            else:
                it_there_a_multiline_comment = False
                break


            r_multiline_comment = re.compile('\/\*(.|[\r\n])*?\*\/')
            comment = r_multiline_comment.search(updated_contract)
            comment_group = comment.group() #find first occurence of multiline comment

            r2 = re.findall("\n", comment_group) #determine how many lines does the comment takes
            amount_of_lines_to_replace = len(r2)
            string_to_inject_in_comment_place = amount_of_lines_to_replace * "multiline comment removed\n" #prepare string to inject

            tmp_contract = re.sub(r_multiline_comment, string_to_inject_in_comment_place, updated_contract,1) #replace FIRST occurence 
                                                                                                                #with prepared string
            updated_contract = tmp_contract
        #print(updated_contract)
    return updated_contract
            


        


