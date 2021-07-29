import XLUtils
from selenium import webdriver
from TestObjects.Objects import Object

driver = webdriver.Chrome(r'C:\Users\Shree\PycharmProjects\Project\pythonProject\pythonProject\RTI_Test_Project\drivers\chromedriver.exe')
obj = Object(driver)
driver.maximize_window()
driver.get('https://www.redthreadinnovations.com/')
obj.setContactUs()

path = 'data/ddt.xlsx'

rows = XLUtils.getRowCount(path, 'Sheet1')
for r in range(2, rows + 1):
    firstname = XLUtils.readData(path, 'Sheet1', r, 1)
    lastname = XLUtils.readData(path, 'Sheet1', r, 2)
    email = XLUtils.readData(path, 'Sheet1', r, 3)
    subject = XLUtils.readData(path, 'Sheet1', r, 4)
    message = XLUtils.readData(path, 'Sheet1', r, 5)

    obj.setFirstName(firstname)
    obj.setLastName(lastname)
    obj.setEmail(email)
    obj.setSubject(subject)
    obj.setMessage(message)
    obj.setSendBtn()

    elements = driver.find_element_by_xpath('//*[@id="contactus"]/div/div/form/div[6]/h3')
    if elements == 'Message sent':
        print('Test is pass')
        XLUtils.writeData(path, 'Sheet1', r, 6, 'Test Passed')
    else:
        print('Test is fail')
        XLUtils.writeData(path, 'Sheet1', r, 6, 'Test Failed')
    obj.setLogo()
