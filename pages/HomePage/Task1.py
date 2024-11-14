from base.selenium_driver import SeleniumDriver
import utils.customer_logger as cl
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class task1(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

    _homePageJuiceShopTitle = "//span[text()='OWASP Juice Shop']"
    _homePageIdentifier = "//*[contains(text(),'All Products')]"
    _bottomPageElement = "//*[text()=' Items per page: ']//following::mat-form-field"
    _itemPerPageSelector = "//mat-select[@role='combobox']"
    _selectMaximumObjects = "//span[@class='mat-option-text' and text()=48]"
    _fieldToObtainTotalCards="//div[@class='mat-paginator-range-label']"
    _totalMatCards = "//mat-card"
    _welcomeBanner = "//mat-dialog-container[contains(@class,'mat-dialog-container')]"
    _closeWelcomeBanner = "//*[@aria-label='Close Welcome Banner']"

    def scrollToBottomOfPage(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.getElement(locator=self._bottomPageElement,locatorType='xpath')
        

    def changeItemsPerPage(self):
        self.elementClick(locator=self._itemPerPageSelector,locatorType='xpath')
        
        self.driver.implicitly_wait(1)

        if(self.getElement(locator=self._selectMaximumObjects,locatorType='xpath')):

            self.elementClick(locator=self._selectMaximumObjects,locatorType='xpath')

    def getTotalCards(self):
        totalCards = self.getElement(locator=self._fieldToObtainTotalCards,locatorType='xpath')
        inputText = totalCards.text
        splittedText = inputText.split('of')
        
        return int(splittedText[-1].strip())


    def validateMaximumCardOnHomePage(self):
        """
        Check if home page is loaded, if yes the perform test else fail.
        """
        self.driver.implicitly_wait(5)

        welcomeBanner = self.getElement(locator=self._welcomeBanner,locatorType='xpath')
        if welcomeBanner:
            self.elementClick(locator=self._closeWelcomeBanner, locatorType='xpath')

        homePageTitle = self.getElement(locator=self._homePageJuiceShopTitle,locatorType='xpath')
        homePageHeading = self.getElement(locator=self._homePageIdentifier,locatorType='xpath')

        if (homePageTitle and homePageHeading):
            self.scrollToBottomOfPage()
            self.driver.implicitly_wait(1)
            self.changeItemsPerPage()
            self.driver.implicitly_wait(1)
            totalCardsToValidate = self.getTotalCards()
            self.driver.implicitly_wait(1)
            validateTotalElements = self.getElements(locator=self._totalMatCards,locatorType='xpath')

            if (len(validateTotalElements) == totalCardsToValidate):
                return True
            else:
                return False

        else:
            return False



        


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
        # time.sleep(5)
        resultText = self.driver.find_element(By.XPATH,self._getTextSearchCityName)

        if resultText:
    
            returnedText = resultText.text

            if searchQuery in returnedText:

                return True
            
            else:
                
                return False
            
        else:
            return False


        

