#Отображение страницы товара
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
shop = driver.find_element_by_link_text("Shop").click()
#Откройте книгу "HTML 5 Forms"
html_5 = driver.find_element_by_xpath("//a[@data-product_id='181']").click()
#Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
h1_html_5 = driver.find_element_by_css_selector(".product_title.entry-title")
h1_html_5_get_text = h1_html_5.text
assert h1_html_5_get_text == "HTML5 Forms"
driver.quit()

#Количество товаров в категории
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
shop = driver.find_element_by_link_text("Shop").click()
#Откройте категорию "HTML"
html = driver.find_element_by_css_selector(".cat-item.cat-item-19>a").click()
#Добавьте тест, что отображается три товара
items_count = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
if len(items_count) == 3:
    print("На странице 3 товара")
else:
    print("Ошибка. Количество товаров на странице: " + str(len(items_count)))
driver.quit()

#сортировка товаров
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
shop = driver.find_element_by_link_text("Shop").click()
#Отсортируйте товары от большего к меньшему (используйте селект)
from selenium.webdriver.support.select import Select
selector = driver.find_element_by_class_name("orderby")
select = Select(selector)
select.select_by_value("price-desc")
#Добавьте тест, что в селекторе выбран вариант сортировки от большего к меньшему (проверка по value)
select_value = driver.find_element_by_class_name("orderby")
select_value_check = select_value.get_attribute("value")
if select_value_check == "price-desc":
	print("Сортировка от большего к меньшему")
else:
	print("Другой вариант сортировки")
#Снова объявите переменную с локатором основного селектора сортировки
selector = driver.find_element_by_class_name("orderby")
select = Select(selector) # Select после "=" должен быть с большой буквы, так как в import он указан с большой буквы
select.select_by_value("menu_order")
# Добавьте тест, что выбран основной селектор сортировки "По умолчанию"
select_value = driver.find_element_by_class_name("orderby")
select_value_check = select_value.get_attribute("value")
if select_value_check == "menu_order":
	print("По умолчанию")
else:
	print("Другой вариант сортировки")
driver.quit()


#Отображение, скидка товара
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
shop = driver.find_element_by_link_text("Shop").click()
#Откройте книгу "Android Quick Start Guide"
android_book = driver.find_element_by_class_name("post-169.product").click()
#Добавьте тест, что содержимое старой цены = "₹600.00"	# используйте assert
price_600 = driver.find_element_by_css_selector("p.price >del>.woocommerce-Price-amount")
price_600_get_text = price_600.text
assert "₹600" in price_600_get_text
#Добавьте тест, что содержимое новой цены = "₹450.00"
price_450 = driver.find_element_by_css_selector("ins>.woocommerce-Price-amount")
price_450_get_text = price_450.text
assert "₹450.00" in price_450_get_text
#Добавьте явное ожидание и нажмите на обложку книги
#Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
android_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-main-image.zoom")) )
android_btn.click()
#Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
close_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.pp_close")) )
close_btn.click()
driver.quit()

#Проверка цены в корзине
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
#Нажмите на вкладку "Shop"
shop = driver.find_element_by_link_text("Shop").click()
#Добавьте в корзину книгу "HTML5 WebApp Development"(добавить нельзя, так как ее нет в наличии,добавила "Освоение Javascript"
Java = driver.find_element_by_css_selector("[data-product_id='165']").click()
#Добавьте тест, что в возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹350.00"
#Используйте для проверки assert
import time
time.sleep(3)
cart_price = driver.find_element_by_css_selector("span.amount")
time.sleep(3)
cart_price_get_text = cart_price.text
assert cart_price_get_text == "₹350.00"
time.sleep(3)
item = driver.find_element_by_class_name("cartcontents")
time.sleep(3)
item_get_text = item.text
assert item_get_text == "1 Item"
# Перейдите в корзину
basket = driver.find_element_by_css_selector("a.wpmenucart-contents").click()
# Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
subtotal = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "td>span.woocommerce-Price-amount"), "₹350.00"))
#Используя явное ожидание, проверьте что в Total отобразилась стоимость
total = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "strong>.woocommerce-Price-amount"), "₹367.50"))
driver.quit()


#Работа в корзине
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
#Нажмите на вкладку "Shop"
shop = driver.find_element_by_link_text("Shop").click()
#Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# (добавить эти книги нельзя, их нет в наличии, на сайте можно добавить только одну книгу в корзину "Mastering JavaScript")
#-Перед добавлением первой книги, проскролльте вниз на 300 пикселей
#-После добавления 1-й книги добавьте sleep
driver.execute_script("window.scrollBy(0, 300);")
Java = driver.find_element_by_css_selector("[data-product_id='165']").click()
import time
time.sleep(3)
#Перейдите в корзину
basket =driver.find_element_by_class_name("wpmenucart-contents").click()
#Удалите первую книгу
#-Перед удалением добавьте sleep
time.sleep(3)
book_del = driver.find_element_by_css_selector(".product-remove>a.remove").click()
#Нажмите на Undo (отмена удаления)
undo_book_del = driver.find_element_by_link_text("Undo?").click()
#В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
#возможно только для книги "Mastering JavaScript"
quantity = driver.find_element_by_css_selector(".quantity > input")
quantity.clear()
quantity.send_keys("3")
#Нажмите на кнопку "UPDATE BASKET"
update_basket = driver.find_element_by_css_selector("[value='Update Basket']").click()
#Добавьте тест, что value элемента quantity для "Mastering JavaScript" равно 3
# используйте assert
quantity = driver.find_element_by_css_selector(".quantity > input")
quantity_value = quantity.get_attribute("value")
assert quantity_value =="3"
time.sleep(3)
#Нажмите на кнопку "APPLY COUPON"
apply_coupon = driver.find_element_by_css_selector("[value='Apply Coupon']").click()
#Добавьте тест, что возникло сообщение: "Please enter a coupon code."
modal_message = driver.find_element_by_css_selector(".woocommerce-error>li")
modal_message_text = modal_message.text
assert "Please enter a coupon code." in modal_message_text
driver.quit()


#Покупка товара (Тест осуществить невозможно, так как полностью отсутсвует товар на сайте и добавить в корзину ничего нельзя)