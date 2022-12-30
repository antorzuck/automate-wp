import requests
from requests.auth import HTTPBasicAuth


auth = HTTPBasicAuth("Auto", "XLO2 F2EM liMY ild4 9B0R jMMd")


data = {
        "status" : "draft",
        "title" : "Romantic Love Letters For Him Long Distance Quotes",
 
}

headers = {
    "Accept" : "application/json",
    }

url = "https://quotesholy.com/wp-json/wp/v2/posts?status=draft&type=post"

r = requests.get(url,headers=headers, auth=auth).json()


#data['content'] = r['content']['raw'] + '\n\n' + "testing"

#r1 = requests.post(url,headers=headers,data=data, auth=auth).json()

print(r)