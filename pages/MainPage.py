class MainPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.username = driver.find_element_by_xpath("//div[@class='est']") #логин юзера, отображается вверху справа
        self.quit_button = driver.find_element_by_xpath("//a[text()='Выход']") #кнопка выхода
        self.pers_cab = driver.find_element_by_xpath("//a[text()='Личный кабинет']") #

    #получить логин текущего юзера
    def getUsername(self): return self.username.text

    #разлогиниться
    def logOut(self): self.quit_button.click()

    #зайти в ЛК
    def goToPersCab(self): self.pers_cab.click()