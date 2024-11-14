from base.selenium_driver import SeleniumDriver
import utils.customer_logger as cl
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class task3(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

    _welcomeBanner = "//mat-dialog-container[contains(@class,'mat-dialog-container')]"
    _closeWelcomeBanner = "//*[@aria-label='Close Welcome Banner']"
    _validateRegistrationPage = "//*[text()='User Registration']"
    _emailById = 'emailControl'
    _emailValidationError = "//mat-error[text()='Please provide a password. ']"
    _passwordById = "passwordControl"
    _passwordValidationError = "//mat-error[text()='Please provide a password. ']"
    _repeatPasswordById = "repeatPasswordControl"
    _repeatpasswordValidationError = "//mat-error[text()=' Please repeat your password. ']"
    _toggleById = "mat-slide-toggle-1"
    _securityQuestion = "//mat-select"
    _matOptionSelect = "(//mat-option)[2]"
    _securityQuestionValidationError="//mat-error[text()=' Please select a security question. ']"
    _answerById = "//input[@placeholder='Answer to your security question']"
    _answerValidationError="//mat-error[text()=' Please provide an answer to your security question. ']"
    _registerButton = "//*[text()=' Register ']/parent::button"
    _registerSuccess = "//*[text()='Registration completed successfully. You can now log in.']"


    def registrationPageValidations(self):
        self.elementClick(locator=self._emailById,locatorType='id')
        self.elementClick(locator=self._passwordById,locatorType='id')
        self.elementClick(locator=self._repeatPasswordById,locatorType='id')

        #Validate Input errors

        emailValidationErrorElement = self.getElement(locator=self._emailValidationError,locatorType='xpath')
        passwordValidationErrorElement = self.getElement(locator=self._passwordValidationError,locatorType='xpath')


        if(emailValidationErrorElement and passwordValidationErrorElement):
            return True
        else:
            return False



    def registerToOWASPJuiceApp(self,email,password,answer):
        """
        Check if home page is loaded, if yes the perform test else fail.
        """
        self.driver.implicitly_wait(5)

        welcomeBanner = self.getElement(locator=self._welcomeBanner,locatorType='xpath')
        if welcomeBanner:
            self.elementClick(locator=self._closeWelcomeBanner, locatorType='xpath')

        registerPage = self.getElement(locator=self._validateRegistrationPage,locatorType='xpath')
        
        errorValidation = self.registrationPageValidations()

        if (registerPage and errorValidation):
            self.sendKeys(email,locator=self._emailById,locatorType='id')
            self.driver.implicitly_wait(1)
            self.sendKeys(password,locator=self._passwordById,locatorType='id')
            self.driver.implicitly_wait(1)
            self.sendKeys(password,locator=self._repeatPasswordById,locatorType='id')
            self.driver.implicitly_wait(1)
            self.elementClick(locator=self._securityQuestion,locatorType='xpath')
            self.driver.implicitly_wait(1)
            self.elementClick(locator=self._matOptionSelect,locatorType='xpath')
            self.driver.implicitly_wait(1)
            self.getElement(locator=self._answerById,locatorType='xpath').click().sendKeys(answer)
            
            self.driver.implicitly_wait(1)

            self.elementClick(locator=self._registerButton,locatorType='xpath')

            self.driver.implicitly_wait(3)

            successRegister = self.getElement(locator=self._registerSuccess,locatorType='xpath')

            if(successRegister):
                return True
            else:
                return False

        else:
            return False