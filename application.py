from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import keyboard


first_name = "firstName"
last_name = "lastName"
email = ""
cover_letter = "blah blah blah"
phone_number = "911"
address = ""
headline = ""

class education(object):
	name = "University of ..."
	degree = "Bachelors"
	major = "major"
	start_month = ""
	start_day = ""
	start_year = ""
	end_month = ""
	end_day = ""
	end_year = ""

my_school = education()

num_of_jobs = 3
class job(object):
	title = ""
	company = ""
	industry = ""
	summary = ""
	work_here = False
	start_month = ""
	start_day = ""
	start_year = ""
	end_month = ""
	end_day = ""
	end_year = ""
	def __init__(self, title, company, industry, summary, work_here,
				start_month, start_day, start_year,
				end_month, end_day, end_year):
		self.title = title
		self.company = company
		self.industry = industry
		self.summary = summary
		self.work_here = work_here
		self.start_month = start_month
		self.start_day = start_day
		self.start_year = start_year
		self.end_month = end_month
		self.end_day = end_day
		self.end_year = end_year
job1 = job("Title", "Glassdoor", "Cybersecurity", "blah blah blah blah", True, "June", "1", "1998", "N/A", "N/A", "N/A")






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
		if self.css_class != "EasyApplyConfirmation":
			return form
		else:
			return False



def check_form(driver):
	try:
		phoneForm = driver.find_element_by_id('gdPhoneNumber')
	except:
		return 2
	return 1


UserAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25"
opts = Options()
opts.add_argument("user-agent="+UserAgent)
driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=opts)
# https://www.glassdoor.com/job-listing/software-developer-cloud-moser-consulting-JV_IC1153527_KO0,24_KE25,41.htm?jl=3007978726&ctt=1543104906959
# https://www.glassdoor.com/job-listing/software-engineer-dragos-JV_IC1153584_KO0,17_KE18,24.htm?jl=2732222047&ctt=1543105496898
# https://www.glassdoor.com/job-listing/software-developer-callrevu-JV_IC1153589_KO0,18_KE19,27.htm?jl=2907297699&ctt=1543129776165
page_url = input("Enter URL: ")
driver.get(page_url)
assert "Glassdoor" in driver.title
# ad = driver.find_element_by_xpath('//*[@id="SmartBanner"]/a[1]/span/svg')
ad = driver.find_element_by_class_name('SVGInline-svg')
ad.click()
applyButton = driver.find_element_by_class_name("regToApplyArrowBoxContainer")
applyButton.click();
wait = WebDriverWait(driver, 10)
form = wait.until(page_has_form("modalContainer"))

