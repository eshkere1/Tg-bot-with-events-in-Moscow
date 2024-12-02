# Тг бот с мероприятиями в Москве


## Содержание

- [Описание](#описание)
- [Установка](#установка)
- [Использование](#использование)

## Описание

С помощью этого бота вы сможете узнать мероприятия на ближайшие 10 дней в Москве, а также погоду на эти дни.



## Установка
1. Установите python
    
    Python должен быть уже установлен. Если его нет, проследуйте инструкциям [статья по установке python](https://docs.python.org/3/using/windows.html) Python от Microsoft.
    
2. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/eshkere1/Tg-bot-with-events-in-Moscow.git
    ```

3. Перейдите в директорию проекта:

    ```bash
    cd путь к проекту
    ```

4. Создайте виртуальное окружение и активируйте его (опционально, но рекомендуется):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

5. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

6. Создайте файл .env и добавьте ваш токен Telegram Bot API:
    
    ```
    TG_BOT_TOKEN=ваш_токен
    ```
    Для того чтобы получить телеграмм токен вам нужно обратится к [BotFather](https://telegram.me/BotFather) в телеграмм

7. Запустите бота:

    ```bash
    python tg.py
    ```

## Использование

1. Добавьте бота в Telegram.
2. Воспользуйтесь командой /start для запуска.
