
#страница списка объявлений о покупке
from selenium.webdriver.support.wait import WebDriverWait


class CustAdPage(object):

    def __init__(self, driver):
        self.driver = driver


    def isAdvertPresent(self, id):
        for issue_name in self.issues_names:
            if issue_name.get_attribute("id")==id:
                return True
            else:
                return False

    def clickAdvert(self, model, price):
        self.driver.find_element_by_xpath("//tbody//td[2][text()='"+model+"']/..//i[text()='"+price+"']").click()

