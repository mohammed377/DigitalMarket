from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://poe.com/login")
time.sleep(40)
driver.find_element(By.CLASS_NAME,"ChatMessageInputView_textInput__Aervw").send_keys("Hi")
driver.find_element(By.CLASS_NAME,"ChatMessageInputView_sendButton__reEpT").click()
time.sleep(10)
mychats = driver.find_elements(By.CLASS_NAME,"ChatMessage_messageRow__7yIr2")
answer= mychats[-1]
time.sleep(30)

