FROM python:3.11-slim AS build

WORKDIR /app


RUN apt-get update \
    && apt-get install -y curl \
    && curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs

COPY requirements.txt /app/

RUN python -m venv venv
ENV PATH="/venv/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY theme/static_src/package*.json ./
COPY package-lock.json ./
RUN npm install

COPY . /app/

RUN python manage.py tailwind build
RUN python manage.py collectstatic --noinput

FROM python:3.11-slim

WORKDIR /app

COPY --from=build /app/staticfiles /app/staticfiles
COPY --from=build /app /app
COPY requirements.txt /app/
COPY .env /app/

RUN python -m venv venv
ENV PATH="/venv/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py migrate 

EXPOSE 8000

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--settings", "core.settings.production"]