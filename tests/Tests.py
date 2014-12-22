import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
from pages.AdvertPage import AdvertPage
from pages.AutorizPage import AutorizPage
from pages.CreateAdBuyPages.CreateAdBuyMotorbikePage import CreateAdBuyMotorbikePage
from pages.CreateAdBuyPages.IssueAdPage import IssueAdPage
from pages.CustAdPage import CustAdPage
from pages.LeftMenu import LeftMenu
from pages.MailBox import MailBox
from pages.MainPage import MainPage
from pages.MessagePage import MessagePage
from pages.MyStockPage import MyStockPage
from pages.PersonalMenu import PersonalMenu
from pages.RubricsPage import RubricsPage
from pages.CreateAdBuyPages.CreateAdBuyPage import CreateAdBuyPage


class Test(unittest.TestCase):


    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver=webdriver.Chrome("C:\\Users\\User\\IdeaProjects\\chromedriver.exe", chrome_options=chrome_options)
        self.driver.get("http://itebe.ru/")

    def tearDown(self):
        self.driver.close()

    #в этом тесте проверяется, что юзер может:
    #авторизироваться на сайте
    #выбирать себе разные роли(продавца, или покупателя)
    #разместить объявление
    #найти свое объявление в ЛК
    #а также, что другиие юзеры могут найти это объявление и связаться через сервис сообщений
    #с его владельцем для заключения сделки

    def Tests(self):

        log1="test_customer1"
        log2="test_seller"
        pas="123qwerty"
        #авторизируемся
        AutorizPage(self.driver).login(log1, pas)
        #проверяем, что действительно вошли по этому логину
        assert log1 in MainPage(self.driver).getUsername()
        LeftMenu(self.driver).getCurrentRole()

        role="продавец"
        # ставим роль "продавец"
        LeftMenu(self.driver).setRole(role)
        # проверяем, изменилась ли роль на указанную
        assert role in LeftMenu(self.driver).getCurrentRole()

        flmenu="Транспорт"
        slmenu="мототранспорт"
        thlmenu="скутеры"
        current_rubric=slmenu+": "+thlmenu
        # переходим в меню транспорт>мототранспорт>скутеры
        LeftMenu(self.driver).ClickMenu3(flmenu, slmenu, thlmenu)
        # проверяем, что пришли куда хотели
        assert current_rubric.lower() in RubricsPage(self.driver).getCurrentRubric()

        role="покупатель"
        #еще раз меняем роль, т.к. при смене роли ссылка в элементе изменяется, возникает исключение, которые мы ловим
        try:
            RubricsPage(self.driver).setRole(role)
        except StaleElementReferenceException:
            pass
        # проверяем, что роль изменилась
        assert role in LeftMenu(self.driver).getCurrentRole()

        advert="Suzuki"
        #переходим на страницу создания объявления о покупке (т.к. мы сейчас в роли покупателя) мотоцикла Сузуки
        RubricsPage(self.driver).addAdvert(advert)
        # проверяем, что действительно Сузуки
        assert advert.lower() in CreateAdBuyPage(self.driver).getCurrentRubric()


        #заполняем поля объявления
        model="Burgman 200"
        CreateAdBuyMotorbikePage(self.driver).setModelFromSelect(model)

        years=("2013", "2006", "2005", "1997", "1991")
        CreateAdBuyMotorbikePage(self.driver).setYearManuf(years)

        type="внедорожник"
        CreateAdBuyMotorbikePage(self.driver).setType(type)

        description="fwegfg ew efwgwegweg"
        CreateAdBuyMotorbikePage(self.driver).setAddDescr(description)

        #загружаем фото и проверяем, что оно загрузилось
        CreateAdBuyPage(self.driver).attachPhoto()
        self.assertTrue(CreateAdBuyPage(self.driver).isPictureNamePresent())

        price="234"
        CreateAdBuyMotorbikePage(self.driver).setPrice(price)

        CreateAdBuyMotorbikePage(self.driver).clickCheckButon()

        # а тут проверяем, что все, что ммы вводили, совпадает с тем, что сейчас отображается
        # на странице завершения создания объявления
        assert model in IssueAdPage(self.driver).getValueOfOneParamDescr("Модель")
        assert IssueAdPage(self.driver).convertYearsToSrt(years) in \
               IssueAdPage(self.driver).getValueOfOneParamDescr("Год выпуска")
        assert type in IssueAdPage(self.driver).getValueOfOneParamDescr("Тип")
        assert description in IssueAdPage(self.driver).getValueOfOneParamDescr("Дополнительное описание")
        self.assertTrue(IssueAdPage(self.driver).isPicturePresent())
        assert price in IssueAdPage(self.driver).getPrice(len(price))

        #завершаем создание объявления
        IssueAdPage(self.driver).finishCreateIssue()
        #запоминаем id нашего объявления
        advert_id=AdvertPage(self.driver).getId()

        #идем в ЛК
        MainPage(self.driver).goToPersCab()

        # находим наше объявление в ЛК по id
        self.assertTrue(MyStockPage(self.driver).isAdvertPresent(advert_id))

        #перелогиниваемся под другим юзером
        MainPage(self.driver).logOut()
        AutorizPage(self.driver).login(log2, pas)

        #выбираем роль продавца
        role="продавец"
        LeftMenu(self.driver).setRole(role)

        #идем в рубрику, где было размещено объявление
        LeftMenu(self.driver).ClickMenu3(flmenu, slmenu, thlmenu)
        RubricsPage(self.driver).ClickRubrick(advert)

        #находим наше объявление по названию модели и цене, и кликаем по нему
        CustAdPage(self.driver).clickAdvert(model, price)

        #отправляем сообщение владельцу объявления
        mess="i want sell scooter to you!"
        AdvertPage(self.driver).sendMess(mess)

        #снова логинимся под первым юзером
        MainPage(self.driver).logOut()
        AutorizPage(self.driver).login(log1, pas)

        #идем в раздел сообщения
        MainPage(self.driver).goToPersCab()
        PersonalMenu(self.driver).ClickMenu("Сообщения")

        #открываем последнее сообщение
        MailBox(self.driver).OpenLastMess()

        #убеждаемся, что сообщение пришло
        assert mess in MessagePage(self.driver).getTextMessage()

if __name__ =='__main__':
    unittest.main