form_type = check_form(form)
print('form type: ', form_type)
if form_type == 1:
	first_name_field = driver.find_element_by_id('gdFirstName')
	last_name_field = driver.find_element_by_id('gdLastName')
	email_field = driver.find_element_by_id('gdEmailAddress')
	cover_letter_field = driver.find_element_by_id('gdCoverLetter')
	phone_number_field = driver.find_element_by_id('gdPhoneNumber')
	headline_field = driver.find_element_by_id('headline')
	address_field = driver.find_element_by_id('address')
	#education
	school_field = driver.find_element_by_id('education_._school')
	degree_field = driver.find_element_by_id('education_._degree')
	field_of_study_field = driver.find_element_by_id('education_._field_of_study')
	start_month_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[1]/div[4]/div/select[1]')
	start_day_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[1]/div[4]/div/select[2]')
	start_year_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[1]/div[4]/div/select[3]')
	end_month_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[1]/div[5]/div/select[1]')
	end_day_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[1]/div[5]/div/select[2]')
	end_year_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[1]/div[5]/div/select[3]')
	#experience
	title_field = driver.find_element_by_id('experience_._title')
	company_field = driver.find_element_by_id('experience_._company')
	industry_field = driver.find_element_by_id('experience_._industry')
	summary_field = driver.find_element_by_id('experience_._summary')
	check_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[11]/div[1]/div[5]/div/label[1]/div')
	x_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[11]/div[1]/div[5]/div/label[2]/div')
	job_start_month_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[11]/div[1]/div[6]/div/select[1]')
	job_start_day_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[11]/div[1]/div[6]/div/select[2]')
	job_start_year_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[11]/div[1]/div[6]/div/select[3]')
	job_end_month_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[11]/div[1]/div[7]/div/select[1]')
	job_end_day_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[11]/div[1]/div[7]/div/select[2]')
	job_end_year_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[11]/div[1]/div[7]/div/select[3]')



	first_name_field.clear()
	first_name_field.send_keys(first_name)
	last_name_field.clear()
	last_name_field.send_keys(last_name)
	email_field.clear()
	email_field.send_keys(email)
	cover_letter_field.clear()
	cover_letter_field.send_keys(cover_letter)
	resume = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[6]/div/button')
	resume.click()
	#move through path to resume file
	keyboard.write('Desktop')
	keyboard.press_and_release('enter')
	keyboard.write('Resume')
	keyboard.press_and_release('enter')
	keyboard.write('resume.docx')
	keyboard.press_and_release('enter')
	phone_number_field.clear()
	phone_number_field.send_keys(phone_number)
	headline_field.clear()
	headline_field.send_keys(headline)
	address_field.clear()
	address_field.send_keys(address)

	#Education
	school_field.clear()
	school_field.send_keys(my_school.name)
	degree_field.clear()
	degree_field.send_keys(my_school.degree)
	field_of_study_field.clear()
	field_of_study_field.send_keys(my_school.major)
	start_month_field.send_keys(my_school.start_month)
	start_day_field.send_keys(my_school.start_day)
	start_year_field.send_keys(my_school.start_year)
	end_month_field.send_keys(my_school.end_month)
	end_day_field.send_keys(my_school.end_day)
	end_year_field.send_keys(my_school.end_year)

	#Experience
	title_field.clear()
	title_field.send_keys(job1.title)
	company_field.clear()
	company_field.send_keys(job1.company)
	industry_field.clear()
	industry_field.send_keys(job1.industry)
	summary_field.clear()
	summary_field.send_keys(job1.summary)
	if (job1.work_here == True):
		check_field.click()
	else:
		x_field.click()
		job_end_month_field.send_keys(job1.end_month)
		job_end_day_field.send_keys(job1.end_day)
		job_end_year_field.send_keys(job1.end_year)

	job_start_month_field.send_keys(job1.start_month)
	job_start_day_field.send_keys(job1.start_day)
	job_start_year_field.send_keys(job1.start_year)
	add = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[2]')
	add.click()
	
	#job2
	title_field = driver.find_element_by_xpath('(//*[@id="experience_._title"])[2]')
	company_field = driver.find_element_by_xpath('(//*[@id="experience_._company"])[2]')
	industry_field = driver.find_element_by_xpath('(//*[@id="experience_._industry"])[2]')
	summary_field = driver.find_element_by_xpath('(//*[@id="experience_._summary"])[2]')
	check_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[2]/div[6]/div/label[1]/div')
	x_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[2]/div[6]/div/label[2]/div')
	job_start_month_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[2]/div[7]/div/select[1]')
	job_start_day_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[2]/div[7]/div/select[2]')
	job_start_year_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[2]/div[7]/div/select[3]')
	job_end_month_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[2]/div[8]/div/select[1]')
	job_end_day_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[2]/div[8]/div/select[2]')
	job_end_year_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[2]/div[8]/div/select[3]')

	title_field.clear()
	title_field.send_keys(job2.title)
	company_field.clear()
	company_field.send_keys(job2.company)
	industry_field.clear()
	industry_field.send_keys(job2.industry)
	summary_field.clear()
	summary_field.send_keys(job2.summary)
	if (job2.work_here == True):
		check_field.click()
	else:
		x_field.click()
		job_end_month_field.send_keys(job2.end_month)
		job_end_day_field.send_keys(job2.end_day)
		job_end_year_field.send_keys(job2.end_year)

	job_start_month_field.send_keys(job2.start_month)
	job_start_day_field.send_keys(job2.start_day)
	job_start_year_field.send_keys(job2.start_year)
	add = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[3]')
	add.click()

	#job3
	wait = WebDriverWait(driver, 10)
	title_field = driver.find_element_by_xpath('(//*[@id="experience_._title"])[3]')
	company_field = driver.find_element_by_xpath('(//*[@id="experience_._company"])[3]')
	industry_field = driver.find_element_by_xpath('(//*[@id="experience_._industry"])[3]')
	summary_field = driver.find_element_by_xpath('(//*[@id="experience_._summary"])[3]')

	title_field.clear()
	title_field.send_keys(job3.title)
	company_field.clear()
	company_field.send_keys(job3.company)
	industry_field.clear()
	industry_field.send_keys(job3.industry)
	summary_field.clear()
	summary_field.send_keys(job3.summary)
	check_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[3]/div[6]/div/label[1]/div')
	x_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[3]/div[6]/div/label[2]/div')
	job_start_month_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[3]/div[7]/div/select[1]')
	job_start_day_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[3]/div[7]/div/select[2]')
	job_start_year_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[3]/div[7]/div/select[3]')
	job_end_month_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[3]/div[8]/div/select[1]')
	job_end_day_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[3]/div[8]/div/select[2]')
	job_end_year_field = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[10]/div[3]/div[8]/div/select[3]')
	if (job3.work_here == True):
		check_field.click()
	else:
		x_field.click()
		job_end_month_field.send_keys(job3.end_month)
		job_end_day_field.send_keys(job3.end_day)
		job_end_year_field.send_keys(job3.end_year)

	job_start_month_field.send_keys(job3.start_month)
	job_start_day_field.send_keys(job3.start_day)
	job_start_year_field.send_keys(job3.start_year)
	# //*[@id="ApplySection"]/div[2]/label/div
	checkbox = driver.find_element_by_class_name('theme__check___2nJhq')
	checkbox.click()
	submit = driver.find_element_by_xpath('//*[@id="ApplyContainer"]/div/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/button')
	actions = ActionChains(driver)
	actions.move_to_element(submit).perform()
	submit.click()
wait = WebDriverWait(driver, 10)
submitted = form = wait.until(form_submitted("modalContainer"))





if (form_type == 2):
	name_field = driver.find_element_by_name("answers[0]")
	email_field = driver.find_element_by_name("answers[1]")
	name_field.clear()
	name_field.send_keys(first_name+" "+last_name)
	email_field.clear()
	email_field.send_keys(email)
	resume = driver.find_element_by_xpath('//*[@id="ApplyQuestions"]/div[5]/div/button')
	resume.click()
	#move through path to resume file
	keyboard.write('Desktop')
	keyboard.press_and_release('enter')
	keyboard.write('Resume')
	keyboard.press_and_release('enter')
	keyboard.write('resume.docx')
	keyboard.press_and_release('enter')

	checkbox = driver.find_element_by_class_name('theme__check___2nJhq')
	checkbox.click()
	submit = driver.find_element_by_xpath('//*[@id="ApplyContainer"]/div/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/button')
	actions = ActionChains(driver)
	actions.move_to_element(submit).perform()
	submit.click()
wait = WebDriverWait(driver, 10)
submitted = form = wait.until(form_submitted("modalContainer"))

assert "No results found." not in driver.page_source
driver.close()
driver.quit()