import getpass

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cs_settings_page import CSSettingsPage
from pages.login_page import LoginPage


employee_id = input('Employee ID: ')
account_number = input('Account Number: ')
password = getpass.getpass()
countries = ["United States","Canada","Afghanistan","Albania","Algeria","American Samoa","Andorra","Angola","Anguilla","Antarctica","Antigua And Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia And Herzegowina","Botswana","Bouvet Island","Brazil","British Indian Ocean Territory","Brunei Darussalam","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Canada","Cape Verde","Cayman Islands","Central African Republic","Chad","Chile","China","Christmas Island","Cocos (Keeling) Islands","Colombia","Comoros","Congo","Cook Islands","Costa Rica","Cote D'Ivoire","Croatia","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","East Timor","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","France, Metropolitan ","French Guiana","French Polynesia","French Southern Territories","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guadeloupe","Guam","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Heard And Mc Donald Islands","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Kuwait","Kyrgyzstan","Lao People's Republic","Latvia","Lebanon","Lesotho","Liberia","Libyan Arab Jamahiriya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Martinique","Mauritania","Mauritius","Mayotte","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montserrat","Morocco","Mozambique","Myanmar","Namibia","Nauru","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Niue","Norfolk Island","North Korea","Northern Mariana Islands","Norway","Oman","Other-Not Shown","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Pitcairn","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russian Federation","Rwanda","Saint Kitts And Nevis","Saint Lucia","Saint Vincent And The Grenadines","Samoa","San Marino","Sao Tome And Principe","Saudi Arabia","Senegal","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Georgia and South Sandwich Islands","South Korea","Spain","Sri Lanka","St Helena","St Pierre and Miquelon","Sudan","Suriname","Svalbard And Jan Mayen Islands","Swaziland","Sweden","Switzerland","Syrian Arab Republic","Taiwan","Tajikistan","Tanzania","Thailand","Togo","Tokelau","Tonga","Trinidad And Tobago","Tunisia","Turkey","Turkmenistan","Turks And Caicos Islands","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","selected="">United States","United States Minor Outlying Islands","Uruguay","Uzbekistan","Vanuatu","Vatican City State","Venezuela","Viet Nam","Virgin Islands (British)","Virgin Islands (U.S.)","Wallis And Futuna Islands","Western Sahara","Yemen","Zaire","Zambia","Zimbabwe"]

browser = webdriver.Firefox()

cs_settings_page = CSSettingsPage(driver=browser)
cs_settings_page.go()

login_page = LoginPage(driver=browser)
login_page.url = browser.current_url
login_page.login_id_input.input_text(f"{employee_id}:{account_number}")
login_page.password_input.input_text(password)
login_page.login_button.click()

cs_settings_page.wait_for_switch_to_frame()
cs_settings_page.tab("cart").click()
cs_settings_page.name_input_1.input_text("Country")
for country in countries:
	cs_settings_page.value_input_1.input_text(country)
	cs_settings_page.add_button_1.click()
cs_settings_page.save.click()







