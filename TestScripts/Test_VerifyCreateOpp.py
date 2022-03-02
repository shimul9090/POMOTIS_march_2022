import random

from Pages.Home import HomePage
from Pages.Login import LoginPage
from Pages.NewOpportunity import OpportunityPage
from conftest import BaseTest


class Test_VerifyCreateOpportunity(BaseTest):
    def test_VerifyNewOpp(self):
        self.lp = LoginPage(self.driver)
        self.lp.application_Login("Shimulah","X7emy88ccc")

        self.hm = HomePage(self.driver)
        self.hm.clickOpp()

        self.opp = OpportunityPage(self.driver)
        randNum = random.randint(1,100)
        strRandNum = str(randNum)
        self.opp.createOpp("2U","TestTitle"+strRandNum,"Asia - 9ORA (9IRC)","Health","test description","03032024","04042024","100","200.00","CRRD")

        succMsg = self.opp.oppCreatedSuccessfully()
        if "TestTitle"+strRandNum in succMsg:
            assert True,"Opportunity created successfully"
        else:
            assert False,"Opportunity creation failed"
