
#страница завершения создания объявления, тут отображаются дааны введеные на странице создания объявления
class IssueAdPage(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.price = driver.find_element_by_xpath("//div[@class='price']/div") #цена
        self.issue_button = driver.find_element_by_xpath("//input[@type='submit']") #кнопка "Оформить"

    #метод проверяет, загрузилась ли фотка
    def isPicturePresent(self):
        picture=self.driver.find_element_by_xpath("//td//img")
        if picture.size !=0: return True
        else: return False

    #получить цену
    def getPrice(self, price_len):
        return self.price.text[:price_len]

    #метод получает один из параметров, значение которго было указано на странице создания объявления и возвращает эо значение
    def getValueOfOneParamDescr(self, param):
        return self.driver.find_element_by_xpath("//span[contains(.,'"+param+"')]/../span[2]").text

    #мы указывали года выпуска как элементы списка, а getValueOfOneParamDescr возвращает эти года как отсортированную
    #по уменьшению строку, поэтому надо преобразовать список в такую же строку, чтобы потом их можно было сравнить
    def convertYearsToSrt(self, years):
        year_str=""
        for year in years:
            year_str +=year+"\n"
        return year_str[:-1]

    #кликнуть "оформить"
    def finishCreateIssue(self):
        self.issue_button.click()