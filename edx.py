import csv		
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='C:/Users/msk/Desktop/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://www.edx.org/course')

course_name=[]
provided_by=[]
duration=[]
course_links=[]
price=[]

def open_new_course(link):
	#open tab

	driver.execute_script("window.open('');")
	driver.switch_to.window(driver.window_handles[1])
	driver.implicitly_wait(10)
	driver.get(link)
	if (link.find('professional') != -1): 
	    try:
	    	WebDriverWait(driver, 10).until(professional)
	    except TimeoutException as e:
	    	print(e)
	
	else:
		try:
			
			course_name.append(driver.find_element_by_xpath('//div[@class="col-md-8 details"]/h1').text)
			provided_by.append(driver.find_element_by_xpath("//span[@class='providers']").text)
			price.append(driver.find_elements_by_xpath('//div[@class="stat-details"]/div')[0].text)
			duration.append(driver.find_elements_by_xpath('//div[@class="stat-details"]/div')[3].text)
			
			print(course_name[-1])
			print(provided_by[-1])
			print(duration[-1])
			print(price[-1])
			
			
			print("\n")

		except Exception as e:
			try:
				course_name.append(driver.find_element_by_xpath('//span[@class="text-size-heading"]').text)
				provided_by.append(driver.find_element_by_xpath("//li[@data-field='school']/span[@class='block-list__desc']/a").text)
				price.append(driver.find_element_by_xpath("//li[@data-field='price']/span[@class='block-list__desc']").text)
				duration.append(driver.find_element_by_xpath("//li[@data-field='length']/span[@class='block-list__desc']").text)
				print(course_name[-1])
				print(provided_by[-1])
				print(duration[-1])
				print(price[-1])
			except Exception as e:
				try:
					course_name.append(driver.find_element_by_xpath('//h1[@id="program-title"]').text)
					provided_by.append(driver.find_element_by_xpath("//li[@data-field='authoring_organization']/span[@class='block-list__desc']/a").text)
					price.append(driver.find_element_by_xpath("//li[@data-field='price']/span[@class='block-list__desc']/span[@aria-label='Current Price']").text)
					duration.append(driver.find_element_by_xpath("//li[@data-field='length']/span[@class='block-list__desc']").text)
					print(course_name[-1])
					print(provided_by[-1])
					print(duration[-1])
					print(price[-1])
				except Exception as e:
					print(e)	
	driver.close()
	driver.switch_to.window(driver.window_handles[0])

def professional(driver):
	try:
		link=driver.find_elements_by_xpath('//a[@class="card-link"]')
		money = driver.find_elements_by_xpath('//div[@class="card-detail d-flex"]/span')
		effort = driver.find_elements_by_xpath('//div[@class="card-detail d-inline-block"]/span[@class="font-weight-bold ml-1"]')
		for i in range(len(link)):
			course_links.append(link[i].get_attribute("href"))
			course_name.append(link[i].text)
			price.append(money[i].text)
			duration.append(effort[i].text)
			print(course_links[-1])
			print(course_name[-1])
			print(price[-1])
			print(duration[-1])
		return True		
	except Exception as e:
		return False 


courses = driver.find_elements_by_xpath('//a[@class="course-link"]')
print(len(courses))

for course in courses:
	ele = course.get_attribute("href")
	course_links.append(ele)
	print(ele)




for course in course_links:
	print("opening link " + course)
	open_new_course(course)

print(course_name)
print(course_links)
print(provided_by)
print(price)
print(duration)
print("Done")



driver.close()
driver.quit()