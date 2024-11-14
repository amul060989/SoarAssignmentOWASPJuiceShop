from pages.HomePage.Task2 import task2
import pytest
import unittest
from utils.test_status import TestStatus


@pytest.mark.usefixtures('oneTimeSetUp','setUp')
class Task2test(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.valiateCardPopUp = task2(self.driver)

        """
            Soft assertion only use if test case needed to be continued.
        """

        self.testStatus = TestStatus(self.driver)

    
    def test_task2(self):
        result = self.valiateCardPopUp.validatePopUpItems()
        self.testStatus.markFinal("Pop Items on Home page test ",result,".") 