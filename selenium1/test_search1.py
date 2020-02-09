## Test Case
# 1. Open browser chrome browser
# 2. Launch the 'automationpractice.com'
# 3. Enter 't-shirt' in search box
# 4. Click search button (option2: hit ENTER key on keyboard)
# 5. Verify at least one product displayed/appeared

from selenium import webdriver
import time

# CONSTANTS
chrome_url = "C:\\dev\\chromedriver_win32\\chromedriver.exe"
home_url = "http://automationpractice.com"
keyword = 't-shirt'

def test_searching():
    # step: 1
    driver = webdriver.Chrome(chrome_url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    # step: 2
    driver.get(home_url)
    # step: 3
    driver.find_element_by_name("search_query").send_keys(keyword)
    # step: 4
    time.sleep(5)
    driver.find_element_by_name("submit_search").click()
    products_list = driver.find_elements_by_xpath("//*[@id='center_column']/ul/li")
    # step: 5
    assert len(products_list) >= 1
    time.sleep(5)
    # step: 6 - closing the browser
    driver.quit()
