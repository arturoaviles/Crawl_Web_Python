# Crawl_Web_Python
This is a Project w/ Python &amp; library lxml to get info from web and use it

How to put hands to work!

**1. Install Python**

	Enter to (python.org) and install python lastest version

**2. Install pip**

	sudo easy_install pip
	sudo easy_install pip3

**3. Update pip**
	
	pip install --upgrade pip

**4. Install lxml**

	**Normally:**
		pip install lxml

	**Another way:**
		sudo CPATH=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.9.sdk/usr/include/libxml2 CFLAGS=-Qunused-arguments CPPFLAGS=-Qunused-arguments pip install lxml

**5. Install Requests**

	pip install requests

**6. See if you can import those libraries**

	python
	python3

	>>>from lxml import html
	>>>import requests
	>>>quit()

**7.Find a website you like**

	Example: (https://itunes.apple.com/us/app/angry-birds-2/id880047117?mt=8)


**How to Use it:**

	1. Download the file .py3
	2. Open Terminal
	3. Navigate to the file folder
	4. Write:
		python3 file.py3 or python file.py *See Considerations
	5. Hit Enter

	If it did'nt deliver anything or deliver strange things you should edit the paths:

	class AppCrawler
		def get_info_from_link
		name = tree.xpath('//PATH')[0]
		developer = tree.xpath('//PATH')[0]
		price = tree.xpath('//PATH')[0]
		links = tree.xpath('//PATH')

	If you want to use an specific URL you can change it in the last lines.

	

**Considerations:**

	1. If you are using python 2.* in 
	class App 
		def __str__(self) you should put:

		return ("Name: " + self.name.encode('UTF-8') + 
        	"\r\nDeveloper: " + self.developer.encode('UTF-8') + 
        	"\r\nPrice: " + self.price.encode('UTF-8') + "\r\n")


	