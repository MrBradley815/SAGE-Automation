from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locator import Locator
from .base_element import BaseElement


class BasePage(object):

	url = None

	def __init__(self, driver):
		self.driver = driver

	def go(self):
		self.driver.get(self.url)

	def tab(self, tab):
		locator = Locator(By.XPATH, f"//a[@href='#{tab}']")
		return BaseElement(self.driver, locator=locator)

	def wait_for_switch_to_frame(self):
		WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it('ContentFrame'))

	@property
	def save(self):
		locator = Locator(By.XPATH, "//input[@name='Save']")
		return BaseElement(self.driver, locator=locator)