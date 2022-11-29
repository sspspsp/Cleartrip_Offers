from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from data import reading_object

locators = reading_object.read_locators()


class HotelOffers:
    def __init__(self,driver):
        self.driver=driver


    def cancel_popup(self):
        #cancel_popup
        time.sleep(2)
        self.driver.find_element(*locators["cancel_popup"]).click()
        time.sleep(2)

    def click_offers(self):
        #click_offers
        self.driver.find_element(*locators["click_offers"]).click()
        time.sleep(2)

    def click_hotels(self):
        #click_hotels
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        time.sleep(2)
        self.driver.find_element(*locators["click_hotels"]).click()
        time.sleep(2)

    def know_more(self):
        # know_more
        self.driver.find_element(*locators["know_more"]).click()
        time.sleep(4)
        time.sleep(2)

    def book_now(self):
        #book_now
        ac_obj = ActionChains(self.driver)
        time.sleep(2)
        ac_obj.send_keys(Keys.PAGE_DOWN)
        time.sleep(4)
        self.driver.find_element(*locators["book_now"]).click()
        time.sleep(3)

    def reset_filters(self):
        #reset_filters
        time.sleep(3)
        self.driver.find_element(*locators["reset_filters"]).click()
        time.sleep(2)





############################################################################################################


# path = r'D:\Downloads\chromedriver_win32/chromedriver.exe'
#
# driver = webdriver.Chrome(path)
# driver.get('https://www.cleartrip.com/')
# time.sleep(2)
# driver.maximize_window()
# driver.implicitly_wait(20)



# obj = HotelOffers()
# obj.cancel_popup()
# obj.click_offers()
# obj.click_hotels()
# obj.know_more()
# obj.book_now()
# obj.reset_filters()