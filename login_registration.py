#РЕГИСТРАЦИЯ АККАУНТА
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
#Нажмите на вкладку "My Account Menu"
my_account = driver.find_element_by_link_text("My Account").click()
#В разделе "Register", введите email для регистрации
email = driver.find_element_by_id("reg_email").send_keys("natrom434@mail.ru")
#В разделе "Register", введите пароль для регистрации
password = driver.find_element_by_id('reg_password').send_keys("Megi13nik#$")
#Нажмите на кнопку "Register"
register = driver.find_element_by_name("register").click()
driver.quit()

#ЛОГИН В СИСТЕМУ
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
#Нажмите на вкладку "My Account Menu"
my_account = driver.find_element_by_link_text("My Account").click()
#В разделе "Login", введите email для логина
email_log = driver.find_element_by_id("username").send_keys("natrom434@mail.ru")
#В разделе "Login", введите пароль для логина
password_log = driver.find_element_by_id("password").send_keys("Megi13nik#$")
#Нажмите на кнопку "Login"
login_btn = driver.find_element_by_name("login").click()
#Добавьте проверку, что на странице есть элемент "Logout"
element_logout = driver.find_element_by_link_text("Logout")
element_get_text = element_logout.text
assert element_get_text == "Logout"
driver.quit()
