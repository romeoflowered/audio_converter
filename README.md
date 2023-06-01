# Руководство по установке и запуску Audio Converter

В этом репозитории представлен сервис Audio Converter, который позволяет загружать аудиофайлы, конвертировать их и скачивать результаты конвертации. В этом руководстве вы найдете инструкции по сборке докер-образа с сервисом, его настройке и запуску. Также мы предоставим вам примеры запросов к методам сервиса.

## Требования

Перед началом установки убедитесь, что у вас установлены следующие компоненты:

- Docker: https://docs.docker.com/get-docker/
- Docker Compose: https://docs.docker.com/compose/install/

## Шаги установки и запуска

1. Клонируйте репозиторий:

```shell
git clone https://github.com/romeoflowered/audio_converter.git
```

2. Перейдите в директорию проекта:

```shell
cd audio_converter
```

3. Создайте файл `.env`, содержащий необходимые переменные окружения. Пример содержимого файла `.env`:

```
DB_HOST=db
DB_PORT=5433
DB_USER=postgres
DB_PASS=postgres
DB_NAME=audio_db

POSTGRES_DB=audio_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

4. Соберите и запустите контейнеры с помощью Docker Compose:

```shell
docker-compose up -d
```

5. Дождитесь завершения сборки и запуска контейнеров. Вы можете проверить статус контейнеров с помощью команды:

```shell
docker-compose ps
```

6. Когда контейнеры успешно запущены, вы можете использовать сервис Audio Converter. Он будет доступен по адресу `http://localhost:8000`.

## Примеры запросов

### Создание нового пользователя

**URL:** `http://localhost:8000/user`
**Метод:** `POST`
**Тело запроса (JSON):**

```json
{
  "name": "John Doe"
}
```

**Успешный ответ (JSON):**

```json
{
  "user_id": 1,
  "token": "your_token"
}
```

### Загрузка аудиофайла и конвертация

**URL:** `http://localhost:8000/audio`
**Метод:** `POST`
**Тело запроса (multipart/form-data):**
- `user_id`: 1 (идентификатор пользователя)
- `token`: "your_token" (токен пользователя)
- `audio_file`: Загружаемый аудиофайл (файл WAV)

**Успешный ответ (JSON):**

```json
{
  "audio_id": "your_audio_id",
  "download_url": "http://localhost:8000/record?id=your_audio_id&user=1"
}
```

### Скачивание аудиофайла

**URL:** `http://localhost:8000/audio`
**Метод:** `GET`


**Параметры запроса:**
- `user_id`: 1 (идентификатор пользователя)
- `token`: "your_token" (токен пользователя)
- `audio_uuid`: "your_audio_id" (идентификатор аудиофайла)

**Успешный ответ (JSON):**

```json
{
  "audio_id": "your_audio_id",
  "download_url": "http://localhost:8000/record?id=your_audio_id&user=1"
}
```
### Важно!
Обратите внимание, что это только примеры запросов, и вам может потребоваться дополнительная информация о структуре данных и параметрах запросов. Вы можете обратиться к встроенной документации FastAPI, доступной по адресу http://localhost:8000/docs, для получения полной информации о доступных маршрутах, параметрах запросов и моделях данных.