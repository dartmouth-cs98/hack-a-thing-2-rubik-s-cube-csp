#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Sources:
https://seleniumhq.github.io/selenium/docs/api/py/api.html
https://www.guru99.com/selenium-python.html
https://selenium-python.readthedocs.io/locating-elements.html
'''

#import necessary classes
from selenium.webdriver import Chrome
from time import sleep 
import random
import time

#set up local variables
chromedriver = './chromedriver'
page = "https://collegepulse.com/app"
driver = Chrome('./chromedriver')
email = 'j.h.d.19@dartmouth.edu'
url = 'https://collegepulse.com/login?returnurl=https://collegepulse.com/app'
big_break = False
t1 = time.time()
nonce = random.randint(0, 1800)

#go to login page
driver.get(url)

#wait and let page load
sleep(5)

#input email and click on login
email_input = driver.find_element_by_id('email')
email_input.send_keys(email)
pwd = driver.find_element_by_id('password1')
sleep(1)
pwd.click()

#human intervention necessary at this point as dartmouth login has no html tags to hook on to
sleep(50)

#loop run to fill out surveys indefinitely
while True:
    
    #select random survey from first page, (random required as some surveys are mobile only)
    el = random.randint(0, len(driver.find_elements_by_class_name('survey-card'))-1)
    driver.find_elements_by_class_name('survey-card')[el].click()
    
    #once a valid survey is selected, enter loop to fill out survey
    loop = 0
    old_ops = []
    while True:
        
        #count the number of loops for diagnostic purposes
        loop += 1 
        
        #sleep for a random amount of time to simulate how human would act
        rt = random.randint(0, 3)
        sleep(2+rt)
        
        #find all options buttons
        ops = driver.find_elements_by_class_name('mc-option ')
        
        #select numeric input or text boxes if they exist
        try:
            num_input = driver.find_element_by_id('numeric-input-box')
        except:
            num_input = None
        try:
            text = driver.find_element_by_id('answer-box')
        except:
            text = None
            
        #if input is not radio buttons work to determine proper inputs    
        if len(ops) == 0:
            
            #if input is supposed to be numeric 
            if num_input is not None:
                
                #get text to derive proper range of numbers
                txt = driver.find_element_by_class_name('prompt-text').text
                between = False
                greater = False
                less = False
                num_list = []
                
                #parse text and set range
                for word in txt.split():                    
                    if word == 'between':
                        between = True
                    if word == 'greater':
                        greater = True
                    if word == 'less':
                        less = True
                    if word[-1] == '.':
                        try:
                            num_list.append(int(word[:-1]))
                        except:
                            pass     
                    try:
                        num_list.append(int(word))
                    except:
                        pass                
                num_input.click()
                sleep(1)
                
                #enter random number in appropriate range
                if between:                    
                    num_input.send_keys(str(random.randint(num_list[0], num_list[1])))
                elif greater:
                    num_input.send_keys(str(random.randint(num_list[0], 2*num_list[0])))
                elif less:
                    num_input.send_keys(str(random.randint(0, num_list[0])))
                else:
                    num_input.send_keys(str(random.randint(0, 20)))
                    
            #if input is text, enter the word "pizza"
            elif text is not None:
                text.click()
                sleep(1)
                text.send_keys('pizza')
            try:
                nxt = driver.find_elements_by_class_name('nav-button')
                nxt[-1].click()
            
            #break out of the loop if none of the input formats are available, this assumes the submit page has been reached
            except:
                break
        
        #else select a random button and wait
        else:
            
            if old_ops:
                
                #if page is the same select second option then next button
                if ops[0] == old_ops[0]:
                    try:
                        if len(ops) > 4:
                            rd = random.randint(0, 3)
                            ops[rd].click()
                            sleep(1)
                        nxt = driver.find_elements_by_class_name('nav-button')
                        nxt[-1].click()
                        continue
                    except:
                        continue
                    
            #click a random
            rd = random.randint(0, len(ops)-1)
            if rd >= 4:
                rd = random.randint(0, 3)
            ops[rd].click()
        
        #sleep a random amount ot simulate human activity
        rt = random.randint(0, 2)
        sleep(1+rt)
        old_ops = ops
        
    sleep(2)
    
    #submit the survey
    try:
        driver.find_element_by_class_name('survey-submit-button').click()
    except:
        driver.find_element_by_id('surveys').click()
        
    #random length pause to simulate human activity    
    rt = random.randint(0,2)
    sleep(2 + rt)
    driver.find_element_by_id('surveys').click()
    rt = random.randint(0,2)
    sleep(2 + rt)
    
    #take a small break at intervals of about every 1.5 hours
    if time.time() - t1 > 3600 + nonce and not big_break:
        big_break = True
        nonce = random.randint(0, 1800)
        nsleep = random.randint(300, 900)
        for x in range(0, nsleep):
            print("sleep " + str(x) + ":" + str(nsleep))
            sleep(1)
        t1 = time.time()
        
    #take a big break at intervals of about every 4.5 hours
    elif time.time() - t1 > 9000 + nonce and big_break:
        big_break = False
        nonce = random.randint(0, 1800)
        nsleep = random.randint(1200, 2400)
        for x in range(0, nsleep):
            print("sleep " + str(x) + ":" + str(nsleep))
            sleep(1)
        t1 - time.time()