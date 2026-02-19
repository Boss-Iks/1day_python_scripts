import requests
import re

def get_html(domain):	
	query = "https://crt.sh/?q="+domain+"&exclude=expired"
	response = requests.get(query)
	print(f"Status: {response.status_code}")	
	
	if response.status_code!= 200:
			return "check the status"		

	pattern = rf'\S+{re.escape(domain)}\S+'
	matching_lines = re.findall(pattern, response.text, re.IGNORECASE)
	clearning_lines = r'<TD>([^<>\r\n]+?)</TD>'	
	domains = []
	for line in matching_lines:
		domains += re.findall(clearning_lines,line,re.IGNORECASE)    
	
	#getting rid of duplicates		
	print("deleting duplicates...")
	domains = list(dict.fromkeys(domains))
	print(f"Found {len(domains)} matches\n")	
	domains = "\n".join(domains)
	return domains  

if __name__ == "__main__":
	domain = input("Enter the domain: ").strip()
	print(get_html(domain))
