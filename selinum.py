from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=tbnzAVRZ9Xc")
print(driver.title)