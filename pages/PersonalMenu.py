#меню в ЛК юзера
class PersonalMenu(object):

    def __init__(self, driver):
        self.driver = driver

    #кликает по указанному меню
    def ClickMenu(self, menu):
        self.driver.find_element_by_xpath("//ul[@class='h-menu']//a[contains(.,'"+menu+"')]").click()