from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator


class CartSettingsPage(BasePage):

	url = 'https://www.sagemember.com/sgadmin.exe/SelectSiteForEdit?UID=36218&Site=1000540'

	@property
	def code_input(self):
		locator = Locator(By.XPATH, "//input[@name='AddPCCode']")
		return BaseElement(self.driver, locator=locator)

	@property
	def percent_input(self):
		locator = Locator(By.XPATH, "//input[@name='AddPCPercentOff']")
		return BaseElement(self.driver, locator=locator)

	@property
	def dollar_input(self):
		locator = Locator(By.XPATH, "//input[@name='AddPCDollarsOff']")
		return BaseElement(self.driver, locator=locator)

	@property
	def code_no_limit(self):
		locator = Locator(By.XPATH, "//input[@name='AddPCReuseSetting'][@value='0']")
		return BaseElement(self.driver, locator=locator)

	@property
	def code_once_per_client(self):
		locator = Locator(By.XPATH, "//input[@name='AddPCReuseSetting'][@value='1']")
		return BaseElement(self.driver, locator=locator)

	@property
	def code_once_only(self):
		locator = Locator(By.XPATH, "//input[@name='AddPCReuseSetting'][@value='2']")
		return BaseElement(self.driver, locator=locator)

	@property
	def add_button(self):
		locator = Locator(By.XPATH, "/html/body/form/div[1]/div/div[4]/table/tbody/tr[3]/td[2]/div/div[2]/div[2]/input")
		return BaseElement(self.driver, locator=locator)


		