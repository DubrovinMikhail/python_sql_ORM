 Домашнее задание к лекции «Python и БД. ORM»

## Задание 1

Составить модели классов SQLAlchemy по схеме:

![](book_publishers_scheme.png)

Интуитивно необходимо выбрать подходящие типы и связи полей.

## Задание 2

Используя SQLAlchemy, составить запрос выборки магазинов, продающих целевого издателя.

Напишите Python скрипт, который:

- Подключается к БД любого типа на ваш выбор (например, к PostgreSQL).
- Импортирует необходимые модели данных.
- Выводит издателя (publisher), имя или идентификатор которого принимается через `input()`.

## Задание 3 (необязательное)

Заполните БД тестовыми данными.

Тестовые данные берутся из файла (tests_data.json)[[/tests_data.json](https://github.com/DubrovinMikhail/python_sql_ORM/blob/main/tests_data.json)]. Пример содержания в JSON файле.

В
