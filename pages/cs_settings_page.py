from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator


class CSSettingsPage(BasePage):

	url = 'https://www.sagemember.com/sgadmin.exe/SelectSiteForEdit?UID=32506&Site=CS20142'

	@property
	def name_input_1(self):
		locator = Locator(By.XPATH, "//input[@name='CustomCheckOut1Name']")
		return BaseElement(self.driver, locator=locator)

	@property
	def value_input_1(self):
		locator = Locator(By.XPATH, "//input[@name='CF1NameAdd']")
		return BaseElement(self.driver, locator=locator)

	@property
	def add_button_1(self):
		locator = Locator(By.XPATH, "//*[@id='cart']/table/tbody/tr[18]/td[2]/div[1]/div[3]/div[2]/input")
		return BaseElement(self.driver, locator=locator)