import csv		
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/Users/msk/Desktop/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://in.udacity.com/courses/all')

course_link = []
course_name = []
course_skill =[]
course_time=[]
course_price=[]
desc_1 = []
desc_2 = []
desc_3=[]
course_image=[]
faqs=[]
course_level = []

def open_course(link):
	driver.execute_script("window.open('');")
	driver.switch_to.window(driver.window_handles[1])
	driver.implicitly_wait(1)
	driver.get(link)

	temp_name = ""
	temp_skill = ""
	temp_desc1 = ""
	temp_desc2 = ""
	temp_faq = ""
	removed = False

	try:
		print("#case 1")
		temp_name = (driver.find_element_by_xpath('//h1[@class="ng-star-inserted"]').text)
		#course_price.append(driver.find_element_by_xpath('//*[@id="nanodegreeEnrollmentSectionIn"]/div/ir-degree-pricing/div/div/ir-degree-pricing-card/div/div[2]/div/span').text)
		temp_desc1 = (driver.find_element_by_xpath('//div[@class="description half"]/p').text)
		temp_desc2 = (driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-ndop-b/section[3]/ir-nd-hero-video/div/div[2]/div/p').text)
		course_keywords = (driver.find_elements_by_xpath('//ul[@class="nd-skills-data"]/li'))

		All_key ="Udacity"

		for key in course_keywords:
			if  key.text != "":
				All_key += ","+key.text
			else:
				break
		temp_skill = (All_key)
		#course_time.append(driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-ndop-b/section[5]/ir-nd-overview/div/ul/li[1]').text)
		#desc_3.append(driver.find_element_by_xpath('/html/body/ir-root/ir-content/ir-ndop-b/section[9]/ir-nd-why/div/div[1]').text)
		ques = driver.find_elements_by_xpath('//div[@class="faq_wrapper"]/ul/li/h6')
		answ = driver.find_elements_by_xpath('//div[@class="faq_wrapper"]/ul/li/div')
		faq = ""
		for q,a in zip(ques,answ):
			faq = faq+q.get_attribute("textContent")+'\n'+a.get_attribute("textContent")+"\n\n\n"
		temp_faq = (faq)	
	
	except Exception as e:
		try:
			print("#case 2")
			temp_name = (driver.find_element_by_xpath('//div[@class="content"]/h1').text)
			temp_desc1 = (driver.find_element_by_xpath('//div[@class="description half"]/p').text)
				
			try:
				temp = driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-ndop-b/section[3]/ir-nanodegree-summary-banner/div/div[2]/div[1]/p').get_attribute("innerText")
				print("try2")
				temp_desc2 = (temp)
			except Exception as e:
				try:
					temp = driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-ndop-b/section[3]/ir-nd-hero-video/div/div[2]/div/p').text
					print("try3")
					temp_desc2 = (temp)
				except Exception as e :
					print(e)	
			ques = driver.find_elements_by_xpath('//div[@class="faq_wrapper"]/ul/li/h6')
			answ = driver.find_elements_by_xpath('//div[@class="faq_wrapper"]/ul/li/div')

			faq = ""
			for q,a in zip(ques,answ):
				faq = faq+q.get_attribute("textContent")+'\n'+a.get_attribute("textContent")+"\n\n\n"
			temp_faq = (faq)

			course_keywords = (driver.find_elements_by_xpath('//ul[@class="nd-skills-data"]/li'))

			All_key ="Udacity"

			for key in course_keywords:
				if  key.text != "":
					All_key += ","+key.text
				else:
					break
			
			temp_skill = (All_key)
			
		except Exception as e:
			try:
				print("#case 3")
				temp_name = (driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-ndop-in/section[3]/ir-new-nanodegree-summary-banner/div/div/div/h1').text)
				#course_price.append(driver.find_element_by_xpath('//*[@id="nanodegreeEnrollmentSectionIn"]/div/ir-degree-pricing/div/div/ir-degree-pricing-card/div/div[2]/div/span').text)
				temp_desc1 = (driver.find_element_by_xpath('//div[@class="description half"]/p').text)
				temp_desc2 = (driver.find_element_by_xpath('/html/body/ir-root/ir-content/ir-ndop-in/section[3]/ir-new-nanodegree-summary-banner/div/div/div[1]/p').text)
				ques = driver.find_elements_by_xpath('//div[@class="faq_wrapper"]/ul/li/h6')
				answ = driver.find_elements_by_xpath('//div[@class="faq_wrapper"]/ul/li/div')				
				faq = ""
				for q,a in zip(ques,answ):
					faq = faq+q.get_attribute("textContent")+'\n'+a.get_attribute("textContent")+"\n\n\n"
				temp_faq = (faq)
				course_keywords = (driver.find_elements_by_xpath('//ul[@class="nd-skills-data"]/li'))

				All_key ="Udacity"

				for key in course_keywords:
					if  key.text != "":
						All_key += ","+key.text
					else:
						break
				
				temp_skill = (All_key)					
				

			except Exception as e:
				try:
					print("#case 4")
					temp_name  = (driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-course-overview/section[2]/div/ir-course-hero/ir-course-title-card/h1').text)
					temp_desc1 = (driver.find_element_by_xpath('//div[@class="description half"]/p').text)
					temp_desc2 = (driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-course-overview/section[3]/div/ir-product-summary/div/p').get_attribute("innerText"))
					faq = driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/h4').get_attribute('textContent')+'\n\n'+driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-summary').get_attribute('textContent')+'\n\n\n'+driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-details-list/h6').get_attribute('textContent')
					t = driver.find_elements_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-details-list/ir-why-take-course-details-item')
					temp=faq
					for x in t:
						temp = temp+"\n"+x.get_attribute("textContent")
					temp_faq = (temp)	
					course_keywords = (driver.find_elements_by_xpath('//ul[@class="nd-skills-data"]/li'))

					All_key ="Udacity"

					for key in course_keywords:
						if  key.text != "":
							All_key += ","+key.text
						else:
							break
					
					temp_skill = (All_key)
					
				except Exception as e:
					try:
						print("#case 5")
						temp_name  = (driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-course-in/section/ir-cop-banner/section/div[2]/h1').text)

						temp_desc1 = (driver.find_element_by_xpath('//div[@class="description half"]/p').text)
						temp_desc2 = (driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-course-in/section/section[1]/ir-cop-course-details/div/div[2]/div/div[1]/div/p').get_attribute("innerText"))
						faq = driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/h4').get_attribute('textContent')+'\n\n'+driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-summary').get_attribute('textContent')+'\n\n\n'+driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-details-list/h6').get_attribute('textContent')
						t = driver.find_elements_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-details-list/ir-why-take-course-details-item')
						temp=faq
						for x in t:
							temp = temp+"\n"+x.get_attribute("textContent")
						temp_faq = (temp)	
						course_keywords = (driver.find_elements_by_xpath('//ul[@class="nd-skills-data"]/li[@class="ng-star-inserted"]'))

						All_key ="Udacity"

						for key in course_keywords:
							if  key.text != "":
								All_key += ","+key.text
							else:
								break
						
						temp_skill =(All_key)					
						
					except Exception as e:
						try:
							print("#case 6")
							temp_name = (driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-course-overview/section[2]/div/ir-course-hero/ir-course-title-card/h1').text)

							temp_desc1 = (driver.find_element_by_xpath('//div[@class="description half"]/p').text)
							temp_desc2 = (driver.find_element_by_xpath('//html/body/ir-root/ir-content/ir-course-overview/section[3]/div/ir-product-summary/div').get_attribute("innerText"))
							faq = driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/h4').get_attribute('textContent')+'\n\n'+driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-summary').get_attribute('textContent')+'\n\n\n'+driver.find_element_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-details-list/h6').get_attribute('textContent')
							t = driver.find_elements_by_xpath('//section[@class="course-why bg-gray ng-star-inserted"]/ir-why-take-course/ir-why-take-course-details-list/ir-why-take-course-details-item')
							temp=faq
							for x in t:
								temp = temp+"\n"+x.get_attribute("textContent")
							temp_faq = (temp)	
							course_keywords = (driver.find_elements_by_xpath('//ul[@class="nd-skills-data"]/li[@class="ng-star-inserted"]'))

							All_key ="Udacity"

							for key in course_keywords:
								if  key.text != "":
									All_key += ","+key.text
								else:
									break
							
							temp_skill =(All_key)	


						except Exception as e:
							print("Removing")
							course_link.remove(link)

	if temp_name !="" and temp_faq !="" and temp_skill!="" and temp_desc1!="" and temp_desc2!="" :
		course_name.append(temp_name)
		course_skill.append(temp_skill)
		faqs.append(temp_faq)
		desc_1.append(temp_desc1)
		desc_2.append(temp_desc2)				

	driver.close()
	driver.switch_to.window(driver.window_handles[0])

courses = driver.find_elements_by_xpath('//h3[@class="card-heading"]/a')
images = driver.find_elements_by_xpath('/html/body/ir-root/ir-content/ir-course-catalog/section[3]/div/div[2]/ir-course-card-catalog/div/div/div/div/ir-catalog-card/div/div[1]/div[1]/div[1]/a/div')
skills = driver.find_elements_by_xpath('/html/body/ir-root/ir-content/ir-course-catalog/section[3]/div/div[2]/ir-course-card-catalog/div/div/div/div/ir-catalog-card/div/div[1]/div[1]/div[2]/div[2]/div[1]')
course_levels = driver.find_elements_by_xpath('//span["course-level"]/span[@class="capitalize"]')

print(len(images))
for image in images:
	course_image.append(image.value_of_css_property('background-image')[5:-2])

print(len(course_levels))
for level in course_levels:
	course_level.append(level.text)

print(len(courses))
for i in courses:
	course_link.append(i.get_attribute('href'))
	print(course_link[-1])
	open_course(course_link[-1])
	

	
fields = ['course_link','course_name','course_image','Description_1','Description_2','faq','category', 'level']


rows = list(zip(course_link,course_name,course_image,desc_1,desc_2,faqs,course_skill,course_level))

with open("udacity.csv", 'w',  encoding="utf-8") as csvfile: 
	csvwriter = csv.writer(csvfile,delimiter=',',lineterminator='\n')
	csvwriter.writerow(fields) 
	csvwriter.writerows(rows)	
driver.close()
driver.quit()