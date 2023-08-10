from pages.getWeatherData.getWeatherData import getWeatherData
import pytest
import unittest
from utils.test_status import TestStatus
from ddt import ddt,unpack,data
from utils.read_data import getData


@pytest.mark.usefixtures('oneTimeSetUp','setUp')
@ddt
class getWeatherResultTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.getSearch = getWeatherData(self.driver)

        """
            Soft assertion only use if test case needed to be continued.
        """

        self.testStatus = TestStatus(self.driver)

    @data(*getData("testData/getWeatherData.csv"))
    @unpack
    def test_getWeatherData(self,searchQuery):
        result = self.getSearch.validateSearchResult(searchQuery)
        self.testStatus.markFinal("getWeatherData",result,"Delhi Weather")