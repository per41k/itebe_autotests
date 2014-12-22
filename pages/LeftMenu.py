from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

#страница меню навигации по сайту
class LeftMenu(object):

    def __init__(self, driver):
        self.driver = driver

        self.customer = driver.find_element_by_xpath("//label[@id='buy']") #кнопка, при нажатии на которую юзер получает роль покупателя
        self.seller = driver.find_element_by_xpath("//label[@id='sell']") # кнопка, при нажатии на которую юзер получает роль продавца
        self.i_am = driver.find_element_by_xpath("//p[@id='circle']") #ккопка в входа в ЛК
        self.current_role = driver.find_element_by_xpath("//span[@id='sb_note']/b") #элемент отображает текущую роль юзера

    #Меню слева имеет 3 уровня вложенности, но некоторые пункты меню имеют только 2 уровня вложенности
    #этот метод наводит курсор на указанный пункт меню первого уровня
    def focus_on_first_level_menu(self, name_menu):
        menu = self.driver.find_element_by_xpath("//ul[@id='nav']//b[text()='"+name_menu+"']")
        ActionChains(self.driver).move_to_element(menu).perform()

    #этот метод наводит курсор на указанный пункт меню второго уровня
    def focus_on_second_level_menu(self, name_menu):
        menu = self.driver.find_element_by_xpath("//li//b[text()='"+name_menu+"']")
        WebDriverWait(self.driver, 10).until(lambda driver: menu)
        ActionChains(self.driver).move_to_element(menu).perform()

    #этот медод наводит курсор и кликакает по указанному меню второго уровня вложенности
    def click_on_second_level_menu(self, name_menu):
        menu=self.driver.find_element_by_xpath("//li[@class='second']//b[text()='"+name_menu+"']")
        WebDriverWait(self.driver, 10).until(lambda driver: menu)
        ActionChains(self.driver).move_to_element(menu).perform()
        menu.click()

    #этот метод наводит курсор и кликает по указаному меню 3-го уровня вложенности
    def click_on_third_level_menu(self, name_menu):
        menu = self.driver.find_element_by_xpath("//b[text()='"+name_menu+"']")
        ActionChains(self.driver).move_to_element(menu).perform()
        WebDriverWait(self.driver, 10).until(lambda driver: menu)
        menu.click()

    #этот метод используется, если надо перейти в пункт меню во втором уровне вложенности
    def ClickMenu2(self, first_level_menu, second_level_menu):
        self.focus_on_first_level_menu(first_level_menu)
        self.click_on_second_level_menu(second_level_menu)

    #а этот - если нужный пунут меню находится на 3-м уровне
    def ClickMenu3(self, first_level_menu, second_level_menu, third_level_menu):
        self.focus_on_first_level_menu(first_level_menu)
        self.focus_on_second_level_menu(second_level_menu)
        self.click_on_third_level_menu(third_level_menu)

    #Метод устанавливает роль юзера: покупатель, или продавец. Этот метод работает норм только на главной
    def setRole(self, role):
        if role=="покупатель": self.customer.click()
        elif role=="продавец": self.seller.click()

    #перейти в ЛК
    def goToProfile(self): self.i_am.click()

    #Узнать свою текущую роль
    def getCurrentRole(self):
        WebDriverWait(self.driver, 10).until(lambda driver: self.current_role)
        return self.current_role.text.lower()[1:-1]







