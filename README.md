# JobsJua

JobsJua é um projeto web desenvolvido com Django e Tailwind CSS. Este projeto utiliza Docker para facilitar o desenvolvimento e a implantação.

## Requisitos

- Docker
- Docker Compose

## Configuração do Ambiente de Desenvolvimento

1. Clone o repositório:

    ```sh
    git clone https://github.com/seu-usuario/jobsjua.git
    cd jobsjua
    ```

2. Crie um arquivo [.env](http://_vscodecontentref_/1) na raiz do projeto com as variáveis de ambiente necessárias. :

Exemplo    ```env
    DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgres://user:password@db:5432/jobsjua
    ```

3. Construa e inicie os contêineres Docker:

    ```sh
    docker-compose up --build
    ```

4. Acesse o aplicativo no navegador:

    ```
    http://localhost:8000
    ```

## Estrutura do Projeto

- `theme/static_src/`: Diretório contendo os arquivos estáticos do Tailwind CSS.
- `requirements.txt`: Arquivo contendo as dependências do Python.
- `Dockerfile`: Arquivo de configuração do Docker para construir a imagem do projeto.
- `docker-compose.yml`: Arquivo de configuração do Docker Compose para orquestrar os contêineres.

## Comandos Úteis

### Executar Migrações

Para aplicar as migrações do banco de dados, execute:

```sh
docker-compose exec web python manage.py migrate --settings=core.settings.production