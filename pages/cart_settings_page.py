from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator


class CartSettingsPage(BasePage):

	url = 'https://www.sagemember.com/sgadmin.exe/Settings?Pg=CartSettings&UID=83451'

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
