import requests
from bs4 import BeautifulSoup as B
from my_fake_useragent import UserAgent
import random
from requests.auth import HTTPBasicAuth
import json
import sys
import gen_thumbnail


def create_post(ttl, content, thumb):
    base_url = "https://quotesholy.com/wp-json/wp/v2/posts"
    media_url = "https://quotesholy.com/wp-json/wp/v2/media"

    headers = {
    "Accept" : "application/json",
    }

    auth = HTTPBasicAuth("Auto", "XLO2 F2EM liMY ild4 9B0R jMMd")
    data = {
        "status" : "draft",
        "title" : ttl,
        "content" : content,
}
    alt = thumb
    if "-" in alt:
        alt = alt.replace("-"," ")
    if ".jpg" in alt:
        alt = alt.replace(".jpg","")
   
    if thumb:
    	file = {"file" : open(f'thumbnail/{thumb}', 'rb')}
    	data1 = {"alt_text" : alt}
    	res = requests.post(url=media_url,data=data1, files=file, headers=headers, auth=auth)
    	imgid = json.loads(res.content)['id']
    	data["featured_media"] = imgid
    	
    	
    req = requests.post(url=base_url, data=data, headers=headers, auth=auth)
   
kwlist = []
kw = kwlist.append(input("Type keyword: ").split(','))

def get_image_kw(keyword):
    space = keyword.split(' ')
    return str(space[-1])

def create_title(text):
    space = text.split(' ')
    ok = ' '.join(space[0:-1])
    return str(ok.title())



def user_agent():
    browser = ['chrome','firefox','edge','ie','opera','safari']
    os = ['windows','linux','mac','ios','chrome os']
    ua = UserAgent(family=random.choice(browser), os_family=random.choice(os))
    return str(ua.random)

headers = {
    'user-agent': user_agent()
}


for k in kwlist[0]:
    print(k)    
    url = f"https://www.google.com/search?q={create_title(k)}"
 
    req = requests.get(url=url, headers=headers)
    print(req)
    soup = B(req.text, 'html.parser')

    link = soup.find_all('a')
    all_links = []
    main_links=[]
    p = ""
    p1 = ""
    body = ""
    for i in link:
        if i['href'].startswith('/url?'):
            i = i['href'].replace('/url?q=', "")
            i = i.split('&')
            all_links.append(i)

    for i in all_links:
        if not i[0].startswith('https://support'):
            if not i[0].startswith('https://accounts'):
                if not i[0].startswith('https://www.pinterest'):
                    main_links.append(i[0])

    for c,i in enumerate(main_links):
        res = requests.get(url=i)
        sp = B(res.text, 'html.parser')
        li = sp.find_all('li')
        if i.startswith('https://benextbrand'):
            p = sp.find('div', class_='entry-content')
        if i.startswith('https://www.wishesmsg'):
            p1 = sp.find('div', class_='entry-content')
        for l in li:
            if not l.attrs:
                if len(l.text.strip()) > 20:
                    f = l.text.strip()
                    if not 'Caption' in f:
                        if not 'Instagram' in f:
                            if not 'Facebook' in f:
                                if not 'Status' in f:
                                    if not 'Best' in f:
                                        if not 'Message' in f:
                                            if not 'Quotes' in f:
                                                if not f in body:
                                                    body = body + f + '\n'
        if p:
            for pt in p.find_all('p')[1:]:
                if not pt.text in body:
                    body = body + pt.text + '\n'
        if p1:
            for pt1 in p1.find_all('p')[2:-4]:
                if not pt1.text in body:
                    body = body + pt1.text + '\n'

   
    if '"' in body:
        body = body.replace('"', "")
    if '“' in body:
        body = body.replace('“', "")
        
    if '”' in body:
        body = body.replace('”', "")

    print("captions collected going to post this shit on wp")
    create_post(ttl=create_title(k), content=body, thumb=gen_thumbnail.create_thumb(name=create_title(k), text=get_image_kw(k)))
    print("posted...")
