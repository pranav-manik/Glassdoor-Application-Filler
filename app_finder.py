#import Beautiful Soup
from bs4 import BeautifulSoup
import requests
# var cookies = require('./cookies');


#retreive url to search
# page_url = input("Enter URL: ")
page_url = "https://www.glassdoor.com/Job/columbia-software-engineer-intern-jobs-SRCH_IL.0,8_IC1153546_KO9,33.htm?jl=3000713306&jaguid=&src=GD_JOB_AD&srs=MY_JOBS&ao=376840"
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
	sess = requests.Session()
	#print(job.find("a", attrs={"class":"jobLink"})["href"])
	easyApply_url = mainSite + job.find("a", attrs={"class":"jobLink"})["href"]
	easyApply_response = sess.get(easyApply_url, headers={'User-Agent': 'Mozilla/5.0'})
	curPage = BeautifulSoup(easyApply_response.content, "html.parser")
	# sess.get()

	if once == True:
		# print(easyApply_response)
		# print(curPage.prettify())
		print("Session cookie", easyApply_response.cookies.get_dict())
		cookie = easyApply_response.cookies.get_dict()
		start_app_url = easyApply_url.replace("/partner/jobListing.htm?", "/job-listing/trackClickAsync.htm?")
		start_app_url = start_app_url + "&tgt=APPLY_START"
		start_app_response =  sess.get(start_app_url, headers={'User-Agent': 'Mozilla/5.0'}, cookies=cookie)
		post_response = sess.post("https://www.glassdoor.com/Job/json/applyGet.htm", headers={'User-Agent': 'Mozilla/5.0'}, cookies=cookie)
		print(start_app_response)
		print(post_response)
		curPage = BeautifulSoup(easyApply_response.content, "html.parser")
		# print(start_app)

		#write to file
		f = open("webpage.txt", "w")
		f.write(easyApply_url)
		f.write(start_app_url)
		f.write(curPage.prettify())
		
	once = False
	i=i+1

# f = open("webpage.txt", "w")
# f.write(soup.prettify())
