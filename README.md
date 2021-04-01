# Scholarship project. Sport part
## Heroku-service
* https://young-basin-37598.herokuapp.com

## Ngrok-service
* http://0be750be2a83.ngrok.io

## API Endpoints
###  Events
* **api/sport/\*event_type\*/** - [GET, POST] - получение всех обьектов модели/добавление обьекта
* **api/sports/\*event_type\*/id/** [PATCH, GET, DELETE] - редактирование, получение по id, удаление по id

>GET response - object or list of objects  
POST response - added object  
PATCH response - modified object  
DELETE response - None

### Event types
* #### global_event - Приложение №5, таблица 1
> * name - [String] - название мероприятия  
> * level - [String] - уровень мероприятия (международное, всеросийское, ведомственное, региональное)  
> * degree - [String] - степень участия (индивидуальное, командное)
> * place - [Integer] - занятое место
> * date - [DateTime] - дата мероприятия (дд.мм.гггг)
> * points - [Integer] - количество очков за мероприятие

URL: https://young-basin-37598.herokuapp.com/api/sport/global_event/

* #### trp - Приложение №5, таблица 2
> * trp_badge - [Boolean] - наличие золотого знака ГТО
> * date - [DateTime] - дата мероприятия (дд.мм.гггг)
> * age_group - [Integer] - возраcтная группа [1..11]
> * points - [Integer] - количество очков за мероприятие 

URL: https://young-basin-37598.herokuapp.com/api/sport/trp/

* #### national - Приложение №5, таблица 3.1 
> * name - [String] - название мероприятия   
> * degree - [String] - степень участия (индивидуальное, командное)
> * place - [Integer] - занятое место
> * date - [DateTime] - дата мероприятия (дд.мм.гггг)
> * points - [Integer] - количество очков за мероприятие

URL: https://young-basin-37598.herokuapp.com/api/sport/national/

* #### not_national - Приложение №5, таблица 3.2
> * name - [String] - название мероприятия  
> * level - [String] - уровень мероприятия (международное, всеросийское, ведомственное, региональное)  
> * degree - [String] - степень участия (индивидуальное, командное)
> * place - [Integer] - занятое место
> * date - [DateTime] - дата мероприятия (дд.мм.гггг)
> * points - [Integer] - количество очков за мероприятие

URL: https://young-basin-37598.herokuapp.com/api/sport/not_national/

* #### online_event - Приложение №5, таблица 3.3
> * name - [String] - название мероприятия  
> * date - [DateTime] - дата мероприятия (дд.мм.гггг)
> * points - [Integer] - количество очков за мероприятие
 
URL: https://young-basin-37598.herokuapp.com/api/sport/online_event/

## Launch
### Installing dependencies
    pip install -r requirements.txt
### Database configuration
    Coming soon
### Running application
    python manage.py runserver <port>


### Описание функционала сервиса ###

Сервис принимает данные от пользователя, связанные с его спортивными достижениями в формате json и вносит в базу данных заявок. Информация обрабатывается в соответсвие с пунктами из Приложения5 и вносится в соответствующие базы данных. Связь между базами будет осуществляться через присвоение уникального id каждому пользователю во внутренней архитектуре сервиса. После этого заявка становится в статус "неподтвержденной" (скорее всего для этого будет создана бд с полями: id, фио, статус заявки) до проверки и выставления баллов за все достижения ответственными лицами. После прохождения всех проверок и выставления баллов заявка принимает статсу "подтверждена", по id со всех бд стаскиваются данные для генерации нужного пакета документов.

### Используемые технологии 

* Django REST 
* PostgreSQL
* Heroku

