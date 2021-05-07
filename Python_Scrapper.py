from bs4 import BeautifulSoup
import requests 

# Collect the page 
# source = requests.get('').text
# print the page
# print (soup.prettify())

source = requests.get('https://www.github.com/').text  #prints the formatted code from a website


soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())

# match = soup.div        #match variable is used to grab div tags
# print(match)




