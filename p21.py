import requests
from bs4 import BeautifulSoup

def print_to_text(base_url,filename):
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text)
    with open(filename, "w") as textfile:
        for paragraph in soup.find_all(dir="ltr"):
            textfile.write(paragraph.text.replace("<span>",""))

if __name__ == "__main__":

    base_url = "http://www.theatlantic.com/business/archive/2014/08/to-work-better-work-less/375763/"
    base_url2 = "http://www.theatlantic.com/business/archive/2014/08/to-work-better-work-less/375763/2/"
    filename = input("Please enter file name : ")
    print_to_text(base_url,filename)
    print_to_text(base_url2,filename)