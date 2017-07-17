import requests,re,os
import bs4
import ntpath as path
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

url='https://gabrielecirulli.github.io/2048/'

browser=webdriver.Firefox()
browser.get(url)

newgame=browser.find_element_by_class_name('restart-button')
newgame.click()

score=browser.find_element_by_class_name('score-container')
#sleep(2)
print ('SCORE IS :',score.text, type(score.text))
htmlelem=browser.find_element_by_tag_name('html')
cnt=0
if score.text!=str(0):
    print ('RESTART THE GAME , SINCE THE SCORE IS NOT SET TO 0:-')
else:
    print ('LETS START THE NEW GAME NOW')
    sleep(5)

    while (int(score.text) < 800):
        cnt+=1
        htmlelem.send_keys(Keys.UP)
        htmlelem.send_keys(Keys.DOWN)
        htmlelem.send_keys(Keys.LEFT)
        htmlelem.send_keys(Keys.RIGHT)
        score = browser.find_element_by_class_name('score-container')
        print ('UR SCORE AFTER ',cnt,' CHANCES ARE:-', score.text)
        sleep(1)


