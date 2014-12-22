class MessagePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.text_mess=driver.find_element_by_xpath("//div[@class='msg set topmes']/span")

    def getTextMessage(self):
        return self.text_mess.text