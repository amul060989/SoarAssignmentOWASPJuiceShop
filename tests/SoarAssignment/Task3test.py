from pages.UserRegistrationPage.Task3 import task3
import pytest
import unittest
from utils.test_status import TestStatus
from ddt import ddt,unpack,data
from utils.read_data import getData


@pytest.mark.usefixtures('oneTimeManualSetUp','setUp')
@ddt
class Task3test(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.validateRegisterPage = task3(self.driver)

        """
            Soft assertion only use if test case needed to be continued.
        """

        self.testStatus = TestStatus(self.driver)

    @data(*getData("testData/registerUser.csv"))
    @unpack
    def test_task3(self,email,password,answer):
        result = self.validateRegisterPage.registerToOWASPJuiceApp(email,password,answer)
        self.testStatus.markFinal("Register Page validation ",result,".") 