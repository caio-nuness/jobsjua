FROM python:3.11-slim AS build

WORKDIR /app

RUN apt-get update \
    && apt-get install -y curl \
    && curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs

COPY .env /app/
COPY requirements.txt /app/

# Cria um ambiente virtual e instala as dependências do Python
RUN python -m venv venv
ENV PATH="/venv/bin:$PATH"

# atualiza o pip e instala as dependências do Python no ambiente virtual
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos package.json e package-lock.json para o diretório de trabalho
COPY theme/static_src/package*.json /app/theme/static_src/
WORKDIR /app/theme/static_src

# Executa o npm install no diretório theme/static_src
RUN npm install

RUN ls -la /app/theme/static_src/node_modules

# Volta para o diretório de trabalho principal
WORKDIR /app

# Copia todos os arquivos do diretório de trabalho para o diretório de trabalho do contêiner
COPY . /app/


# Executa o comando para instalar o Tailwind CSS e compilar os arquivos CSS
RUN python manage.py tailwind install 
RUN python manage.py tailwind build 
RUN python manage.py collectstatic --noinput 


FROM python:3.11-slim

WORKDIR /app

# Copia o ambiente virtual do contêiner de compilação para o contêiner de produção
COPY --from=build /app /app

# Cria um ambiente virtual e instala as dependências do Python
RUN python -m venv venv
ENV PATH="/venv/bin:$PATH"
# atualiza o pip e instala as dependências do Python no ambiente virtual
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Comando para aplicar as migrações
RUN python manage.py migrate --settings=core.settings.production

EXPOSE 8000

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--settings=core.settings.production"]