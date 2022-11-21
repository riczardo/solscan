from termcolor import colored, cprint
#from modules.vulnerabilities_descriptions import *



def printer_vuln(line_num_arg, vuln_name_arg, vuln_description_arg, vuln_more_info_links, recommendation_arg, recommendations_more_info_links):
    #line_num = 1+parsed_contract_into_list.index(newlist[line_num_arg])
    #line_num = 1
    line_number = colored(str(line_num_arg), "red", attrs=["bold"])
    vuln_name = colored(vuln_name_arg, "red", attrs=["bold"])
    vuln_found = vuln_name + ' vulnerability found at line: ' + str(line_number)
    vuln_description = colored("Description:", "green", attrs=["bold"]) + "\n" + colored("	" + vuln_description_arg, "grey", attrs=["bold"])
    vuln_more_info = colored("	More info:", "yellow", attrs=["concealed"]) + "\n" 
    recommendation = colored("Recommendation:", "green", attrs=["bold"]) + "\n" + colored("	" + recommendation_arg, "cyan", attrs=['dark'])
    recommendation_more_info = colored("	More info:", "yellow", attrs=["concealed"])
    text_1 = vuln_found + "\n" + vuln_description + "\n" + vuln_more_info.strip()   
    text_2 = recommendation + "\n" + recommendation_more_info
    print(text_1)
    for link in vuln_more_info_links:
        print("	* " + link)
    print(text_2)
    for link in recommendations_more_info_links:
        print("	* " + link)
    print("\n")


#Usage:
#printer_vuln(i, vulnerabilities_descriptions.example_vuln.vulnerability_name, example_vuln.vulnerability_description, example_vuln.vulnerability_more_info_links, example_vuln.vulnerability_recommendation, example_vuln.vulnerability__description_more_info_links)
#printer_vuln(4, vulnerability_name, vulnerability_description, vulnerability_more_info_links, vulnerability_recommendation, vulnerability__description_more_info_links)
