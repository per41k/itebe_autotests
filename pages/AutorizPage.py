
#страница авторизации
class AutorizPage(object):

    def __init__(self, driver):
        self.driver = driver

        self.log_field = driver.find_element_by_xpath("//input[@name='log']") #поле ввода логина
        self.pass_field = driver.find_element_by_xpath("//input[@name='pas']") #поле ввода пароля
        self.log_button = driver.find_element_by_xpath("//input[@type='submit']") # кнопка "Войти"

    #метод очищает поле логина и водит в него полученное значение логина
    def setlogin(self, log):
        self.log_field.clear()
        self.log_field.send_keys(log)

    #метод очищает поле пароля и водит в него полученное значение пароля
    def setpass(self, pas):
        self.pass_field.clear()
        self.pass_field.send_keys(pas)

    #медот кликает по кнопке "Войти"
    def clickbutton(self):
        self.log_button.click()

    #метод авторизации на сайте
    def login(self, log, pas):
        self.setlogin(log)
        self.setpass(pas)
        self.clickbutton()