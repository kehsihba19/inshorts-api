import requests
from bs4 import BeautifulSoup as bs

def getdata(value):
	try:
		if(value=='all'):
			r=requests.get("https://inshorts.com/en/read").text
		else:
			r=requests.get(f"https://inshorts.com/en/read/{value}").text
		soup=bs(r,'lxml')
		x=soup.find_all('div',class_="news-card z-depth-1")
		val={}
		val["data"]=[]
		for i in range(0,len(x)):
			dic={}
			dic["title"]=x[i].find('span', itemprop="headline").text
			dic["decription"]=x[i].find('div',itemprop="articleBody").text
			dic["images"]=x[i].find('div', class_="news-card-image")['style'].split("url(")[1].split(")")[0].replace("'",'')
			dic["author"]=x[i].find('span',class_='author').text
			dic["time"]=x[i].find('span', class_="time").attrs["content"]
			dic["inshorts-link"]=x[i].find('span',content="")['itemid']
			if(x[i].find('a', class_="source")==None):
				dic["read-more"]="None"
			else:
				dic["read-more"]=x[i].find('a', class_="source").attrs['href']
			val["data"].append(dic)
		val["category"]=value
		val["count-articles"]=len(x)
		return val
	except Exception as e:
		return {"status":False,"error":e}