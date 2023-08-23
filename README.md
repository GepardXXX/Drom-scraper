# Drom Parser

[![GitHub license](https://img.shields.io/github/license/GepardXXX/Drom-scraper)](https://github.com/GepardXXX/Drom-scraper/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100)
![GitHub last commit](https://img.shields.io/github/last-commit/GepardXXX/Drom-scraper)
![GitHub repo size](https://img.shields.io/github/repo-size/GepardXXX/Drom-scraper)
![GitHub watchers](https://img.shields.io/github/watchers/GepardXXX/Drom-scraper?style=social)
![GitHub stars](https://img.shields.io/github/stars/GepardXXX/Drom-scraper?style=social)

Проект Drom Parser представляет собой парсер для сбора информации о продаже автомобилей на [drom.ru](https://drom.ru).

## Описание

Данный парсер собирает информацию о продаже автомобилей с сайта Drom в заданном диапазоне параметров. Он обходит страницы с объявлениями, извлекает данные о марке, годе, двигателе, мощности, цене и URL-ссылке на объявление. Собранные данные сохраняются в формате Excel для дальнейшего анализа.

## Требования

Для запуска парсера необходимо иметь установленный Python и следующие библиотеки:
- `requests`
- `pandas`
- `beautifulsoup4`

## Структура проекта
```css
drom-parser/
├── parsers/
│ └── scraper.py
├── README.md
├──LICENSE
├── requirements.txt
```
- `scraper.py`: Файл с кодом для парсинга данных с сайта Drom.
- `README.md`: Файл, содержащий описание проекта, инструкции по использованию и связи.
- `LICENSE`: Файл с лицензией, определяющей условия распространения и использования вашего кода.
- `requirements.txt`: Файл, содержащий список библиотек и их версий, необходимых для работы парсера.
## Использование

1. Установите зависимости, указанные в `requirements.txt`, с помощью команды:
```
pip install -r requirements.txt
```
2. Отредактируйте файл `scraper.py`, укажите URL с параметрами поиска, которые вам необходимы.

3. Запустите парсер, выполните команду:
```
python scraper.py
```
4. После завершения работы парсера, результаты будут сохранены в файле `data.xlsx`.

## Связь

В случае вопросов или предложений, вы можете связаться со мной через [__GitHub__](https://github.com/GepardXXX) или [__Telegram__](https://t.me/GepardXXX).