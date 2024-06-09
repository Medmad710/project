from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройки для работы с headless режимом (без открытия окна браузера)
def PriceFindWB(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Инициализация драйвера
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # URL товара на Wildberries


    # Переход на страницу
    driver.get(url)

    # Ожидание загрузки страницы и цены товара
    time.sleep(10)  

    try:
        # Поиск элемента с ценой
        price_element = driver.find_element(By.CLASS_NAME, "price-block__final-price")
        price = price_element.text
        return price
    except Exception as e:
        return -1

    # Закрытие драйвера
    driver.quit()
