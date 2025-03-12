FROM python:3.11-slim AS build

WORKDIR /app


COPY .env /app/
COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


WORKDIR /app

COPY . /app/


RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py collectstatic --noinput 

FROM python:3.11-slim

WORKDIR /app

COPY --from=build /app /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--settings=core.settings.production"]