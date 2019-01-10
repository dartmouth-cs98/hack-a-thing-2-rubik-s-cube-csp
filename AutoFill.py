#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 10:11:21 2018

@author: jonah
"""

from selenium.webdriver import Chrome
from time import sleep 
import random
import time

chromedriver = './chromedriver'

page = "https://collegepulse.com/app"

driver = Chrome('./chromedriver')
driver.get('https://collegepulse.com/login?returnurl=https://collegepulse.com/app')
sleep(5)
email_input = driver.find_element_by_id('email')
email_input.send_keys('j.h.d.19@dartmouth.edu')
pwd = driver.find_element_by_id('password1')
sleep(1)
pwd.click()
sleep(50)
big_break = False
t1 = time.time()
nonce = random.randint(0, 1800)
while True:
    el = random.randint(0, len(driver.find_elements_by_class_name('survey-card'))-1)
    driver.find_elements_by_class_name('survey-card')[el].click()
    loop = 0
    old_ops = []
    while True:
        loop += 1 
        rt = random.randint(0, 3)
        sleep(2+rt)
        ops = driver.find_elements_by_class_name('mc-option ')
        
        try:
            num_input = driver.find_element_by_id('numeric-input-box')
        except:
            num_input = None
        try:
            text = driver.find_element_by_id('answer-box')
        except:
            text = None
        if len(ops) == 0:
            print('p')
            if num_input is not None:
                txt = driver.find_element_by_class_name('prompt-text').text
                between = False
                greater = False
                less = False
                num_list = []
                print(txt)
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
                print(num_list)
                sleep(1)
                if between:                    
                    num_input.send_keys(str(random.randint(num_list[0], num_list[1])))
                elif greater:
                    num_input.send_keys(str(random.randint(num_list[0], 2*num_list[0])))
                elif less:
                    num_input.send_keys(str(random.randint(0, num_list[0])))
                else:
                    num_input.send_keys(str(random.randint(0, 20)))
            elif text is not None:
                text.click()
                sleep(1)
                text.send_keys('pizza')
            try:
                nxt = driver.find_elements_by_class_name('nav-button')
                nxt[-1].click()
                print('nxt')
            except:
                print('p')
                break
        else:
            if old_ops:
                if ops[0] == old_ops[0]:
                    try:
                        if len(ops) > 4:
                            rd = random.randint(0, 3)
                            ops[rd].click()
                            sleep(1)
                        nxt = driver.find_elements_by_class_name('nav-button')
                        print(nxt)
                        nxt[-1].click()
                        continue
                    except:
                        continue
            rd = random.randint(0, len(ops)-1)
            if rd >= 4:
                rd = random.randint(0, 3)
            ops[rd].click()
            print('ops')
        rt = random.randint(0, 2)
        sleep(1+rt)
        old_ops = ops
    sleep(2)
    try:
        driver.find_element_by_class_name('survey-submit-button').click()
    except:
        driver.find_element_by_id('surveys').click()
    rt = random.randint(0,2)
    sleep(2 + rt)
    driver.find_element_by_id('surveys').click()
    rt = random.randint(0,2)
    sleep(2 + rt)
    if time.time() - t1 > 3600 + nonce and not big_break:
        big_break = True
        nonce = random.randint(0, 1800)
        nsleep = random.randint(300, 900)
        for x in range(0, nsleep):
            print("sleep " + str(x) + ":" + str(nsleep))
            sleep(1)
        t1 = time.time()
    elif time.time() - t1 > 9000 + nonce and big_break:
        big_break = False
        nonce = random.randint(0, 1800)
        nsleep = random.randint(1200, 2400)
        for x in range(0, nsleep):
            print("sleep " + str(x) + ":" + str(nsleep))
            sleep(1)
        t1 - time.time()