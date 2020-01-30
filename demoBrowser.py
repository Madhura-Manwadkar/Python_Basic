from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we need to invoke the executable file which will then invoke actual browser

#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="F:\Internship\geckodriver.exe")
driver = webdriver.Ie(executable_path="F:\Internship\IEDriverServer.exe")

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")    #get method to hit on a speific browser

print(driver.title)     #shows the title of the webpage
print(driver.current_url)      #gets the current url we have used (on which u are landed)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()       #to come back on browser.
driver.refresh()       #to refresh.

driver.close()

#driver.quick