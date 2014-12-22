
class PersonalMenu(object):

    def __init__(self, driver):
        self.driver = driver

    def ClickMenu(self, menu):
        self.driver.find_element_by_xpath("//ul[@class='h-menu']//a[contains(.,'"+menu+"')]").click()

    def printMenu(self):
        a=self.driver.find_element_by_xpath("//ul[@class='h-menu']//a[1]")
        print(a.text)