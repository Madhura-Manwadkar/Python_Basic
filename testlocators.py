from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# driver = webdriver.Firefox(executable_path="F:\\Internship\\geckodriver.exe")

driver.get("https://www.rahulshettyacademy.com/angularpractice/")
#driver.find_element_by_name("name").send_keys("Madhurima")
driver.find_element_by_css_selector("input[name='name']").send_keys("Sana")

driver.find_element_by_name("email").send_keys("Shetty")

#select class provides the methods to handle the option is dropdown

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
# dropdown.select_by_value("M")

driver.find_element_by_id("exampleCheck1").click()

driver.find_element_by_xpath("//input[@type='submit']").click()

# print(driver.find_element_by_class_name("alert-success").text)

message = driver.find_element_by_class_name("alert-success").text

assert "success" in  message
# assert "success" in  message




