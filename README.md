# Setup Django Project

1. создать виртуальное окружение 
`pyhton3 -m  venv venv`
2. актавировать виртуальное окружение
" .venv/bin/activate
3. создать файл requirements.txt
`touch requirement.txt`
4. записать зависимости
django
djangorestframework
psycopg2-binary
python-decouple
5.установить библиотеки
`pip install -r requirements.txt`
6. оазвернуть проект
`django-admin startproject todo`
7.создать базу данных для проета
`create <db_name>`
8. настроить базу данных в перменной DATABASES в файле settings.py
9. создать приложение 
`python3 manage.py startapp todo_app`
10. Зарегистрировать приложение/занести в список
INSTALLED_APPS в файле setting.py
11. Занести в INSTALLED_APPS rest_framework
12. создать миграции
`python3 manage.py makemigrations`
13. Применить миграции
`pyhton3 manage.py migrate`
14. Создать супе-пользователя
`python3 manage.py createsuperuser`
15. Запустить сервер
`python3 manage.py runserver [port]`

