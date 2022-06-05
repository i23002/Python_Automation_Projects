import requests

from bs4 import BeautifulSoup

import datetime


print("Starting....")

URL = 'https://timesofindia.indiatimes.com/india'



print("Gathering the Headlines...")


def TimesOfIndia(url):
    lis = list()
    response_from_server = requests.get(url)
    scrape = BeautifulSoup(response_from_server.content,'lxml')
    headings = scrape.find_all('span' , attrs={'class':'w_tle'})
    
    
    
    for heading in headings:
        lis.append(heading.text)
     
    
    lis = [i for i in lis if len(i.split()) == 8 or len(i.split()) > 8]
    return lis 

actual_content = TimesOfIndia(URL)

print("HERE ARE THE HEADLINES YOU HAVE REQUESTED...  " , end="  ")
print(datetime.datetime.now())
print("\n")

print("TODAYS HEADLINES: ")
for i in range(len(actual_content)):
    print(str(i)+" : "+actual_content[i])

print("Have a good day ")
    
