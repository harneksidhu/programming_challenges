docker-compose build
docker-compose up -d
docker-compose exec event-api python3 manage.py create_db
