

class MyStockPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.issues_ids=driver.find_elements_by_xpath("//tbody//td[1]")

    def isAdvertPresent(self, id):
        for issue_name in self.issues_ids:
            if issue_name.get_attribute("data-id")==id:
                return True
            else:
                return False

    def getId(self, name):
        for issue_name in self.issues_names:
            if issue_name.text==name:
                return self.driver.find_element_by_xpath("//tbody//p/../../../td[1]").get_attribute("id")