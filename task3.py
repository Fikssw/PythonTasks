import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('div', class_='quote')

    for i, quote in enumerate(quotes[:10]):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        print(f'{i+1}. {text} - {author}')
else:
    print(f'Не вдалося завантажити сторінку. Статус код: {response.status_code}')