
class Object:
    logo_by_xpath = "//*[@id='nav-bar']/div[1]/a/img"
    process_by_css_selector = "input[class='menu-item'][href='/#process']"
    process_by_xpath = "//*[@id='nav-bar']/div[2]/ul/li[1]/a"
    work_by_xpath = "//*[@id='nav-bar']/div[2]/ul/li[2]/a"
    careers_by_xpath = "//*[@id='nav-bar']/div[2]/ul/li[3]/a"
    contactUs_by_xpath = "//*[@id='nav-bar']/div[2]/ul/li[4]"

    partner_btn_by_xpath = "/html/body/section[1]/div/div/a"

    first_name_by_id = "contact-form-first-name"
    last_name_by_id = "contact-form-last-name"
    email_by_id = "contact-form-email"
    subject_by_id = "contact-form-subject"
    message_by_id = "contact-form-message"
    send_by_xpath = "//*[@id='contactus']/div/div/form/button"

    def __init__(self, driver):
        self.driver = driver

    def setLogo(self):
        self.driver.find_element_by_xpath(self.logo_by_xpath).click()

    def setProcess(self):
        self.driver.find_element_by_xpath(self.process_by_xpath).click()

    def setWork(self):
        self.driver.find_element_by_xpath(self.work_by_xpath).click()

    def setCareers(self):
        self.driver.find_element_by_xpath(self.careers_by_xpath).click()

    def setContactUs(self):
        self.driver.find_element_by_xpath(self.contactUs_by_xpath).click()

    def setPartnerBtn(self):
        self.driver.find_element_by_xpath(self.partner_btn_by_xpath).click()

    def setFirstName(self, firstName):
        self.driver.find_element_by_id(self.first_name_by_id).clear()
        self.driver.find_element_by_id(self.first_name_by_id).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element_by_id(self.last_name_by_id).clear()
        self.driver.find_element_by_id(self.last_name_by_id).send_keys(lastName)

    def setEmail(self, email):
        self.driver.find_element_by_id(self.email_by_id).clear()
        self.driver.find_element_by_id(self.email_by_id).send_keys(email)

    def setSubject(self, subject):
        self.driver.find_element_by_id(self.subject_by_id).clear()
        self.driver.find_element_by_id(self.subject_by_id).send_keys(subject)

    def setMessage(self, message):
        self.driver.find_element_by_id(self.message_by_id).clear()
        self.driver.find_element_by_id(self.message_by_id).send_keys()

    def setSendBtn(self):
        self.driver.find_element_by_xpath(self.send_by_xpath).click()






