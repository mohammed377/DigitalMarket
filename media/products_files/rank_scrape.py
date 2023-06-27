from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()



def get_problems():
    problems = []
    driver.get('https://www.hackerrank.com/domains/python?filters%5Bstatus%5D%5B%5D=unsolved')
    scroll_down()
    elements = driver.find_elements(By.CLASS_NAME,'js-track-click')

    time.sleep(5)

    for element in elements:
        problems.append(element.get_attribute('href'))

    return problems

def solve_problem(prompt):
    solution=None
    driver.get('https://poe.com/Claude-instant')
    element= driver.find_element(By.CLASS_NAME,("ChatMessageInputView_textInput__Aervw"))
    element.clear()
    element.send_keys(prompt)
    
    return solution
     



def scroll_down():

    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height



print(get_problems())
"""

Algorithm:
    start the driver
    go to the hackerrank
    load the problems
    loop through all problems:
        copy a problem
        go to poe.com
        paste the problem
        copy the solution
        back to hackerrank
        paste the solution
    close driver

"""