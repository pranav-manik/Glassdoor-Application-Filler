#import the library used to query website
import urllib2
#import Beutiful Soup
from sb4 import BeautifulSoup

#give the url
myURL = ""

#Query the website and return the html
page = urlli2.urlopen(myURL)

#parse the html'
soup = BeautifulSoup(page)
