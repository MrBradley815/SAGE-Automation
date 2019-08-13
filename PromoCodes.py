from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_settings_page import CartSettingsPage
from pages.login_page import LoginPage


employee_id = input('Employee ID: ')
account_number = input('Account Number: ')
password = getpass.getpass()
codes = ['SALESXY182', 'SALESAX138', 'SALESBH178', 'SALESMP109', 'SALESFE56', 'SALESOM87', 'SALESGE137', 'SALESPA176', 'SALESBD35', 'SALESYG10', 'SALESGT37', 'SALESUM122', 'SALESSP184', 'SALESQA121', 'SALESGW97', 'SALESLU178', 'SALESRM183', 'SALESAF104', 'SALESIM55', 'SALESGJ160', 'SALESVZ156', 'SALESBT151', 'SALESWU28', 'SALESFK187', 'SALESSX192', 'SALESBO22', 'SALESSB198', 'SALESLH72', 'SALESDI69', 'SALESTG62', 'SALESJL44', 'SALESKF71', 'SALESRJ123', 'SALESZG111', 'SALESIM195', 'SALESKN52', 'SALESPX181', 'SALESVV178', 'SALESXI122', 'SALESIL22', 'MKTGRV11', 'MKTGWZ172', 'MKTGRG147', 'MKTGLM177', 'MKTGXW83', 'MKTGYY68', 'MKTGJM188', 'MKTGTY193', 'MKTGCF41', 'MKTGDW144', 'MKTGWV69', 'MKTGWB89', 'MKTGXT37', 'MKTGFY73', 'MKTGXO119', 'MKTGPN150', 'MKTGWJ110', 'MKTGTM66', 'MKTGEF88', 'MKTGUU60', 'MKTGYG153', 'MKTGIH43', 'MKTGSD170', 'MKTGUB121', 'MKTGAN73', 'MKTGMJ182', 'MKTGNY158', 'MKTGFX141', 'MKTGIV44', 'MKTGOM120', 'MKTGRR199', 'MKTGVQ130', 'MKTGUL156', 'MKTGNG27', 'MKTGHY193', 'MKTGQC59', 'MKTGAW102', 'MKTGLS19', 'MKTGLI182', 'MKTGGH83', 'HRESGI105', 'HRESJX154', 'HRESBW118', 'HRESTJ50', 'HRESXC126', 'HRESDQ126', 'HRESLL105', 'HRESTR90', 'HRESEA102', 'HRESOI31', 'HRESPA165', 'HRESLB74', 'HRESMB78', 'HRESOE183', 'HRESYT15', 'HRESHF174', 'HRESKP101', 'HRESDG167', 'HRESJG86', 'HRESCA126', 'HRESXW47', 'HRESJS94', 'HRESUM175', 'HRESCD103', 'HRESEM104', 'HRESYT35', 'HRESAZ10', 'HRESVB194', 'HRESJQ107', 'HRESMC57', 'HRESVP165', 'HRESEV23', 'HRESTK43', 'HRESJI42', 'HRESLP192', 'HRESJY142', 'HRESKV42', 'HRESYB12', 'HRESPT29', 'HRESKW87']

browser = webdriver.Firefox()

cart_settings_page = CartSettingsPage(driver=browser)
cart_settings_page.go()

login_page = LoginPage(driver=browser)
login_page.url = browser.current_url
login_page.login_id_input.input_text(f"{employee_id}:{account_number}")
login_page.password_input.input_text(password)
login_page.login_button.click()

WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/nav/div[2]/div/ul/li[3]/ul/li[20]/a')))
browser.find_element_by_xpath('/html/body/div/nav/div[2]/div/ul/li[3]/ul/li[20]/a').click()

cart_settings_page.wait_for_switch_to_frame()
cart_settings_page.tab('pricing').click()

once_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, cart_settings_page.code_once_only.locator.value)))
browser.execute_script('return arguments[0].scrollIntoView(true);', once_button)
once_button.click()

for code in codes:
	cart_settings_page.code_input.input_text(code)
	cart_settings_page.percent_input.input_text('100')
	cart_settings_page.dollar_input.input_text('100')
	cart_settings_page.add_button.click()

cart_settings_page.save.click()