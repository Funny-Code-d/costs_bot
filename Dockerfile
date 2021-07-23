FROM python:3.9

RUN mkdir -p /Telegram_bot/

WORKDIR /Telegram_bot/

COPY . /Telegram_bot/

RUN pip install aiogram asyncio psycopg2

CMD ["python3", "app.py"]