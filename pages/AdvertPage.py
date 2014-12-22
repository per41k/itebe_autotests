#страинца объявления
class AdvertPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.id=driver.find_element_by_xpath("//input[@id='id']")
        self.mess_field=driver.find_element_by_xpath("//textarea")
        self.send_button=driver.find_element_by_xpath("//input[@type='button']")

    def getId(self):
        return self.id.get_attribute("value")

    def sendMess(self, mess):
        self.mess_field.send_keys(mess)
        self.send_button.click()
