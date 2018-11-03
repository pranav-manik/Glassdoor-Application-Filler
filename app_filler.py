#import Beutiful Soup
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen


url = input("Enter URL: ")

#give the url
page_url = url

#requets page through User Agent Mozilla
req = Request( url , headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

page_response = requests.get(page_url, timeout=5)
soup = BeautifulSoup(page_response.content, "html.parser")


print(soup.prettify())



