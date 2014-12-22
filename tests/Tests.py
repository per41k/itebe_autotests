import unittest
from selenium import webdriver
from pages.AutorizPage import AutorizPage
from pages.MainPage import MainPage
from pages.MyStockPage import MyStockPage
from pages.PersonalMenu import PersonalMenu


class Test(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome("C:\\Users\\User/IdeaProjects\\chromedriver.exe")
        self.driver.get("http://itebe.ru/")

    def tearDown(self):
        self.driver.close()

    def testlogin(self):

        log="test_customer1"
        pas="123qwerty"
        AutorizPage(self.driver).login(log, pas)

        MainPage(self.driver).goToPersCab()
        PersonalMenu(self.driver).printMenu()
        MyStockPage(self.driver).getNameAdvert()

if __name__ =='__main__':
    unittest.main