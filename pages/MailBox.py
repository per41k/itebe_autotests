class MailBox(object):

    def __init__(self, driver):
        self.driver = driver
        self.messages = driver.find_elements_by_xpath("//tr[@class='onclick3 skin1']")


    def OpenLastMess(self):
        self.messages[0].click()




