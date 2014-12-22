from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

#страница создания объявлений о покупке мотоцикла
class CreateAdBuyMotorbikePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.model_field = driver.find_element_by_xpath("//input[@id='model']") #поле ввода модели
        self.description_field = driver.find_element_by_xpath("//textarea") #поле ввода дополнительного описания
        self.price_field = driver.find_element_by_xpath("//input[@name='p']") #поле ввода цены

    #выбрать модель из списка
    def setModelFromSelect(self, molel):
        selected_model=self.driver.find_element_by_xpath("//select[@name='vs']/option[text()='"+molel+"']")
        selected_model.click()

    # ввести название модели
    def setModel(self, model):
        self.model_field.clear()
        self.model_field.send_keys(model)

    #выбрать один год выпуска, ctrl+click, чтобы можно было выбрать нескольго годов
    def set_year(self, year):
        selected_year=self.driver.find_element_by_xpath("//select[@name='v1[]']/option[text()='"+year+"']")
        ActionChains(self.driver).key_down(Keys.CONTROL).click(selected_year).key_up(Keys.CONTROL).perform()

    #установить годы выпуска, медот получает список годов, список должен идти от большего к меньшему
    def setYearManuf(self, years):
        for year in years: self.set_year(year)

    #выбрать тип из списка
    def setType(self, type):
        selected_type=self.driver.find_element_by_xpath("//select[@name='v2']/option[text()='"+type+"']")
        selected_type.click()

    #ввести дополнительное описание
    def setAddDescr(self, description):
        self.description_field.clear()
        self.description_field.send_keys(description)

    #ввести цену
    def setPrice(self, price):
        self.price_field.clear()
        self.price_field.send_keys(price)

