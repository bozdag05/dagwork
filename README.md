Я основы Markdown не знаю, поэтому красиво оформить не получиться.
Но пока я буду учить его напишу как смогу 

**Время которое ушло на создание данного проекта примерно ~ 12ч**

Ссылка на 4 минутное видео с показом функционала сайта - https://drive.google.com/file/d/1Ur-RkvG9KRHs8ucE9hLoXnONh9CRH--0/view?usp=drive_link

1. Проект называется dagwork. приложенее dagfreelance
  dagfreelance, является сайтом, где представленны учётные записи заказчиков, и исполнителей

2. У данного приложения есть следующие возможности:
  - Админка
  - Регистразция/Авторизация
  - Редактирования профия
  - Страницы с списками заказчиков и исполнителй
  - Представление определённой записи

**ИНСТРУКЦИЯ ПО УСТАНОВКЕ И ПОДКЛЮЧЕНИЮ**

1. Загрузите проект к себе на локальноую машину
2. Установите все нужные библиотеки, указанные в `requirements.txt`, для этого можете использовать команду В терминале `pip install -r requirements.txt`
3. Создайте файл .env (на уровне с `manage.py`) и укажите там следующие **СВОИ** параметры
   - SECRET_KEY=Свой ключ (возможно мне придётся свой отдавать, чтобы вы могли проверить)
      
   PostgreSQL (эту строку не пишем)
   - NAME=Имя БД
   - USER=Имя пользователя
   - PASSWORD=Пароль

4. Запустите сайт спомощью команды `python manage.py runserver`
5. Создайте супер юзера `python manage.py createsuperuser`
6. Заполните БД нужными данными и можете проверять что хотите

**ПРИМЕЧАНИЕ:**
  1. Через суперпользователя не получиться зарегаться заказчиком или исполнителём, для этого создайте новых пользователей, чтобы суперпользователь стал заказчиком, или     исполнителем, нужно его привязть через Админку
  2. Один и тот же пользователь не может быть и заказчиком и исполнителем, так как я создал связь Один-к-Одному в модели
