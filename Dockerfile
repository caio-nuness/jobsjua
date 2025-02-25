FROM python:3.11-slim

RUN apt-get update && apt-get install -y libpq-dev gcc

RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs npm

RUN npm install -g yarn 

WORKDIR /app 

RUN yarn -i

COPY . .


RUN pip install --no-cache-dir -r requirements.txt 

COPY . /app/

EXPOSE 8000

CMD ["make", "run"] # Executa as migrações e inicia o Gunicorn