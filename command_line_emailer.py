import os,re, bs4
import requests
from selenium import webdriver
import ntpath as path
import lxml
import sys
from time import sleep

url='http://mail.google.com'

if len(sys.argv) > 1:
    url=sys.argv[1]
    username=sys.argv[2]
    password=sys.argv[3]
    emailData=sys.argv[4:]
else:
    print ('PLEASE ENTER EMAIL URL, USERNAME, PASSWD AND DATA TO BE EMAILED')
assert len(sys.argv) > 1, 'PLEASE ENTER EMAIL URL, USERNAME, PASSWD AND DATA TO BE EMAILED'
print ('Email URL IS {0} \nUSERNAME IS {1} \nPASSWD IS {2} \nDATA TO BE EMAILED IS {3} :-'\
       .format(url,username,password,emailData))

browser=webdriver.Firefox()
browser.get(url)
loginLink=browser.find_element_by_id('identifierId')
print(browser.find_element_by_id('identifierId'))
loginLink.send_keys(username)
loginLink.submit()

next=browser.find_element_by_class_name('RveJvd')
next.click()
sleep(2)

passwdLink=browser.find_element_by_class_name('whsOnd') and browser.find_element_by_class_name('zHQkBf')
passwdLink.send_keys(password)
passwdLink.submit()

next=browser.find_element_by_class_name('RveJvd')
next.click()
sleep(10)

composeLink=browser.find_element_by_css_selector('.T-I-KE')
composeLink.click()

toLink=browser.find_element_by_id(':g7')
toLink.send_keys('aryan21710@gmail.com')
toLink.submit()


SubLink=browser.find_element_by_id(':fq')
SubLink.send_keys('this is a test email')
SubLink.submit()

DataLink=browser.find_element_by_id(':gr')
DataLink.send_keys(emailData)
sleep(2)

SendLink=browser.find_element_by_id(':fg')
SendLink.click()






