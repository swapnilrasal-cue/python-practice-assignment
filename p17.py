import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html,'html.parser')

for heading in soup.find_all("h2"): 
    if heading: 
        print(heading.text.replace("\n", " ").strip())
    else: 
        print(heading.contents[0].strip())
