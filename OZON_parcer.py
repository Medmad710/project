import requests
from bs4 import BeautifulSoup

def PriceFindOZON(url):
    try:
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        name = soup.find('div', class_='b2').find(
            'div', class_='container b6').find("h1", class_="mn3_27 tsHeadline550Medium").text.strip()
        price = soup.find('div', class_='b2').find(
            'div', class_='container b6').find("span", class_="mm4_27 m4m_27 mn1_27").text.strip()
        return [name, price]
    except:
        return -1