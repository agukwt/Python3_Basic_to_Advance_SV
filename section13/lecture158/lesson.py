#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.python.org')
# print(html.text)

soup = BeautifulSoup(html.text, 'lxml')

title = soup.find_all('title')
print(title[0].text)

intro = soup.find_all('div', {'class': 'introduction'})
print(intro[0].text)
