import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.implicitly_wait(2)
browser.get("https://casenik.com.ua/user/login")

email_field = browser.find_element(By.XPATH, "//input[@id='email']")
email_field.send_keys("tdv@mail.com")
password_field = browser.find_element(By.XPATH, "//input[@id='pasword']")
password_field.send_keys("87654321")
login_button = browser.find_element(By.XPATH, "//button[@class='btn button-gen']").click()

time.sleep(5)

message = WebDriverWait(browser, 27).until_not( # Явне очікування. Чекаємо упродовж 27 сек. поки елемент не зникне. Якщо просто until - то чекаємо поки елемент не з'явиться.
    #EC.element_to_be_clickable((By.XPATH, "//div[@class='alert alert-success']"))
    EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success']")) # Вы успешно авторизованы
)


# message2 = WebDriverWait(browser, 32).until_not(
#         #EC.element_to_be_clickable((By.XPATH, "//div[@class = 'alert alert-success']"))
#         EC.visibility_of_element_located((By.XPATH, "//div[@class = 'alert alert-success']"))
#     )






