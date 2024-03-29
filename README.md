# Scholarship project. Sport part

[![Python sport application](https://github.com/IVBO-07-19/scholarship-sport-part/actions/workflows/python-app.yml/badge.svg)](https://github.com/IVBO-07-19/scholarship-sport-part/actions/workflows/python-app.yml)

## Heroku-service
* https://young-basin-37598.herokuapp.com

## API Endpoints

![Models](https://github.com/IVBO-07-19/scholarship-sport-part/blob/main/DB_scheme.png?raw=true)

###  Events
* **api/sport/\*event_type\*/** - [GET, POST] - получение всех обьектов модели/добавление обьекта
* **api/sports/\*event_type\*/id/** [PATCH, GET, DELETE] - редактирование, получение по id, удаление по id

>GET response - object or list of objects  
POST response - added object  
PATCH response - modified object  
DELETE response - None

### Event types
* #### global_event - Приложение №5, таблица 1
> * userID - [String] - идентификатор пользователя
> * name - [String] - название мероприятия  
> * level - [String] - уровень мероприятия (международное, всеросийское, ведомственное, региональное)  
> * degree - [String] - степень участия (индивидуальное, командное)
> * place - [Integer] - занятое место
> * date - [DateTime] - дата мероприятия (гггг-мм-дд)
> * points - [Integer] - количество очков за мероприятие

URL: https://young-basin-37598.herokuapp.com/api/sport/global_event/

* #### trp - Приложение №5, таблица 2
> * userID - [String] - идентификатор пользователя
> * trp_badge - [Boolean] - наличие золотого знака ГТО
> * date - [DateTime] - дата мероприятия (дд.мм.гггг)
> * age_group - [Integer] - возраcтная группа [1..11]
> * points - [Integer] - количество очков за мероприятие 

URL: https://young-basin-37598.herokuapp.com/api/sport/trp/

* #### national - Приложение №5, таблица 3.1 
> * userID - [String] - идентификатор пользователя
> * name - [String] - название мероприятия   
> * degree - [String] - степень участия (индивидуальное, командное)
> * place - [Integer] - занятое место
> * date - [DateTime] - дата мероприятия (гггг-мм-дд)
> * points - [Integer] - количество очков за мероприятие

URL: https://young-basin-37598.herokuapp.com/api/sport/national/

* #### not_national - Приложение №5, таблица 3.2
> * userID - [String] - идентификатор пользователя
> * name - [String] - название мероприятия  
> * level - [String] - уровень мероприятия (международное, всеросийское, ведомственное, региональное)  
> * degree - [String] - степень участия (индивидуальное, командное)
> * place - [Integer] - занятое место
> * date - [DateTime] - дата мероприятия (гггг-мм-дд)
> * points - [Integer] - количество очков за мероприятие

URL: https://young-basin-37598.herokuapp.com/api/sport/not_national/

* #### online_event - Приложение №5, таблица 3.3
> * userID - [String] - идентификатор пользователя
> * name - [String] - название мероприятия  
> * date - [DateTime] - дата мероприятия (гггг-мм-дд)
> * points - [Integer] - количество очков за мероприятие
 
URL: https://young-basin-37598.herokuapp.com/api/sport/online_event/

## Launch
###  Installing dependencies
    pip install -r requirements.txt
###  Install PostgreSQL
### Create Postgres database
* #### Coming soon
### Configure application
    set JWT_AUDIENCE=<your_jwt_audience>
    set JWT_ISSUER=<your_jwt_issuer>
   
    set DATABASE_URL=<your_database_url>
Example:  

    set DATABASE_URL=postgres://<username>:<password>@localhost:5432/<database_name>

#### Running application
    python manage.py runserver <port>


### Описание функционала сервиса ###

Сервис принимает данные от пользователя, связанные с его спортивными достижениями в формате json и вносит в базу данных заявок. Информация обрабатывается в соответсвие с пунктами из Приложения5 и вносится в соответствующие базы данных. Связь между базами будет осуществляться через присвоение уникального id каждому пользователю во внутренней архитектуре сервиса. После этого заявка становится в статус "неподтвержденной" (скорее всего для этого будет создана бд с полями: id, фио, статус заявки) до проверки и выставления баллов за все достижения ответственными лицами. После прохождения всех проверок и выставления баллов заявка принимает статсу "подтверждена", по id со всех бд стаскиваются данные для генерации нужного пакета документов.

### Используемые технологии 

* Django REST 
* PostgreSQL
* Heroku
* Auth0
* JWT

