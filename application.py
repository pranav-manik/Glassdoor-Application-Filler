from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class page_has_form(object):
	def __init__(self, css_class):
		self.css_class = css_class
		print("css_class: " + self.css_class)

	def __call__(self, driver):
		form = driver.find_element_by_class_name(self.css_class) #Find form
		# print(form)
		if self.css_class == "modalContainer":
			return form
		else:
			return False

class form_submitted(object):
	def __init__(self, css_class):
		self.css_class = css_class
		print("css_class: " + self.css_class)

	def __call__(self, driver):
		form = driver.find_element_by_class_name(self.css_class) #Find form
		# print(form)
		if self.css_class != "modalContainer":
			return form
		else:
			return False

UserAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25"
opts = Options()
opts.add_argument("user-agent="+UserAgent)
driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=opts)
driver.get("https://www.glassdoor.com/job-listing/software-engineer-dragos-JV_IC1153584_KO0,17_KE18,24.htm?jl=2732222047&ctt=1542385133501")
assert "Glassdoor" in driver.title
# ad = driver.find_element_by_xpath('//*[@id="SmartBanner"]/a[1]/span/svg')
ad = driver.find_element_by_class_name('SVGInline-svg')
ad.click()
applyButton = driver.find_element_by_class_name("regToApplyArrowBoxContainer")
applyButton.click();
wait = WebDriverWait(driver, 10)
form = wait.until(page_has_form("modalContainer"))
name = driver.find_element_by_name("answers[0]")
email = driver.find_element_by_name("answers[1]")
name.clear()
name.send_keys("Pranav Maniktala")
email.clear()
email.send_keys("pranav.manik@gmail.com")
# //*[@id="ApplyQuestions"]/div[5]/div/button
resume = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[5]/div/button')
resume.send_keys("/Users/PranavNew/Desktop/Resume/PranavManikcollegeResumeLatest.docx")
resume.send_keys('Keys.RETURN')
# resume.click()
checkbox = driver.find_element_by_class_name('theme__check___2nJhq')
checkbox.click()
submit = driver.find_element_by_xpath('//*[@id="ApplyContainer"]/div/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/button')
actions = ActionChains(driver)
actions.move_to_element(submit).perform()
# driver.execute_script("submit.scrollIntoView")
submit.click()
wait = WebDriverWait(driver, 10)
submitted = form = wait.until(form_submitted("modalContainer"))

assert "No results found." not in driver.page_source
driver.close()
driver.quit()