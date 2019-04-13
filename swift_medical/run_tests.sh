docker-compose exec event-api python3 manage.py test
docker-compose exec score-api python3 manage.py test
docker-compose exec event-splitter python3 manage.py test