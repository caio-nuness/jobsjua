# Define o nome do arquivo WSGI do seu projeto
WSGI_FILE = nome_do_seu_projeto.wsgi  # Substitua pelo nome correto

# Tarefa para executar as migrações
migrate:
        python manage.py migrate

# Tarefa para iniciar o Gunicorn
start:
        gunicorn --bind 0.0.0.0:8000 $(WSGI_FILE)


build-tailwind:
        python manage.py tailwind build
       

# Tarefa para rodar o tailwind
tailwind-whatch:
        python manage.py tailwind start

run:
        make migrate && make start && make build-tailwind