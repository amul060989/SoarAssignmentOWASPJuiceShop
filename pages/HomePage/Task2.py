from base.selenium_driver import SeleniumDriver
import utils.customer_logger as cl
import logging
import time

class task2(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

    _homePageJuiceShopTitle = "//span[text()='OWASP Juice Shop']"
    _homePageIdentifier = "//*[contains(text(),'All Products')]"
    _firstElementAppleJuice = "//*[contains(text(),'Apple Juice')]/ancestor::mat-card"
    _cardIsOpen = "//mat-dialog-container//child::div/h1[contains(text(),'')]"
    _cardImage = "//app-product-details//child::img"
    _welcomeBanner = "//mat-dialog-container[contains(@class,'mat-dialog-container')]"
    _review = "//mat-expansion-panel-header[@role='button']"
    _closeButton = "//*[text()=' Close']/parent::span"
    _closeWelcomeBanner = "//*[@aria-label='Close Welcome Banner']"

    def clickOnFirstItem(self):
        self.elementClick(locator=self._firstElementAppleJuice,locatorType='xpath')
        self.driver.implicitly_wait(1)


    def clickReviewSection(self):
        self.elementClick(locator=self._review,locatorType='xpath')

    def closePopUp(self):
        self.elementClick(locator=self._closeButton,locatorType='xpath')
    

    def validatePopUpItems(self):
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
            self.clickOnFirstItem()

            self.driver.implicitly_wait(1)

            checkFirstElement = self.getElement(locator=self._cardIsOpen,locatorType='xpath')
            element = self.getElement(locator=self._cardImage,locatorType='xpath')
            imageUrl = element.get_attribute('src')

            assert(checkFirstElement != None)
            assert(imageUrl != "")

            self.driver.implicitly_wait(1)

            self.clickReviewSection()

            time.sleep(2)

            self.closePopUp()
            
            return True

        else:
            return False

