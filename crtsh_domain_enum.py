import requests
import re

def get_html(domain):
	query = "https://crt.sh/?q="+domain+"&exclude=expired"
	response = requests.get(query)
	print(f"Status: {response.status_code}")		
	response = response.text
	pattern = rf'\S+{re.escape(domain)}\S+'
	matching_lines = re.findall(pattern, response, re.IGNORECASE)
	clearning_lines = r'<TD>([^<>\r\n]+?)</TD>'	
	domains = []
	for line in matching_lines:
		domains += re.findall(clearning_lines,line,re.IGNORECASE)    
	#getting rid of duplicates	
	j =1
	for i in range(len(domains)-1):		
		for j in range(len(domains)-2):
			if domains[i] == domains[j]:
				domains.pop(j)
	print(f"Found {len(domains)} matches")
	domains = "\n".join(domains)
	return domains  

if __name__ == "__main__":
    domain = input("Enter the domain: ").strip()
    if domain:
        print(get_html(domain))
    else:
        print("No domain entered.")
