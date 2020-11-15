import time
import os
import random
import json

try:
    import selenium
    from datetime import datetime   
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options

except:

    os.system("pip -r install requirements.txt")
    exit()

# Import things.

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%d.%m.%Y")
current_file_path = os.path.dirname(os.path.realpath(__file__))

# declaring some global variables

def Main():

    os.system("cls")

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(f"{current_file_path}\\Driver\\chromedriver.exe", options=chrome_options)
    driver.get("https://web.whatsapp.com/")

    os.system("cls")
    unique_id = '//*[@id="side"]/div[1]/div/label'
    logged_in = False

    while logged_in == False:

        try:

            driver.find_element_by_xpath(unique_id)

            if driver.find_element_by_xpath(unique_id).is_displayed():

                print("[ + ] - Succesfully Logged in! - [ + ]")
                logged_in = True
            
        except Exception as e:

            print("[ - ] - Scan the QR Code to Login - [ - ]")
            time.sleep(5)
            os.system("cls")

    with open(f'{current_file_path}\\Birthdays\\Birthdays.json', 'r') as Birthday:
        
        BirthdayObj = json.load(Birthday)
        Name = BirthdayObj["Name"]
        Date = BirthdayObj["Date"]
        Message = BirthdayObj["Message"]

        if Date == current_date:

            print("[ + ] - Today is " + Date + "!" + " Now sending Message: " + Message + " - [ + ]")
            
            search_name_xpath = '//*[@id="side"]/div[1]/div/label/div/div[2]'
            person_xpath = '//*[@id="pane-side"]/div[1]/div/div/div[2]'
            message_input_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
            send_xpath = '//*[@id="main"]/footer/div[1]/div[3]'

            driver.find_element_by_xpath(search_name_xpath).click()
            time.sleep(1)
            driver.find_element_by_xpath(search_name_xpath).send_keys(f"{Name}")
            time.sleep(1)
            driver.find_element_by_xpath(person_xpath).click()
            time.sleep(1)
            driver.find_element_by_xpath(message_input_xpath).click()
            time.sleep(2)
            driver.find_element_by_xpath(message_input_xpath).send_keys(f"{Message}")
            time.sleep(2)
            driver.find_element_by_xpath(send_xpath).click()

            os.system("cls")
            print("[ + ] - Succesfully Sent a Message - [ + ]")
            time.sleep(10)


    

if __name__ == "__main__":
    
    Main() # Call Main