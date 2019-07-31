from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_settings_page import CartSettingsPage
from pages.login_page import LoginPage


browser = webdriver.Firefox()
login = '83451'
password = 'Lunch4bl35'
code_names = ['HRESFS182','HRESXK74','HRESFO179','HRESAH29','HRESHQ175','HRESIU152','HRESHC161','HRESTC25','HRESKG121','HRESPM112','HRESTG114','HRESXI33','HRESAJ73','HRESLU176','HRESFF61','HRESWA122','HRESTN171','HRESOY182','HRESPX46','HRESTC69','HRESZE137','HRESYL158','HRESNY33','HRESCJ176','HRESVZ193','HRESAT166','HRESLC169','HRESGJ169','HRESXT150','HRESUJ110','HRESOG52','HRESYV125','HRESYC50','HRESFJ94','HRESQQ46','HRESYL72','HRESHR129','HRESCC29','HRESPU60','HRESTT114']

cart_settings_page = CartSettingsPage(driver=browser)
cart_settings_page.go()

login_page = LoginPage(driver=browser)
login_page.url = browser.current_url
login_page.login_id_input.input_text(login)
login_page.password_input.input_text(password)
login_page.login_button.click()

cart_settings_page.wait_for_switch_to_frame()
cart_settings_page.tab('pricing').click()
