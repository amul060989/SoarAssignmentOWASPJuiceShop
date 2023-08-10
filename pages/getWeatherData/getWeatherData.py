from base.selenium_driver import SeleniumDriver
import utils.customer_logger as cl
import logging
from selenium.webdriver.common.by import By
import time

class getWeatherData(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

    _acceptCookies = "//button[text()='Accept all cookies']"
    _siteLandingIdentifier = "(//*[@alt='Visual Crossing Corporation'])[1]"
    _weatherDataOption = "(//*[text()='Weather Data'])[1]"
    _searchPageText = "//*[text()='Total Weather Data']"
    _searchBar = "//input[@class='form-control' and @placeholder='Enter a location']"
    _searchButton = "//*[@type='submit' and text()='Search']"
    _getTextSearchCityName = "(//*[contains(text(),'Historical weather data')])[2]"


    def clickOnWeatherDataOption(self):
        self.elementClick(locator=self._weatherDataOption,locatorType='xpath')

    def searchText(self,data):
        self.sendKeys(data,locator=self._searchBar,locatorType='xpath')

    def clickSearchButton(self):
        self.elementClick(locator=self._searchButton,locatorType='xpath')

    def validateSearchResult(self,searchQuery):
        checkCookiesPopUp = self.isElementPresent(locator=self._acceptCookies,locatorType='xpath')
        if checkCookiesPopUp:
            self.elementClick(locator=self._acceptCookies,locatorType='xpath')

        self.isElementPresent(locator=self._siteLandingIdentifier,locatorType='xapth')
        self.driver.implicitly_wait(0.5)
        self.clickOnWeatherDataOption()
        self.driver.implicitly_wait(1)
        self.isElementPresent(locator=self._searchPageText,locatorType='xpath')
        self.driver.implicitly_wait(0.5)
        self.searchText(searchQuery)
        self.clickSearchButton()
        self.driver.implicitly_wait(1)
        time.sleep(5)
        resultText = self.driver.find_element(By.XPATH,self._getTextSearchCityName)

        if resultText:
    
            returnedText = resultText.text

            if searchQuery in returnedText:

                return True
            
            else:
                
                return False
            
        else:
            return False


        

