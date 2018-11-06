#import Beutiful Soup
from bs4 import BeautifulSoup
import requests


#retreive url to search
page_url = input("Enter URL: ")


#requests page through User Agent Mozilla
page_response = requests.get(page_url,  headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(page_response.content, "html.parser")

#print(soup.prettify())

# All Jobs
# soup.find_all("li", attrs={"class":"jl"})

i = 1
for job in soup.find_all("li", attrs={"data-is-easy-apply":"true"}):

	print("Job Number:", i)
	print(job.prettify())
	

	i=i+1

f = open("webpage.txt", "w")
f.write(soup.prettify())
