python manage.py migrate
docker build -t web:latest .
docker run -d --name django-recruitment_task -e "PORT=8765" -e "DEBUG=0" -p 8000:8765 web:latest