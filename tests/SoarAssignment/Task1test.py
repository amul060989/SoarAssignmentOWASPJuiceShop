from pages.HomePage.Task1 import task1
import pytest
import unittest
from utils.test_status import TestStatus
from ddt import ddt,unpack,data
from utils.read_data import getData


@pytest.mark.usefixtures('oneTimeSetUp','setUp')
class getWeatherResultTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.getMaximumCards = task1(self.driver)

        """
            Soft assertion only use if test case needed to be continued.
        """

        self.testStatus = TestStatus(self.driver)

    
    def test_getWeatherData(self):
        result = self.getMaximumCards.validateMaximumCardOnHomePage()
        self.testStatus.markFinal("Maximum Card On Home page test",result,".")