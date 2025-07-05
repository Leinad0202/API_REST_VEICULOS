#  API REST - Cadastro de Veículos
Uma API RESTful desenvolvida com FastAPI, que permite o cadastro, listagem, atualização e exclusão de veículos. Conta com autenticação via API Key, persistência com SQLite + SQLAlchemy, além de estar dockerizada, documentada via Swagger, e com testes automatizados com Pytest.

✅ Tecnologias Utilizadas
- Python 3.8+

- FastAPI

- SQLAlchemy (com SQLite)

- Uvicorn

- Docker + Docker Compose

- Pytest

# Autenticação
A API exige autenticação via API Key. Envie a chave no cabeçalho das requisições:

```bash
X-API-Key: 123456
```

# Endpoints da API

| Método | Rota             | Descrição                                         |
| ------ | ---------------- | ------------------------------------------------- |
| GET    | `/veiculos`      | Lista todos os veículos (com filtros e paginação) |
| GET    | `/veiculos/{id}` | Retorna um veículo pelo ID                        |
| POST   | `/veiculos`      | Cria um novo veículo                              |
| PUT    | `/veiculos/{id}` | Atualiza os dados de um veículo                   |
| DELETE | `/veiculos/{id}` | Remove um veículo do sistema                      |

# Filtros e Paginação

O endpoint GET /veiculos suporta os seguintes parâmetros de filtro:

marca

modelo

ano

placa

Também possui paginação com os parâmetros:

skip: número de registros a pular (default: 0)

limit: número máximo de registros a retornar (default: 10)

# 🛠️ Como executar o projeto localmente

### 1. Clonar o repositório
```bash
git clone <url-do-seu-repositório>
cd nome-do-projeto
```

### 2. Criar ambiente virtual e instalar dependências
```bash
python -m venv api_carros_env
.\api_carros_env\Scripts\activate
pip install -r requirements.txt
```
### 3. Rodar o servidor FastAPI
```bash
cd src
uvicorn main:app --reload
```
Acesse a documentação interativa em:
🔗 http://127.0.0.1:8000/docs

# 🐳 Executando com Docker

### 1. Subindo o projeto com Docker Compose
```bash
docker compose up --build
```
A aplicação será exposta em:

API: http://localhost:8000
Swagger (documentação): http://localhost:8000/docs

# Rodando os Testes Automatizados (Pytest)
⚠️ Atenção: O arquivo test_veiculos.py está totalmente comentado com aspas triplas (""") para evitar conflitos durante a execução normal da API.

### Para rodar os testes:
1. Remova as aspas triplas (""") do início e fim do arquivo test_veiculos.py para que os testes sejam executados.

2. Execute o comando:
```bash
pytest
```

3. Após os testes, adicione novamente as aspas triplas para evitar erros ao subir a API com o uvicorn.

# Estrutura dos dados
```json
{
  "id": 1,
  "marca": "Chevrolet",
  "modelo": "Onix",
  "ano": 2020,
  "placa": "ABC-1234"
}
```

# 📚 Documentações úteis

[📘 FastAPI](https://fastapi.tiangolo.com/learn/)

[🧱 SQLAlchemy ORM](https://docs.sqlalchemy.org/en/20/orm/quickstart.html#declare-models)

[🐍 Python 3](https://docs.python.org/3/contents.html)

[🐳 Docker](https://docs.docker.com/)
