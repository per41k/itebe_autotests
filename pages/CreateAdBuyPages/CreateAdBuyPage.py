import os
from selenium.webdriver.support.wait import WebDriverWait

#базовая страница создания объявления о покупке
class CreateAdBuyPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.current_rubric = driver.find_element_by_xpath("//span[@id='h1']") #текущая рубрика
        self.attach_photo_button = driver.find_element_by_xpath("//a[@class='w_dload_pc']") #кпока "Загрузить" загружает фотки
        self.check_button = driver.find_element_by_xpath("//input[@type='submit']") #кнопка "Проверить"

    #получить название текущей рубрики
    def getCurrentRubric(self):
        WebDriverWait(self.driver, 10).until(lambda driver: self.current_rubric)
        return self.current_rubric.text.lower()

    #добавть фото, метод открывает диалоговое окно и вызывает скрипт, котроый заагружает фотку
    def attachPhoto(self):
        self.attach_photo_button.click()
        os.startfile("C:\\Users\\User\\Documents\\Projects\\Learning\\itebe\\pages\\CreateAdBuyPages\\AttachPhoto.exe")
        WebDriverWait(self.driver, 50).until(lambda driver: self.driver.find_element_by_xpath("//div[@class='if1 fi']/img"))

    #после загрузки фото на страинце появляется название загруженного фото, метод проверят, так ли это
    def isPictureNamePresent(self):
        photo_name_element = self.driver.find_element_by_xpath("//div[@class='if1 fi']")
        if len( photo_name_element.text) !=0: return True
        else: return False

    #кликнуть "Проверить"
    def clickCheckButon(self): self.check_button.click()