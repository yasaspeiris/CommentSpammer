from selenium import webdriver
import time
#import uuid 
import random


nouns = ("isuru", "sandakath", "rusiru", "shakya", "rusith")
fingers = ("one", "two", "three", "four", "five") 
adj = ("adorable", "cute", "dirty", "lovely", "happy")


def commentspam(num,timedelta,postURL):
    #your credentials here
    userId = "<USERNAME>"
    password = "<PW>"

    #need chromedriver for your current chrome version
    browser = webdriver.Chrome("C:\\Users\\yasas\\Downloads\\chromedriver_win32\\chromedriver.exe")
    
    fbURL = "https://m.facebook.com"
    browser.get(fbURL)
    time.sleep(8)

    #fill credentials and log in
    userIdField = browser.find_element_by_id("m_login_email")
    passwordField = browser.find_element_by_id("m_login_password")   
    loginButton = browser.find_elements_by_tag_name("button")[0]
    userIdField.send_keys(userId)
    passwordField.send_keys(password)
    loginButton.click()

    #wait for two factor auth
    time.sleep(10)

    #should be able to get into post now
    browser.get(postURL)
    time.sleep(8)

    #halt and wait for user input. Type anything and press enter
    temp = input('Waiting for user input. Type anything and press enter : ')

    # comment x many times
    for i in range(num):
        time.sleep(timedelta)
        commentBox = browser.find_element_by_id("composerInput")
        num = random.randrange(0,5)
        num2 = random.randrange(0,5)
        comment = adj[num]+ ' ' + nouns[num] + ' puts ' + fingers[num]+ ' finger(s) up ' +  nouns[num2] +"'s bum."
        try:
            commentBox.send_keys(comment)
        except:
            #try 10 times max with 1 second delay if comment box is not available. 
            for i in range(0,10):
                try:
                    time.sleep(1)
                    commentBox.send_keys(comment)
                    break
                except:
                    pass

        #leave this delay fixed. Usually takes 2-3 seconds for the comment to get posted
        time.sleep(2)
        try:
            sendButton = browser.find_elements_by_tag_name("button")[0]
            sendButton.click()
        except:
            #try 10 times max with 1 second delay if comment box is not available. 
            for i in range (0,10):
                try:
                    time.sleep(1)
                    sendButton = browser.find_elements_by_tag_name("button")[0]
                    sendButton.click()
                    break
                except:
                    pass
        
commentspam(5000,8,"https://m.facebook.com/isuruedirisinghe80/posts/10223803470577655")