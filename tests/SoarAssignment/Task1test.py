from pages.HomePage.Task1 import task1
import pytest
import unittest
from utils.test_status import TestStatus


@pytest.mark.usefixtures('oneTimeSetUp','setUp')
class Task1test(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.getMaximumCards = task1(self.driver)

        """
            Soft assertion only use if test case needed to be continued.
        """

        self.testStatus = TestStatus(self.driver)

    
    def test_task1(self):
        result = self.getMaximumCards.validateMaximumCardOnHomePage()
        self.testStatus.markFinal("Maximum Card On Home page test",result,".")