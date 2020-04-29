# A aplicação faz uma requisição a API do desafio e
# e salva a resposta em um arquivo answer.json.
import json, string #, requests

# # Definindo a url da requisição, já com o token:
# MEU_TOKEN = '8060997db46d1bdcf857a8c43638552bb10f0b02'
# URL_DA_API = f'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={MEU_TOKEN}'

# # Fazendo a requisição a api e salvando no arquivo answer.json:
# response = requests.get(URL_DA_API)

# with open('./answer.json', 'w') as json_file:
# 	json_data = json.loads(response.content)

# 	json.dump(json_data, json_file, indent=4)

# Lendo do arquivo answer.json:
with open('./answer.json') as json_file:

	alfabeto = list(string.ascii_lowercase)

	json_data = json.load(json_file)

	cifrado_content = json_data["cifrado"]

	cifrado_content = cifrado_content.lower()
	print(cifrado_content)
	print(alfabeto)





# # Log da aplicação:
# print(f'headers: {response.headers}')
# print(f'status-code: {response.status_code}')
# print(f'content: {response.content}')