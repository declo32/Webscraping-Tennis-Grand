# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os
import requests
import shutil

if("Pictures1" not in os.listdir(".")):
	os.mkdir("Pictures1")

proxies = {
  'http': 'http://172.16.114.19:3128',
  'https': 'https://172.16.114.19:3128',
}

url 	= "http://www.atpworldtour.com"
page 	= open("scrape.html")
soup 	= BeautifulSoup(page.read(), "lxml")

avatars = soup.findAll('td', class_="player-avatar-cell")
names	= soup.findAll('td', class_="player-cell")

for i, (avatar_cell, name_cell) in enumerate(zip(avatars, names)):
	avatar 	= avatar_cell.find('img')
	name 	= name_cell.find(text = True)

	print("Working for " + name + " " + str(i))
	
	while(True):
		try:
			response = requests.get(url+avatar['src'], stream=True,proxies=proxies)
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			continue
		break
	with open('Pictures/'+ name +'.png', 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response
