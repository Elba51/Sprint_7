#done
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# инициализируем драйвер браузера
driver = webdriver.Chrome()
current_url = 'https://stellarburgers.nomoreparties.site/login'
current_url_profile = 'https://stellarburgers.nomoreparties.site/account/profile'

#вход по кнопке «Войти в аккаунт» на главной
driver.get('https://stellarburgers.nomoreparties.site/')
driver.find_element(By.XPATH, "//div/header/nav/a").click()
time.sleep(5)
driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys("Elenabasova4123@yandex.ru")
driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys("sport1234")
driver.find_element(By.XPATH, "//div/form/button").click()
time.sleep(5)
assert current_url_profile
driver.quite()

#вход через кнопку «Личный кабинет»
driver.get('https://stellarburgers.nomoreparties.site/')
driver.find_element(By.XPATH, "//div/main/section[2]/div/button").click()
time.sleep(5)
driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys("Elenabasova4123@yandex.ru")
driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys("sport1234")
driver.find_element(By.XPATH, "//div/form/button").click()
time.sleep(5)
assert current_url_profile
driver.quite()

#вход через кнопку в форме регистрации
driver.get('https://stellarburgers.nomoreparties.site/register')
driver.find_element(By.XPATH, "//div/div/p/a").click()
time.sleep(5)
driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys("Elenabasova4123@yandex.ru")
driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys("sport1234")
driver.find_element(By.XPATH, "//div/form/button").click()
time.sleep(5)
assert current_url_profile
driver.quite()

# вход через кнопку в форме восстановления пароля
driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
driver.find_element(By.XPATH, "//div/div/p/a").click()
time.sleep(5)
driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys("Elenabasova4123@yandex.ru")
driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys("sport1234")
driver.find_element(By.XPATH, "//div/form/button").click()
time.sleep(5)
assert current_url_profile
driver.quit()
