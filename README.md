

Перед установкой поисковика необходимо установить:
###### python 3.9
###### Postgres 14
###### Elasticsearch 8.7.0
##### Создание бд db setup.sql
 #
В конфиге elastic search:

__xpack.security.http.ssl: enabled: false__
## Установка
- Установить необходимые зависимости с помощью команд
```bash
  py -3.9 -m venv .venv
  .\.venv\Scripts\activate.bat
  pip install -r requirements.txt
```
- Указать в файле `config.ini` необходимые параметры подключения к БД Postgresql,
параметры подключения к индексу Elasticsearch
а также параметры индекса
## Запуск

```bash
  .\.venv\Scripts\activate.bat
  python .\main.py
```
Предварительно должен быть запущен сервер БД Postgres и Elasticsearch


## Документация
[http://127.0.0.1:12800/docs](http://127.0.0.1:12800/docs)


