# Запуск и демонстрация

## Шаг 1. Запуск инфраструктуры:

`Bash
docker-compose up -d --build`

## Шаг 2. Проверка базовой работы:

Если вы просто обратитесь к localhost без заголовка, nginx-proxy вернет ошибку 503 Service Temporarily Unavailable, потому что он не знает, куда направлять неизвестный трафик:

`Bash
curl http://localhost/`
Но с правильным заголовком хоста (имитация домена) запрос попадет в наш бэкенд:

`Bash
curl -H "Host: backend.test" http://localhost/`

## Шаг 3. Динамическое масштабирование:

`Bash
docker-compose up -d --scale backend=3`
Что происходит под капотом: nginx-proxy через docker.sock мгновенно увидит событие создания новых контейнеров, сам перепишет свой внутренний конфигурационный файл (добавив новые IP в upstream) и сделает nginx -s reload.

## Шаг 4. Тест балансировки:

`Bash
for i in {1..12}; do curl -s -H "Host: backend.test" http://localhost/; sleep 0.5; done`