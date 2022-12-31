import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup as B
import sys
import faker
f = faker.Faker()

"""
auth = HTTPBasicAuth("Auto", "XLO2 F2EM liMY ild4 9B0R jMMd")


data = {
        "status" : "draft",
        "title" : "Romantic Love Letters For Him Long Distance Quotes",
 
}

headers = {
    "Accept" : "application/json",
    }

url = "https://quotesholy.com/wp-json/wp/v2/posts?slug=6-years-of-friendship-and-still-counting"

r = requests.get(url,headers=headers, auth=auth).json()


#data['content'] = r['content']['raw'] + '\n\n' + "testing"

#r1 = requests.post(url,headers=headers,data=data, auth=auth).json()

print(r)
"""
headers = {
    "user-agent" : f.chrome()
    }

inp = input("fhdhf ")
all_links = []
main_links = []
url = f"https://www.google.com/search?q={inp}"
req = requests.get(url, headers=headers)

print(req)
soup = B(req.text, 'html.parser')

link = soup.find_all('a')

for i in link:
    print(i)

for i in link:
    """    if i['href'].startswith('/url?esrc=s&q=&rct=j&sa=U&url='):
        i = i['href'].replace('/url?esrc=s&q=&rct=j&sa=U&url=', "")
        i = i.split('&')
        all_links.append(i)
"""
    if i['href'].startswith('/url?'):
        i = i['href'].replace('/url?q=', "")
        i = i.split('&')
        all_links.append(i)

for i in all_links:
    if not i[0].startswith('https://support'):
        if not i[0].startswith('https://accounts'):
            if not i[0].startswith('https://www.pinterest'):
            	main_links.append(i[0])

print(main_links)