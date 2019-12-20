import json
import time
import sys
from selenium import webdriver

br= webdriver.Chrome(executable_path='C:/Users/admin/chromedriver')
def get_captcha():
	captcha_id = input('Enter the captcha code:')
	return captcha_id

def login(DL_Number , dob ):
	url="https://parivahan.gov.in/rcdlstatus/?pur_cd=101"
	br.get(url)
	br.find_element_by_xpath('//*[@id="form_rcdl:tf_dlNO"]').send_keys(DL_Number) 
	br.find_element_by_xpath('//*[@id="form_rcdl:tf_dob_input"]').send_keys(dob)
	cap_id = br.find_element_by_xpath('//*[@id="form_rcdl:j_idt29:CaptchaID"]')
	cap_id.send_keys(get_captcha())
	br.find_element_by_xpath('//*[@id="form_rcdl:j_idt39"]').click()
	time.sleep(5)
	try:
		msg = br.find_element_by_xpath('//*[@id="form_rcdl:j_idt13"]/div/ul/li/span[1]').text
		print(msg)
		return None
	except:
		result = {}
		result['Name'] = br.find_element_by_xpath('//*[@id="form_rcdl:j_idt137"]/table[1]/tbody/tr[2]/td[2]').text
		result['Date of issue'] = br.find_element_by_xpath('//*[@id="form_rcdl:j_idt137"]/table[1]/tbody/tr[3]/td[2]').text
		result['Date of expiry'] = br.find_element_by_xpath('//*[@id="form_rcdl:j_idt137"]/table[2]/tbody/tr[1]/td[3]').text.split()[1]
		result['Class of vehical'] = br.find_element_by_xpath('//*[@id="form_rcdl:j_idt184_data"]/tr/td[2]').text
		return result
	
	
DL_Number = input("Enter the Driving Licence Number:")
dob = input("DOB (dd-mm-yyyy):")
result = login(DL_Number, dob)
while result is None:
	result = login(DL_Number, dob)

print(result)

