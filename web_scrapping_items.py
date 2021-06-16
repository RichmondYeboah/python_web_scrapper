#pip install bs4
#pip install urllib (use pythonenv if needed urllib3 is new version)
#pip install urlopen
#use ipython interpreter (type: python (in terminal)) 
#print all the uncommented lines of code below to collect page data

#######################
# Collect the page 
# feel free to change the url to any webpage, make sure to inspect to see which tag the review is linked to 
# Connect to the website and return the html to the variable ‘article’
# Print the article to scraped_text.txt
############################
    
    # import libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# specify the url that will collect the formatted data from the website
url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'


try:
    page = uReq(url)
except:
    print("Error opening the URL")

# parse the html using beautiful soup and store in variable `soup`
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

#html parseing
page_soup = soup(page_html, 'html.parser')

#grabs each product
containers = page_soup.findAll("div", {"class": "dynamic-module"})

#count the number of containers
# len(containers)

#lists the first container
#containers[0]