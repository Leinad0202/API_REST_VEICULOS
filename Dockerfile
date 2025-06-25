FROM python:3.11
# define a imagem base como Python 3.11
WORKDIR /app
# define o diretório de trabalho
COPY . /app
## copia o conteúdo do diretório atual para o diretório de trabalho no container
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# define as dependências do projeto
ENV PYTHONPATH=/app/src
# define o PYTHONPATH para incluir o diretório src
EXPOSE 8000
# expõe a porta 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"] 
# define o comando padrão para iniciar o servidor Uvicorn