#страинца сообщений юзера в ЛК
class MailBox(object):

    def __init__(self, driver):
        self.driver = driver
        self.messages = driver.find_elements_by_xpath("//tr[@class='onclick3 skin1']")

    #метод открывает последнее полученное сообщее
    def OpenLastMess(self):
        self.messages[0].click()




