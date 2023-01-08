from termcolor import colored, cprint




def printer_vuln(line_num_arg, vuln_name_arg, vuln_description_arg, recommendation_arg, more_info_links):
    #line_num = 1+parsed_contract_into_list.index(newlist[line_num_arg])
    #line_num = 1
    #line_number = colored(str(line_num_arg), "red", attrs=["bold"])
    line_number = colored(str(line_num_arg), "red", attrs=["bold"])
    vuln_name = colored(vuln_name_arg, "red", attrs=["bold"])
    vuln_found = vuln_name + ' vulnerability found at line: ' + str(line_number)
    vuln_description = colored("Description:", "green", attrs=["bold"]) + "\n" + colored("	" + vuln_description_arg, "grey", attrs=["bold"])
    #vuln_more_info = colored("	More info:", "yellow", attrs=["concealed"]) + "\n" 
    recommendation = colored("Recommendation:", "green", attrs=["bold"]) + "\n" + colored("	" + recommendation_arg, "cyan", attrs=['dark'])
    more_info = colored("More info:", "yellow", attrs=["bold"])
    text = vuln_found + "\n" + vuln_description + "\n" + recommendation + "\n" + more_info
    print(text)
    for link in more_info_links:
        print("	* " + link)
    print("\n")


#example printable line:
#print line number in one line
#line_nums = [11, 15, 78]
#ln_b = []
#for i in line_nums:
#    x = str(i)
#    ln_b.append(x)
#ln = ', '.join(ln_b)
#Usage:
#printer_vuln(i, vulnerabilities_descriptions.example_vuln.vulnerability_name, example_vuln.vulnerability_description, example_vuln.vulnerability_more_info_links, example_vuln.vulnerability_recommendation, example_vuln.vulnerability__description_more_info_links)
#printer_vuln(4, 'reentrancy', 'it is vuln', 'fix it', ['aaa.pl', 'sdgsdfg.pl'])
#printer_vuln(ln, 'reentrancy', 'it is vuln', 'fix it', ['aaa.pl', 'sdgsdfg.pl'])


def printer_vuln_whole_contract(vuln_name_arg, vuln_description_arg, recommendation_arg, more_info_links):
    #line_num = 1+parsed_contract_into_list.index(newlist[line_num_arg])
    #line_num = 1
    #line_number = colored(str(line_num_arg), "red", attrs=["bold"])
    #line_number = colored(str(line_num_arg), "red", attrs=["bold"])
    vuln_name = colored(vuln_name_arg, "red", attrs=["bold"])
    vuln_found = vuln_name + ' vulnerability found in contract'
    vuln_description = colored("Description:", "green", attrs=["bold"]) + "\n" + colored("	" + vuln_description_arg, "grey", attrs=["bold"])
    #vuln_more_info = colored("	More info:", "yellow", attrs=["concealed"]) + "\n" 
    recommendation = colored("Recommendation:", "green", attrs=["bold"]) + "\n" + colored("	" + recommendation_arg, "cyan", attrs=['dark'])
    more_info = colored("More info:", "yellow", attrs=["bold"])
    text = vuln_found + "\n" + vuln_description + "\n" + recommendation + "\n" + more_info
    print(text)
    for link in more_info_links:
        print("	* " + link)
    print("\n")