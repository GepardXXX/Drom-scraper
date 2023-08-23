import requests
import re
import pandas as pd
from bs4 import BeautifulSoup as bs

def get_data(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }

    iterations = 9  # Количество итераций для перехода по страницам
    print(f'Всего итеграций: {iterations}')
    data = []  # Список для хранения данных о машинах

    # Цикл по итерациям
    for i in range(0, 10):
        # Замена номера страницы в URL для перехода на следующую страницу
        url = url.replace(f'page{i}', f'page{i+1}')
        req = requests.get(url, headers=headers)
        soup = bs(req.text, 'lxml')

        get_hrefs = soup.find_all('a', 'css-xb5nz8 e1huvdhj1')

         # Цикл по найденным ссылкам на объявления о продаже машин
        for href in get_hrefs:

            req = requests.get(href.get('href'))
            soup = bs(req.text, 'lxml')

            features = list(soup.find_all('td'))

            car_brand = soup.find('span', "css-1kb7l9z e162wx9x0").text
            car_brand = re.split('Продажа |, | в', car_brand)

            price = soup.find('div', 'css-eazmxc e162wx9x0').text

            power = features[1].text.split(',')

            # Добавление данных о машине в список
            data.append([car_brand[1], car_brand[2],
                        features[0].text, power[0], price, href.get('href')])

        if iterations == 0:
            print('Сбор данных завершён')
        else:
            print(f'Итерация {i+1} завершена. Осталось итераций: {iterations}')
            iterations -= 1

    # Создание DataFrame и сохранение в Excel-файл
    df = pd.DataFrame(
        data, columns=['Марка', 'Год', 'Двигатель', 'Мощность', 'Цена', 'URL-ссылка'])
    df.to_excel("parsers\drom\main\data.xlsx", index=False)


def main():
    get_data('https://rostov-na-donu.drom.ru/auto/all/page0/?maxprice=1500000&minyear=2007&maxyear=2023&fueltype=1')


if __name__ == '__main__':
    main()
