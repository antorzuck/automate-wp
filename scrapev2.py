import requests
from bs4 import BeautifulSoup as B
import faker
import random
from requests.auth import HTTPBasicAuth
import json
import sys
import gen_thumbnail


faker = faker.Faker()
auth = HTTPBasicAuth("Auto", "XLO2 F2EM liMY ild4 9B0R jMMd")


def create_post(ttl, content, thumb, id):
    base_url = f"https://quotesholy.com/wp-json/wp/v2/posts/{id}"
    media_url = "https://quotesholy.com/wp-json/wp/v2/media"

    headers = {
    "Accept" : "application/json",
    }

    data = {
        "status" : "draft",
        "title" : ttl,
        "content" : content,
}
    
    if thumb:
    	file = {"file" : open(f'thumbnail/{thumb}', 'rb')}
    	data1 = {"alt_text" : thumb}
    	res = requests.post(url=media_url,data=data1, files=file, headers=headers, auth=auth)
    	imgid = json.loads(res.content)['id']
    	data["featured_media"] = imgid
    	
    	
    req = requests.post(url=base_url, data=data, headers=headers, auth=auth)


kwlist = []
kw = input("Type keywords: ").split(',')

for x in kw:
    kwlist.append(x)


def get_image_kw(keyword):
    space = keyword.split(' ')
    return str(space[-1])

def create_title(text):
    space = text.split(' ')
    ok = ' '.join(space[0:-1])
    return str(ok.title())



scrape_num = 10

headers = {
    'user-agent': faker.chrome()
}
hdrs = {
    "Accept" : "application/json",
    }

title = ""
body = ""
idofpost = ""

for k in kwlist:
    try:
        print(k)
        draft_url = f"https://quotesholy.com/wp-json/wp/v2/posts?status=draft&search={create_title(k)}"

        rtd = requests.get(draft_url, headers=hdrs, auth=auth).json()


        body += rtd[0]['content']['rendered'] + '\n\n'
        title += rtd[0]['title']['rendered']
        idofpost += str(rtd[0]['id'])

        url = f"https://www.google.com/search?q={title}"

        req = requests.get(url=url)
        print(req)

        soup = B(req.text, 'html.parser')

        link = soup.find_all('a')
        all_links = []
        main_links=[]
        p = ""
        p1 = ""

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
        create_post(id=idofpost, ttl=title, content=body, thumb=gen_thumbnail.twt(name=title, text=get_image_kw(k)))

        title = ""
        body = ""
        idofpost = ""
        print("posted...")
    except:
        title = ""
        body = ""
        idofpost = ""
        with open('failedkw.txt', 'a+') as f:
            f.writelines(k+',')
        print('posting failed. keyword added to the txt file')
