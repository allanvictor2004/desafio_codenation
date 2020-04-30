# A aplicação faz uma requisição a API do desafio e
# e salva a resposta em um arquivo answer.json.
import json, string, requests

from hashlib import sha1

# # Definindo a url da requisição, já com o token:
MEU_TOKEN = '8060997db46d1bdcf857a8c43638552bb10f0b02'

URL_DA_API = {}

URL_DA_API["generate-data"] = f'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={MEU_TOKEN}'
URL_DA_API["submit-solution"] = f'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={MEU_TOKEN}'

# # Fazendo a requisição a api e salvando no arquivo answer.json:
# response = requests.get(URL_DA_API["generate-data"])

# with open('./answer.json', 'w') as json_file:
# 	json_data = json.loads(response.content)

# 	json.dump(json_data, json_file, indent=4)

# del json_file

# Lendo do arquivo answer.json:
# with open('./answer.json', 'r') as json_file:

# 	json_data = json.load(json_file)

# 	cifrado_content = json_data["cifrado"].lower()
# 	numero_casas = json_data["numero_casas"]
# 	alfabeto = list(string.ascii_lowercase)

# 	decifrado = ''

# 	for i in cifrado_content:
# 		if i in alfabeto:
# 			pos = alfabeto.index(i) - numero_casas
# 			decifrado += alfabeto[pos]
# 		else:
# 			decifrado += i

# 	json_data["decifrado"] = decifrado

# 	encoding = json_file.encoding
# 	resumo_criptografico = sha1(decifrado.encode(encoding)).hexdigest()
# 	json_data["resumo_criptografico"] = resumo_criptografico

# if json_file.closed:
# 	del json_file
# 	print(json.dumps(json_data, indent=4))

# 	with open('./answer.json', 'w') as json_file:
# 		json.dump(json_data, json_file, indent=4)

file = {"answer": open('./answer.json', 'rb')}
response = requests.post(URL_DA_API["submit-solution"], files=file)

status_code = response.status_code
json_data = json.loads(response.content)

print(f'status-code {status_code}')
print(json.dumps(json_data, indent=4))



# # Log da aplicação:
# print(f'headers: {response.headers}')
# print(f'status-code: {response.status_code}')
# print(f'content: {response.content}')