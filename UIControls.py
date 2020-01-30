from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_element_by_xpath("//input[@type='checkbox']")
# print(len(checkboxes))

for checkbox in checkboxes:
    # print(checkbox.get_atttibute("value"))
    if checkbox.get_atttibute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

radiobutton = driver.find_element_by_name("radioButton")
radiobutton[2].click()
radiobutton[2].is_selected()

