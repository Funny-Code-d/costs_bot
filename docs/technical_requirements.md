# 1. Цель проекта

Цель проекта - разработать систему контроля личных расходов (далее Система). Пользователь сможет настравиать свои категории покупок добавлять покупки в систему, как вручную так и отскаировав Qr код чека или передав данные чека. Получать сводку о затратах, и настраивать свои шаблоны для получения сводки (выбор категорий, количество дней). Вести свою долговую книжку: записывать и отслеживать кто или кому сколько должен. К записи в долговой книжке можно будет привязать другого пользователя, который будет получать уведомления об изменениях. Разработать функционал на базе API банка Тинкофф, для получения подробной информации об инвестиционном счете.

Взаимодействие с системой будет осуществлятся по API.

Взаимодействие пользователя в рамках проекта будет осуществеленно с помощью Telegram бота. В дальнейшем если проект будет успешным, планируется разработать мобильное приложение и сайт и расширить функционал.
***
# 2. Описание системы
Система состоит из следующих основноых функциональных блоков

1. Регистрация и настройка пользователя
2. Добавление и удаление покупок
3. Стандартных вывод покупок (день, неделя, месяц, год)
4. Настрока шаблонов для вывода покупок (выбор категорий, количество дней)
5. Долговая книжка
6. Категории покупок


## 2.1 Регистрация

При регистрации нового пользователя в формате json передаются данные пользователя:

* Имя
* Фамилия
* Платформа (telegram, mobile)
* ID (в случае если используемая платформа - telegram)
* Email (в случае если платформа - mobile)

В системе присваивается уникальный ID пользователю и отсылается обратно


*Регистрация пользователя*
**POST funny-code.ru/api/{token}/v1/user/**


*Получение информации о пользователе*
**GET funny-code.ru/api/{token}/v1/user/settings/**


*Изменение информации о пользователе*
**PUT/PATCH funny-code.ru/api/{token}/v1/user/settings/**


## 2.2 Добавление и удаление покупок

В данном функционале 2 варианта:
1. Пользователь добавляет покупку вручную


    *Добавление покупок*
    **POST funny-code.ru/api/{token}/v1/user/purchase/**
    ```
    {
        "user_id" : 123,
        "amount" : 80,
        "category" : "Продукты",
        "items" : {
            {
                "description" : "Картофель",
                "amount" : 50
            },
            {
                "description" : "Морковь",
                "amount" : 30
            }
        }
    }
    ```

2. Пользователь фотографирует QR-код или передаёт данные чека


    *Добавление покупок*
    **POST funny-code.ru/api/{token}/v1/user/purchase**
    ```
    {
        "user_id" : 123,
        "data" :{
            "данные чека"
        }
    }
    ```

**Инфомация о покупках будет браться по открытому API ФНС**


> На какой стороне будет реализована расшифровка QR-кода ещё не решил:
> * На стороне клиента (telegram бот или mobile)
> * Передача картинки на сервер и расшифровка на стороне API


## 2.3 Категории покупок

Данный блок реализует управление категориями покупок

* Создание новых категорий
* Удаление категорий
* Изменение категорий

*Создание категории*
**POST funny-code.ru/api/{token}/v1/user/purchase/category/**

*Получение категорий пользователя*
**GET funny-code.ru/api/{token}/v1/user/purchase/category/**
```
{
    "user_id" : 123,
    "items" : {
        {
            "category_id" : 1,
            "category_name" : "Продукты"
        },
        {
            "category_id" : 2,
            "category_name" : "Питание на работе"
        },
        {
            "category_id" : 3,
            "category_name" : "Проезд"
        }
    }
}
```

*Удаление категории пользователя*
**DELETE funny-code.ru/api/{token}/v1/user/purchase/category/**
```
{
    "user_id" : 123,
    "category_id" : 1
}
```

*Изменение категории*
**UPDATE funny-code.ru/api/{token}/v1/user/purchase/category/**
```
{
    "user_id" : 123,
    "category_id" : 1,
    "new_name_category" : "Развлечения"
}
```




## 2.4 Стандартный вывод покупок


Стандартный вывод покупок предусматривает 4 типа:

1. Вывод покупок за сегодня
2. Вывод покупок за неделю
3. Вывод покупок за месяц
4. Вывод покупок за год

*Сегодня*
**GET funny-code.ru/api/{token}/v1/user/purchase/output/today/**

*Неделя*
**GET funny-code.ru/api/{token}/v1/user/purchase/output/week/**

*Месяц*
**GET funny-code.ru/api/{token}/v1/user/purchase/output/month/**

*Год*
**GET funny-code.ru/api/{token}/v1/user/purchase/output/year/**

```
{
    "user_id" : 123,
}
```


## 2.5 Настрока шаблонов покупок

Данный блок будет реализовывать создание шаблонов для получения покупок по критериям. Пользователь при создании выбирает категории которые будут входить в шаблон и количество дней (за какой период от текущей даты получить покупки). Для удобства каждому шаблону пользователь присваивает название.

*Получение всех шаблонов*
**GET funny-code.ru/api/{token}/v1/user/purchase/templates/**

*Получение конкретного шаблона*
**GET funny-code.ru/api/{token}/v1/user/purchase/templates/{templates_id}/**

*Создание нового шаблона*
**POST funny-code.ru/api/{token}/v1/user/purchase/templates/**

```
{
    "user_id" : 123,
    "categories" : items {
        {
            "name_category" : "Продукты"
        },
        {
            "name_category" : "Питание на работе"
        },
        {
            "name_category" : "Проезд"
        }
    },
    
    "number_days" : 14
}
```
## 2.6 Долговая книжка

Данный блок реализует функционал конроля задолжностей:

* Добавление новой записи (заёмщик)
* Привязка другого пользователя к записи в книжке, для отправки уведомлений об изменении суммы
* Запись задолжностей пользователя (дал, взял)
* Получение текущих задолжностей
* Получение истории задолжности по конкретной записи в книжке


*Создание новой записи в книжке*
**POST funny-code.ru/api/{token}/v1/user/debtbook/**
```
{
    "user_id" : 123,
    "name_debtor" : "Ivan"
}
```

*Получение информации о текущих задолжностях*
**GET funny-code.ru/api/{token}/v1/user/debtbook/**

*Изменение задолжности по конкретной записи в книжке*
**UPDATE funny-code.ru/api/{token}/v1/user/debtbook/**
```
{
    "user_id" : 123,
    "name_debtor" : "Ivan",
    "action" : "take"/"give",
    "amount" : 1000
}
```

*Получение истории изменения записи в книжке*
**GET funny-code.ru/api/{token}/v1/user/debtbook/history/**
```
{
    "user_id" : 123,
    "name_debtor" : "Ivan",
    "action" : "take"/"give",
    "range_days" : 10
}
```


***

# Предлагаемый стек технологий

* API
    - Язык программирования Python
    - Фреймворк FastAPI
    - БД PostgreSQL
    - SQLAlchemy ORM
    - docker-compose

* Telegram бот
    - Язык программирования Python
    - Фреймворк Aiogram
    - БД PostgreSQL
    - docker-compose
    - docker






























