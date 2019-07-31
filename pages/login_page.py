from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator


class LoginPage(BasePage):

	url = 'https://www.sagemember.com'

	@property
	def login_id_input(self):
		locator = Locator(By.XPATH, "//input[@name='SAGEID']")
		return BaseElement(self.driver, locator=locator)

	@property
	def password_input(self):
		locator = Locator(By.XPATH, "//input[@name='SAGEPassword']")
		return BaseElement(self.driver, locator=locator)

	@property
	def login_button(self):
		locator = Locator(By.XPATH, "//button[@type='submit']")
		return BaseElement(self.driver, locator=locator)
	
