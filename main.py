import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

search_term = "Python"
url = "https://book24.ua"

browser = webdriver.Chrome()
browser.get(url)
browser.implicitly_wait(30)
browser.find_element_by_css_selector('[id="onesignal-slidedown-cancel-button"]').click()

browser.find_element_by_css_selector('[id="title-search-input_fixed"]').send_keys(search_term)
browser.find_element_by_css_selector('[id="title-search-input_fixed"]').send_keys(Keys.ENTER)
time.sleep(5)

actual_text = browser.find_element_by_css_selector('[class="form-control"]').find_element_by_name('q').get_attribute('value')
expected_text = search_term

assert actual_text == expected_text
time.sleep(20)
browser.close()
