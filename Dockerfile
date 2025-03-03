FROM python:3.11-slim AS build

WORKDIR /app

RUN apt-get update \
    && apt-get install -y curl \
    && curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs

COPY .env /app/
COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY theme/static_src/package*.json /app/theme/static_src/

WORKDIR /app/theme/static_src

RUN npm install


WORKDIR /app

COPY . /app/

RUN python manage.py tailwind install

# Garante que o diretório staticfiles exista
RUN mkdir -p staticfiles/css

RUN python manage.py tailwind build
RUN ls -l staticfiles/css

RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py collectstatic --noinput 
RUN ls -l staticfiles/css
FROM python:3.11-slim

WORKDIR /app

COPY --from=build /app /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--settings=core.settings.production"]