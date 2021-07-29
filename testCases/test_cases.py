from selenium import webdriver
import pytest
from TestObjects.Objects import Object
from utilities.customeLogger import LogGen


class TestRTI:
    baseURL = 'https://www.redthreadinnovations.com/'
    open_Browser = webdriver.Chrome(r'C:\Users\Shree\PycharmProjects\Project\pythonProject\pythonProject\RTI_Test_Project\drivers\chromedriver.exe')

    def testRTI1_1(self):
        self.logger = LogGen.log_generate()
        self.logger.info("**************** RTI1.1 Test Start ******************")
        self.driver = self.open_Browser
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        title = self.driver.title
        if title == 'Red Thread Innovations':
            assert True
            self.logger.info("**************** RTI1.1 Test Pass ******************")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.info("**************** RTI1.1 Test Fail ******************")
            assert False

    def testRTI1A_1(self):
        self.logger = LogGen.log_generate()
        self.logger.info("**************** RTI1A.1 Test Start ******************")
        self.driver = self.open_Browser
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.obj = Object(self.driver)
        self.obj.setPartnerBtn()

        element = self.driver.find_element_by_xpath('//*[@id="contactus"]/div/div/div/h1')
        if element.text == 'Get in touch':
            assert True
            self.logger.info("**************** RTI1A.1 Test Pass ******************")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.info("**************** RTI1A.1 Test Fail ******************")
            assert False