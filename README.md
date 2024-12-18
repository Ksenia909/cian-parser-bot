# Телеграм-бот для поиска квартир на Cian.ru
В этом проекте реализован Telegram-бот, который помогает пользователям искать квартиры на [cian.ru](https://www.cian.ru/). Бот предоставляет удобный интерфейс для настройки параметров поиска, таких как линии и станции метро, время до метро, количество комнат и диапазон цен. После настройки бот формирует URL для поиска и отправляет пользователю новые объявления с заданной периодичностью. Бот использует асинхронное программирование и интеграцию с Redis и PostgreSQL для быстрого и надежного взаимодействия с пользователем.

---

## Оглавление

- [Функциональность](#функциональность)
- [Используемые технологии](#используемые-технологии)
- [Инструкция по установке](#инструкция-по-установке)
- [Как работает бот](#как-работает-бот)
- [Пример](#пример)
- [Лицензия](#лицензия)

---

## Функциональность

- **Интерактивные диалоги**  
  Пользователь настраивает параметры поиска через пошаговое меню:
  - Выбор линий и станций метро.
  - Указание времени в пути до метро.
  - Выбор количества комнат (например, 1-комнатные, 2-комнатные и т.д.).
  - Указание диапазона цен.
  
- **Автоматические обновления**  
  После завершения настройки бот:
  - Немедленно отправляет результаты текущего поиска.
  - С интервалом в 10 минут проверяет новые объявления и отправляет пользователю.

- **Хранение данных**  
  Настройки пользователя и поисковые параметры сохраняются в базе данных PostgreSQL, чтобы обеспечить непрерывность работы.

---

## Используемые технологии

### Основные библиотеки и фреймворки:
- **Aiogram**: Фреймворк для создания Телеграм-ботов.
- **Aiogram-Dialog**: Для создания диалоговых окон и работы с конечными автоматами (FSM).
- **APScheduler**: Планирование и выполнение периодических задач.

### База данных:
- **PostgreSQL**: Реляционная база данных для хранения информации о пользователях и их запросах.
- **SQLAlchemy**: ORM для удобного взаимодействия с базой данных.

### Веб-парсинг и работа с HTTP:
- **BeautifulSoup**: Для парсинга HTML и извлечения данных с веб-страниц.
- **Fake-UserAgent**: Для генерации случайных user-agent и маскировки запросов.
- **HTTPX**: Библиотека для выполнения асинхронных HTTP-запросов.
- **Aiohttp**: Асинхронная работа с HTTP на более низком уровне.

### Хранение и кэширование данных:
- **Redis**: Используется для временного хранения данных, работы с задачами и кэшированием.

### Управление конфигурацией:
- **Environs**: Удобная работа с переменными окружения.
- **Python-dotenv**: Загрузка переменных окружения из файла `.env`.

### Контейнеризация:
- **Docker**: Для развёртывания PostgreSQL, Redis и обеспечения изоляции окружения.
---

## Инструкция по установке

### Требования:
1. **Python 3.10+**
2. **Docker и Docker Compose**
3. Токен Телеграм-бота от BotFather.


1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Ksenia909/cian-parser-bot.git
   
2. Перейдите в директорию проекта:
   ```bash
   cd cian-parser-bot
   
3. Установите виртуальное окружение:
   ```bash
   python3 -m venv env
   source env/bin/activate  # для Unix
   .\env\Scripts\activate   # для Windows
   
4. Установите зависимости:
   ```bash
   pip install -r requirements.txt

5. Настройте прокси-серверы: В проекте используется файл proxy_config.py для хранения списка прокси, которые в свою очередь используются при парсинге данных с сайта. Для корректной работы замените содержимое файла proxy_config.py на свои данные. Пример структуры файла:
   ```bash
   proxy_list = [
    "http://username:password@proxy1.com:port",
    "http://username:password@proxy2.com:port",
    "http://username:password@proxy3.com:port"
   ]

6. Создайте файл .env и docker-compose.yml с помощью .env.example и docker-compose.example.yml соответственно. 

7. Запустите PostgreSQL и Redis через Docker:
   ```bash
   docker-compose up -d
   
8. Запустите бота:
   ```bash
   python bot.py
   
Не забудьте запустить docker.

---

## Как работает бот

### Основные этапы:

1. **Интерактив с пользователем**  
   Бот приветствует пользователя и предлагает настроить параметры поиска через диалоги.

2. **Сбор данных**  
   Введённые параметры (метро, цена, комнаты и т.д.) сохраняются в базе данных.

3. **Формирование ссылки**  
   Генерация URL для поиска осуществляется с помощью специального класса `URLBuilder`.

4. **Парсинг данных**  
   Бот запрашивает данные с сайта Cian.ru и отправляет пользователю.

5. **Автоматическое обновление**  
   Бот каждые 10 минут проверяет наличие новых объявлений и отправляет только уникальные записи.

---

## Пример

<img src="bot.gif" width="300px" />

---

## Лицензия
Этот проект распространяется под лицензией MIT. Подробности в LICENSE.