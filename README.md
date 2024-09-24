# TgMessageScheduler
Автоматическое добавление сообщений в очередь для запланированной отправки Telegram

## Настройка

> Вся настройка производится в файле `config.py`

- **API_ID / API_HASH** — Данные API Telegram для авторизации
- **CHAT_ID** — ID чата, куда будут отправляться сообщения
- **SEND_DELAY** — Задержка между отправками сообщений в секундах
- **SEND_OFFSET** — Смещение времени отправки. Например, если указать `86400`, сообщения будут отправлены на день позже
- **SEND_MESSAGE** — Текст сообщения для отправки
- **MESSAGES_NUM** — Количество сообщений для отправки (максимум 100)
- **MAX_WORKERS** — Количество потоков, используемых для отправки сообщений

---

## Установка

```sh
~ > git clone https://github.com/xysed/TgMessageScheduler.git 
~ > cd TgMessageScheduler

# Linux
~/TgMessageScheduler > python3 -m venv venv
~/TgMessageScheduler > source venv/bin/activate
~/TgMessageScheduler > pip3 install -r requirements.txt
~/TgMessageScheduler > nano config.py  # Укажите ваши API_ID и API_HASH
~/TgMessageScheduler > python3 main.py

# Windows
~/TgMessageScheduler > python -m venv venv
~/TgMessageScheduler > venv\Scripts\activate
~/TgMessageScheduler > pip install -r requirements.txt
~/TgMessageScheduler > # Откройте файл config.py и укажите ваши API_ID и API_HASH
~/TgMessageScheduler > python main.py
```