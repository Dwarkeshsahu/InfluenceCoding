# !/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Author: Dwarika 
# @Env: python 3.6 
# @Github: https://github.com/Dwarkeshsahu/InfluenceCoding 

from bs4 import BeautifulSoup
import requests
page = requests.get(
	"https://www.scorespro.com/rss2/live-cricket.xml")

soup = BeautifulSoup(page.content, 'html.parser')

score = soup.find_all('title')[2].get_text()
print(score)
