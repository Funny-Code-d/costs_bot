<h1 align="center">Бот для контроля расходов</h1>

### Для удобства проект разделён на пакеты

- [Модуль запуска бота](https://github.com/Funny-Code-d/costs_bot/blob/main/app.py)
- [Модуль с созданием всех объектов для работы](https://github.com/Funny-Code-d/costs_bot/blob/main/loader.py)
   - [Пакет с общими модулями](https://github.com/Funny-Code-d/costs_bot/tree/main/moduls)
      - [Модуль для создания клавиатуры бота](https://github.com/Funny-Code-d/costs_bot/blob/main/moduls/Keyboard_class.py)
      - [Модуль с классами машины состояний](https://github.com/Funny-Code-d/costs_bot/blob/main/moduls/Question.py)
      - [Модуль "Интерфейса" для работы с базой](https://github.com/Funny-Code-d/costs_bot/blob/main/moduls/expences.py)
      - [Модуль класса работы с базой](https://github.com/Funny-Code-d/costs_bot/blob/main/moduls/sql_class.py)
   - [Пакет с утилитами для бота](https://github.com/Funny-Code-d/costs_bot/tree/main/utils)
       - [Модуль для установки команд бота](https://github.com/Funny-Code-d/costs_bot/blob/main/utils/bot_commands.py)
   - [Пакет с хендлерами бота](https://github.com/Funny-Code-d/costs_bot/tree/main/handlers)
       - [Модуль с вызовом стартового меню бота](https://github.com/Funny-Code-d/costs_bot/blob/main/handlers/start_bot.py)
       - [Модуль для добавления покупок](https://github.com/Funny-Code-d/costs_bot/blob/main/handlers/adding_purchase.py)
       - [Модуль для удаления покупок](https://github.com/Funny-Code-d/costs_bot/blob/main/handlers/remove_purchase.py)
       - [Модуль для получения статистики покупок](https://github.com/Funny-Code-d/costs_bot/blob/main/handlers/output_statistics.py)
       - [Модуль с реализацией книжки задолжностей](https://github.com/Funny-Code-d/costs_bot/blob/main/handlers/deptor.py)
 ___
