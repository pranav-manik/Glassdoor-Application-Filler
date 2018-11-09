#import Beautiful Soup
from bs4 import BeautifulSoup
import requests


#retreive url to search
page_url = input("Enter URL: ")
mainSite = "https://www.glassdoor.com"

#requests page through User Agent Mozilla
page_response = requests.get(page_url,  headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(page_response.content, "html.parser")

#print(soup.prettify())

# All Jobs
# soup.find_all("li", attrs={"class":"jl"})

i = 1
once = True
for job in soup.find_all("li", attrs={"data-is-easy-apply":"true"}):

	print("Job Number:", i)
	#print(job.find("a", attrs={"class":"jobLink"})["href"])
	easyApply_url = mainSite + job.find("a", attrs={"class":"jobLink"})["href"]
	easyApply_response = requests.get(easyApply_url, headers={'User-Agent': 'Mozilla/5.0'})
	curPage = BeautifulSoup(easyApply_response.content, "html.parser")
	sess = requests.Session()
	# sess.get()

	if once == True:
		# print(easyApply_response)
		# print(curPage.prettify())
		# print("Session cookie", easyApply_response.cookies)
		start_app_url = easyApply_url.replace("/partner/jobListing.htm?", "/job-listing/trackClickAsync.htm?")
		start_app_url = start_app_url + "&tgt=APPLY_START"
		start_app_response =  requests.get(start_app_url, headers={'User-Agent': 'Mozilla/5.0'})
		print(start_app_response)
		curPage = BeautifulSoup(easyApply_response.content, "html.parser")
		# print(start_app)

		#write to file
		f = open("webpage.txt", "w")
		f.write(start_app_url)
		f.write(curPage.prettify())
	once = False

	i=i+1

# f = open("webpage.txt", "w")
# f.write(soup.prettify())
