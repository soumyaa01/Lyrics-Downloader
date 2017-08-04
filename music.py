import os
import requests
import bs4
import re
import urllib
from bs4 import BeautifulSoup
def lyric(song,artist):
	addr = 'http://www.metrolyrics.com/%s-lyrics-%s.html' % (song,artist)
	url=requests.get(addr)
	lyrics= None
	soup = BeautifulSoup(url.content,'html.parser')
	lyrics = soup.findAll('p', class_='verse')
	lyr= [] 
	filename = song + ' - ' + artist + '.txt'
	header = artist + ' - ' + song + ' lyrics\n'
	if lyrics is not None:
		with open(filename, "a") as curfile:
			curfile.write(header)
   		for ver in lyrics:
			print ver.get_text()
			text=ver.get_text()
			with open(filename, "a") as curfile:
    				curfile.write(text)
  	else:
    		print("Please enter correct information")

song= raw_input('Enter song name ')
s = song.lower().replace(' ','-')
artist = raw_input('Enter artist name ')
a = artist.lower().replace(' ','-')
lyric(s,a)