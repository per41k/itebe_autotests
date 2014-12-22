from selenium.webdriver.support.wait import WebDriverWait
from pages.LeftMenu import LeftMenu


class RubricsPage(object):

    def __init__(self, driver):
        self.driver = driver

        #Еще одна кнопка, которая меняет роль юзера, эта работает норм, но тоже со своими приколами
        #находит вверху справа формы создания объявления
        self.change_role_button = driver.find_element_by_xpath("//a[@class='revers']")
        self.current_rubric = driver.find_element_by_xpath("//div[@class='ff']/div/h1") #текущая рубрика

    #устанавливает роль юзера: покупатель, или продавец
    def setRole(self, role):
        current_role = LeftMenu(self.driver).getCurrentRole()
        if role != current_role: self.change_role_button.click()

    #метод получает название рубрики и кликает по "+" для перехода на страницу создания объявления в этой рубрике
    def addAdvert(self, rubric):
        advert = self.driver.find_element_by_xpath("//a[text()='"+rubric+"']/..//span[text()='+']")
        WebDriverWait(self.driver, 10).until(lambda driver: advert)
        advert.click()

    #получить название текущей рубрики
    def getCurrentRubric(self):
        WebDriverWait(self.driver, 10).until(lambda driver: self.current_rubric)
        return self.current_rubric.text.lower()

    #Перейти в указанную подрубрику
    def ClickRubrick(self, rubrick):
        self.driver.find_element_by_xpath("//a[text()='"+rubrick+"']").click()



