# import dependencies
#   1) web client interface
#   2) web-data parser
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# site to be scraped
my_url = 'https://shop.macmillerswebsite.com/'

# initialize/open web client
uClient = uReq(my_url)
page_html = uClient.read() # snag the HTML
uclient.close() # just like a scanner, close that stuff

page_soup = soup(page_html, "html.parser") # use bs4 to parse page_html using its "html.parser"

# find specific items to scrape
