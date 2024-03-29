# API Yamdb

**For documentation in English, please refer to [README_EN.md](./README_EN.md).**

## Описание проекта
YaMDb - это проект, на котором люди могут оставлять отзывы о книгах, фильмах, музыке и других произведениях.  Произведения разделены на категории и им можно присвоить жанр. Администраторы могут добавлять новые произведения, категории и жанры. Пользователи могут оставлять свои отзывы и ставить оценки произведениям и комментировать отзывы других пользователей.
## Запуск проекта
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Belyanski/api_yamdb
```
```
cd api_yamdb
```
- Cоздать и активировать виртуальное окружение
```
python -m venv venv # Для Windows
python3 -m venv venv # Для Linux и macOS
```
```
source venv/Scripts/activate # Для Windows
source venv/bin/activate # Для Linux и macOS
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Перейти в папку со скриптом управления и выполнить миграции
```
cd api_yamdb
```
```
python manage.py migrate
```

- Запустить проект
```
python manage.py runserver
```
## Создание суперпользователя
- В директории с файлом manage.py выполнить команду
```
python manage.py createsuperuser
```
- Заполнить поля в терминале
```
Username: <ваше_имя>
Email address: <ваш_email>
Password: <ваш_пароль>
Password (again): <ваш_пароль>
```
## Регистрация нового пользователя
- Передать на эндпоинт ```127.0.0.1:8000/api/v1/auth/signup/``` **username** и **email**
- Получить код подтверждения на переданный **email**. Права доступа: Доступно без токена. Использовать имя 'me' в качестве **username** запрещено. Поля **email** и **username** должны быть уникальными. 

## Получение JWT-токена
- Передать на эндпоинт ```127.0.0.1:8000/api/v1/auth/token/``` **username** и **confirmation** code из письма. Права доступа: Доступно без токена.

## Примеры запросов

- Отправить POST-запрос на адрес ```http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/``` и передать поле ```text``` <br>
Пример запроса на создание комментария к отзыву:
```
{
"text": "Классный отзыв!"
}
```
Пример ответа:
```
{
"id": 0,
"text": "Классный отзыв!",
"author": "string",
"pub_date": "2019-08-24T14:15:22Z"
}
```

## Полная документация к API проекта:

Перечень запросов к ресурсу можно посмотреть в описании API

```
http://127.0.0.1:8000/redoc/
```

### Импорт данных из тестовых CSV файлов в базу:
Для импорта данных следует использовать команду ```importdata```.
```
python3 manage.py importdata
```

Команда импортирует данные из CSV файлов в таблицы базы данных с соответствующими именами.
CSV файлы должны быть размещены в папке  прописанной ```STATICFILES_DIRS``` во вложенной папке data.
Данные будут импортированы в дефолтную базу данных, указанную в настройках проекта как ```DATABASE['default']```.



### Techonologies: 

REST API, Viewsets, routers, JWT, serializers, permissions, limits, pagination, sorting, CSV, Django.

## Над проектом работали
* [Екатерина Додонова](https://github.com/dodonova)</br>
* [Алексей Котко](https://github.com/Zaphod999)</br>
* [Антон Ильичев](https://github.com/Antochino)</br>


