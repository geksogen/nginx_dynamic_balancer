#!/bin/bash

# Стучимся на локальный порт 80, но передаем заголовок Host,
# чтобы nginx-proxy понял, к какому сервису мы обращаемся.
URL="http://localhost/"
HOST_HEADER="Host: backend.test"
REQUESTS=12

echo "Начинаем тестирование Nginx-Proxy (Docker Socket)..."
echo "Слушаем домен: backend.test"
echo "------------------------------------------------"

for ((i=1; i<=REQUESTS; i++)); do
    printf "Запрос %02d: " "$i"
    curl -s -H "$HOST_HEADER" "$URL"
    sleep 0.5
done

echo "------------------------------------------------"