

# Работа с менеджером урлов

## Задание

Необходимо в менеджере урлов `file_server/urls.py`
реализовать схему отображения для трех ситуаций:

* отображение списка файлов
* отображение списка файлов с фильтрацией по дате `/2018-01-01/`
* отображение отдельных файлов `/file_name.txt`

Для первых двух ситуаций использовать один класс для отображения: `file_server.views.FileList`
Для второй ситуации реализовать конвертер для преобразования даты
`datetime.date` в указанный в задании вид и наоборот.
Для третьей ситуации использовать функцию для отображения: `file_server.views.file`

В классе `file_server.views.FileList` и функции `file_server.views.file`
реализовать логику для формирования контекста.

## Документация по проекту

Для запуска проекта необходимо:

### шаг первый

Установить зависимости:

```bash
pip install -r requirements.txt
```

### шаг второй

Создать файл с локальными настройками `file_server/settings_local.py`
и задать туда обязательные параметры:

* SECRET_KEY - секретная строка
* FILES_PATH - путь до директории с файлами

Например:

```python
import os

SECRET_KEY = 'd+mw&mscg5i&tx+#@bf+6m%e+d5z!u#!n%z-^o9u7y1felv2o&'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILES_PATH = os.path.join(BASE_DIR, 'files')
```

### шаг третий

Выполнить команду:

```bash
python manage.py runserver
```