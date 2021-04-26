#Добавление комментария
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
#Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
#Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
selen_ruby = driver.find_element_by_css_selector("a.woocommerce-LoopProduct-link").click()
#Нажмите на вкладку "REVIEWS"
reviews = driver.find_element_by_css_selector(".reviews_tab >a").click()#поиск по ссылке не сработал почему-то (элемент не был найден)
#Поставьте 5 звёзд
stars = driver.find_element_by_css_selector("p.stars").click()
star_5 = driver.find_element_by_css_selector("a.star-5").click()
#Заполните поле "Review" сообщением: "Nice book!"
rew_comment = driver.find_element_by_id("comment").send_keys("Nice book!")
#Заполните поле "Name"
name = driver.find_element_by_id("author").send_keys("Natasha")
#Заполните "Email"
email = driver.find_element_by_id("email").send_keys("nikolaeva@mail.ru")
#Нажмите на кнопку "SUBMIT"
submit = driver.find_element_by_id("submit").click()
driver.quit()




