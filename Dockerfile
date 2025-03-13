# Stage de Build
FROM python:3.11-slim AS build

WORKDIR /app

# Instalação do Node.js e Yarn usando corepack
RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs
RUN corepack enable

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN yarn --version
COPY theme/static_src/package*.json ./
COPY theme/static_src/package-lock.json ./

COPY . /app/

RUN python manage.py tailwind build
RUN python manage.py collectstatic --noinput

# Stage de Runtime
FROM python:3.11-slim

WORKDIR /app

COPY --from=build /app/staticfiles /app/staticfiles
COPY --from=build /app /app

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--settings", "core.settings.base"]
