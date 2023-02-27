import requests
from bs4 import BeautifulSoup as B
import faker
import random
from requests.auth import HTTPBasicAuth
import json
import sys
import gen_thumbnail









faker = faker.Faker()

def create_post(ttl, content, thumb):
    base_url = "https://allpickupliner.xyz/wp-json/wp/v2/posts"
    media_url = "https://allpickupliner.xyz/wp-json/wp/v2/media"

    headers = {
    "Accept" : "application/json",
    }

    auth = HTTPBasicAuth("antor", "NTDZ JK1j frfr tSWf skxG F6U8")
    data = {
        "status" : "draft",
        "title" : ttl,
        "content" : content
}
    
    if thumb:
    	file = {"file" : open(f'thumbnail/{thumb}', 'rb')}
    	data1 = {"alt_text" : thumb}
    	res = requests.post(url=media_url,data=data1, files=file, headers=headers, auth=auth)
    
    	imgid = json.loads(res.content)['id']
    	data["featured_media"] = imgid
    	
    	
    req = requests.post(url=base_url, data=data, headers=headers, auth=auth)
   

kw = str(input("Type keyword: "))

if kw == "blank":
    create_post(ttl=" ", content=" ", thumb=None)
    print("blank created")
    sys.exit()
scrape_num = int(input("How many pages you want to scrape? (limit is 10) "))
q = str(input("Enter a keyword for thumbnail: "))


meta = f"""
These funny, cheesy, dirty, cute {kw} are perfect for anyone looking to add a little romance to their love life.
"""


cons = f"""
<b> Conclusion </b>

We hope you enjoyed our collection of {kw} and found them useful in your dating and social life.

Remember to always use them responsibly and with respect for the other person's feelings. And if you have any {kw} that you think should be added to our collection, feel free to send them our way!

"""

heading = f"""
Looking for some cute, funny, corny,cheesy, yet effective ways to win over your crush? Look no further than these <b>{kw}</b>! Whether you're looking for a cute and flirty way to get someone's attention or a clever icebreaker to break the ice on a first date, these <b>{kw}</b> are sure to make your heart flutter.

From classic favorites to creative new twists, these <b>{kw}</b> are perfect for anyone looking to add a little romance to their love life. So get ready to turn up the charm and sweep your crush off their feet with these swoon-worthy <b>{kw}</b>!
"""


headers = {
    'user-agent': faker.chrome()
}



url = f"https://www.google.com/search?q={kw}"

req = requests.get(url=url)
print(req)
soup = B(req.text, 'html.parser')

link = soup.find_all('a')
all_links = []
main_links=[]
p = ""
p1 = ""
p2= ""
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

    if c == scrape_num:
    	break
    res = requests.get(url=i)
    sp = B(res.text, 'html.parser')
    li = sp.find_all('li')
    if i.startswith('https://benextbrand'):
    	p = sp.find('div', class_='entry-content')
    if i.startswith('https://www.wishesmsg'):
        p1 = sp.find('div', class_='entry-content')
    if i.startswith('https://pickupline'):
    	p2 = sp.find_all('td', class_="column-1")
    	
    	
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
        										body = body + f"<li>{f}</li>" + '\n\n'
    if p:
    	for pt in p.find_all('p')[1:]:
    		if not pt.text in body:
    			body = body + f"<li>{pt.text}</li>" + '\n\n'
    if p1:
        for pt1 in p1.find_all('p')[2:-4]:
            if not pt1.text in body:
                body = body + f"<li>{pt1.text}</li>" + '\n\n'
                
    if p2:
    	for pt2 in p2:
    		if not pt2.text in body:
    			print(pt2.text)
    			body = body + f"<li>{pt2.text}</li>" + '\n\n'
    			


if '"' in body:
	body = body.replace('"', "")
if '“' in body:
	body = body.replace('“', "")
	
if '”' in body:
	body = body.replace('”', "")
	
	
content = heading + '\n\n' + f"<ul>{body}</ul>" + '\n\n' + cons
print("captions collected going to post this shit on wp")
#create_post(ttl=kw.title(), content=content, thumb=gen_thumbnail.create_thumb(name=kw, text=q))
#print("posted...")

if p2:
	print("hi")
