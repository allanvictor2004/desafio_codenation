# A aplicação faz uma requisição a API do desafio e
# e salva a resposta em um arquivo answer.json.
import json, requests

# Definindo a url da requisição, já com o token:
MEU_TOKEN = '8060997db46d1bdcf857a8c43638552bb10f0b02'
URL_DA_API = f'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={MEU_TOKEN}'

# Fazendo a requisição a api e salvando no arquivo answer.json:
response = requests.get(URL_DA_API)

# Log da aplicação:
print(f'status-code: {response.status_code}')
print(f'content: {response.content}')