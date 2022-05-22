from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from random import randint

# 1. Khai báo biến browser
path = "C:/Webdrivers/chromedriver.exe"
s = Service(path)
browser = webdriver.Chrome(service=s)


# 2. Mở trang web Fb
browser.get(url='https://www.facebook.com/beatvn.network/posts/3313788998938438')
sleep(4)



# Đăng nhập
txtUser = browser.find_element(By.ID, "email")
txtUser.send_keys("vnpt2021n1@gmail.com") # Điền user thật

txtPass = browser.find_element(By.ID, "pass") # Điền pass thật
txtPass.send_keys("Vnpt@2021")
txtPass.send_keys(Keys.ENTER) # Enter key
sleep(8)

# 3. Lấy link AllComments , Most relevent, Newest
showcomment_link = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[2]/div[2]/div/div/div/span")
showcomment_link.click()
sleep(3)

# Lấy link AllComments và click
showallcomments_link = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[3]/div[1]/div/div[2]/span")
showallcomments_link.click()
sleep(3)

# Lấy link more comment
showmorecomments_link = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[2]/div[4]/div[1]/div[2]/span")
showmorecomments_link.click()
sleep(5)

# showmorecomments_link.click()
# sleep(5)
#comment_list = browser.find_elements_by_class_name("l9j0dhe7 ecm0bbzt rz4wbd8a qt6c0cv9 dati1w0a j83agx80 btwxx1t3 lzcic4wl")
#comment_list = browser.find_elements_by_class_name("rj1gh0hx buofh1pr ni8dbmo4 stjgntxs hv4rvrfc")
comment_list = browser.find_elements(By.XPATH, "//div[@role='article']")
# print(comment_list)

# for comment in comment_list:
#     poster = comment.find_element(By.XPATH, '//*[@id="mount_0_0_Wn"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[2]/ul/li[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div/div/div/span/div/div')
#     #content = comment.find_element(By.CLASS_NAME, "d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id")
#     print("*", poster.text, ":")
    #, content.text
# Lấy link AllComments và click
# showmorecomments_link = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[3]/div[2]/div/a")
# showmorecomments_link.click()
# sleep(3)

# sleep(randint(4,6))
# browser.close()