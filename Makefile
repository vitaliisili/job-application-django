runserver:
	cd api && python manage.py runserver

install:
	cd api && pip install -r requirements.txt

makemigrations:
	cd api && python manage.py makemigrations

migrate:
	cd api && python manage.py migrate

createsuperuser:
	cd api && python manage.py createsuperuser

startapp:
	cd api/apps && django-admin startapp $(app)

flake:
	cd api && flake8

install-web:
	cd ui && npm install

start-web:
	cd ui && npm start

build-web:
	cd ui && npm run build

test:
	cd api && python -m pytest

test-class:
	cd api && python -m pytest -k $(class)

testprint:
	cd api && python -m pytest -s

test-cov:
	cd api && python -m pytest --cov

test-cov-detail:
	cd api && python -m pytest --cov-report term-missing --cov

collectstatic:
	cd api && python -m manage collectstatic

shell:
	cd api && python -m manage shell

create-env:
	cd api && \
	echo 'DB_NAME=test_db_name' > .env && \
	echo 'DB_USER=test_db_user' >> .env && \
	echo 'DB_PASSWORD=test_password' >> .env && \
	echo 'DB_HOST=localhost' >> .env && \
	echo 'DB_PORT=5432' >> .env && \
	echo 'DJANGO_SECRET_KEY="super_secret_key_write_here"' >> .env && \
	echo 'DJANGO_DEBUG=1' >> .env && \
	echo 'DATABASE_ENGINE=postgresql' >> .env && \
	echo 'DJANGO_ALLOWED_HOSTS="127.0.0.1,http://localhost:3000/,localhost"' >> .env && \
	echo 'CSRF_TRUSTED_ORIGINS="http://127.0.0.1,http://localhost:3000/"' >> .env && \
	echo 'CORS_ALLOWED_ORIGINS="http://localhost:3000"' >> .env && \
	echo 'TOKEN_EXPIRE=7' >> .env && \
	echo 'REFRESH_TOKEN_EXPIRE=28' >> .env

create-env-ui:
	cd ui && echo 'REACT_APP_BACKEND_URL=http://localhost:8000' > .env

spectacular:
	cd api && python -m manage spectacular --file schema.yml