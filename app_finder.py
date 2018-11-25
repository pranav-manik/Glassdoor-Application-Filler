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

# All Easy Apply Jobs
i = 1
for job in soup.find_all("li", attrs={"data-is-easy-apply":"true"}):

	print("Job Number:", i)
	sess = requests.Session()
	easyApply_url = mainSite + job.find("a", attrs={"class":"jobLink"})["href"]
	easyApply_response = sess.get(easyApply_url, headers={'User-Agent': 'Mozilla/5.0'})
	curPage = BeautifulSoup(easyApply_response.content, "html.parser")
	print(easyApply_url)
	curPage = BeautifulSoup(easyApply_response.content, "html.parser")
	#write links to file
	f = open("webpage.txt", "a")
	f.write("Job Number: "+ str(i) + '\n')
	f.write(easyApply_url+'\n')
	f.write('\n')
	i=i+1
# f = open("webpage.txt", "w")
# f.write(soup.prettify())
