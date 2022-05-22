from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


# 1. Khai báo biến browser
browser = webdriver.Chrome(executable_path='C:/Webdrivers/chromedriver.exe')

# 2. Mở trang web Fb
browser.get(url='https://www.facebook.com')

# 2a. Điền thông tin vào ô User , Pass
txtUser = browser.find_element_by_id("email")
txtUser.send_keys("vnpt2021n1@gmail.com") # Điền user thật

txtPass = browser.find_element_by_id("pass") # Điền pass thật
txtPass.send_keys("Vnpt@2021")

# 2b. Submit Form
txtPass.send_keys(Keys.ENTER)

# 3. Dừng chương trình 5s
# sleep(5)

# 4. Đóng trình duyệt
# browser.close()
