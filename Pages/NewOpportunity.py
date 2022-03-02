import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class OpportunityPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    donorBox = (By.CSS_SELECTOR,"#DonorId_chosen > a")
    selectDonor = (By.CSS_SELECTOR,"#DonorId_chosen > div > div > input[type=text]")
    ircTitle = (By.NAME,"Title")
    progArea = (By.NAME,"ProgramAreaId")
    fundingType = (By.NAME,"FundingTypeId")
    leadUnit = (By.NAME,"SubmittingOrganizationalUnit")
    units = (By.CSS_SELECTOR,"#selReceivingOrgUnitsWithT5Codes_chosen > ul")
    unitsTextBox = (By.CSS_SELECTOR,"#selReceivingOrgUnitsWithT5Codes_chosen > ul > li > input")
    outcomeAreas = (By.CSS_SELECTOR,"#OutcomeAreas_chosen")
    outcomeAreasTextbox = (By.CSS_SELECTOR,"#OutcomeAreas_chosen > ul > li > input")
    description = (By.NAME,"Description")
    oppRelased = (By.CSS_SELECTOR,"#createFieldset > div:nth-child(8) > div > div > label.radio-inline.hide-popon > input[type=radio]")
    IRCSuccess = (By.NAME,"LikelihoodIrcIsSuccessfullId")
    relDate = (By.ID,"EstimatedToRReleaseDate")
    dueDate = (By.ID,"EstimatedProposalSubmissionDate")
    oppValue = (By.NAME,"EstimatedSolicitationValue")
    oppValueToIRC = (By.NAME,"EstimatedSolicitationValueToIRC")
    createOpportunity = (By.XPATH,"(//input[contains(@value,'Create Opportunity')])[2]")

    oppCreated = (By.CSS_SELECTOR,"#content > section > section > section > section > header > section > aside > section > section > div > div.col-sm-8 > div > div.m-b-md > h4")

    def createOpp(self,donor,title,unitsOrOff,outAreas,desc, realseDate, due_date, estValue, estOppValueIRC,PrgomArea):
        self.do_click(self.donorBox)
        self.do_sendKeys(self.selectDonor,donor)
        self.hit_Enter(self.selectDonor)
        self.do_sendKeys(self.ircTitle,title)
        self.do_selectFromDropdownByText(self.progArea,PrgomArea)
        self.do_selectFromDropdown(self.fundingType,1)
        self.do_selectFromDropdown(self.leadUnit,1)
        self.do_click(self.units)
        self.do_sendKeys(self.unitsTextBox,unitsOrOff)
        self.hit_Enter(self.unitsTextBox)
        self.do_click(self.outcomeAreas)
        self.do_sendKeys(self.outcomeAreasTextbox,outAreas)
        self.hit_Enter(self.outcomeAreasTextbox)
        self.do_sendKeys(self.description,desc)
        time.sleep(3)
        self.do_click(self.oppRelased)
        self.do_selectFromDropdown(self.IRCSuccess,1)
        self.do_sendKeys(self.relDate,realseDate)
        self.do_sendKeys(self.dueDate,due_date)
        self.do_sendKeys(self.oppValue,estValue)
        self.do_sendKeys(self.oppValueToIRC,estOppValueIRC)
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.hit_Tab(self.oppValueToIRC)
        self.hit_Enter(self.createOpportunity)

    def oppCreatedSuccessfully(self):
        confText = self.do_getText(self.oppCreated)
        return confText