'''
	Author: Arturo Avilés Castellanos
	Email: artcastell@gmail.com
	Date: Aug 5 2015
'''

from lxml import html
import requests

class AppCrawler:
	def __init__(self, starting_url, depth):
		self.starting_url = starting_url
		self.depth = depth
		self.apps = []

	def craw(self):
		self.get_info_from_link(self.starting_url)
		return

	def get_info_from_link(self, link):
		start_page = requests.get(link)

		print(start_page.text)
		return

class App:
	def __init__(self, name, developer, price, links):
		self.name = name
		self.developer = developer
		self.price = price
		self.links = links

	def __str__(self):
		return("Name: " + self.name.encode('UTF-8') +
			"\r\nDeveloper: " + self.developer.encode('UTF-8') +
			"\r\nPrice: " + self.price.encode('UTF-8') + "\r\n")

crawler = AppCrawler('https://itunes.apple.com/us/app/angry-birds-2/id880047117?mt=8',8)
crawler.craw()

for app in crawler.apps:
	print(app)

