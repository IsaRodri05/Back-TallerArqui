#!/bin/sh

echo "Esperando a que MySQL esté listo..."
until nc -z -v -w30 db_products 3306
do
  echo "Esperando a MySQL..."
  sleep 5
done

echo "MySQL está listo, ejecutando migraciones y el servidor..."
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver 0.0.0.0:8000