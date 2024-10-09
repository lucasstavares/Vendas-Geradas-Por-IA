import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
from openpyxl import Workbook
import re

tipo_comercio = 'restaurante coreano'
# não aumente tanto o tempo de venda, IA terá dificuldades em gerar todos os dados se o intervalo exceder um mês.
tempo_de_venda = 'uma semana'
# 35 é o máximo que o gemini-1.5-pro consegue gerar.
quantidade_de_valores = 35

load_dotenv(find_dotenv())
genai.configure(api_key=os.environ.get("API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro")
prompt = fprompt = f"Gere uma tabela de vendas fictícia para um(a) {tipo_comercio}, no título coloque o tipo de comercio,considerando os seguintes campos: data da venda (formato AAAA-MM-DD), hora da venda, loja, produto (apenas quando necessário, com categoria, tamanho, ingredientes), quantidade, valor unitário, valor total, forma de pagamento, idade e sexo do cliente (adicione ou exclua colunas se for necessário dependendo do contexto). O período de vendas é de {tempo_de_venda}.Não utilize acentos ou cedilhas nos valores da tabela, titulos e nomes. Crie ao menos {quantidade_de_valores} itens."
response = model.generate_content(prompt)

cleaned_response = re.sub(r'\*', '', response.text) 
cleaned_response = re.sub(r'#[^a-zA-Z0-9]*', '', cleaned_response)

lines = cleaned_response.strip().split('\n')

cleaned_lines = []
for i, line in enumerate(lines):
    if i > 0 and line.strip().startswith('|') and 'Data' in lines[i - 1]: 
        continue  
    cleaned_lines.append(line)

data = [line.split('|') for line in cleaned_lines]

def convert_to_int(value):
    try:
        return int(float(value))
    except ValueError:
        return value

for i in range(1, len(data)):
    for j in range(len(data[i])):
        data[i][j] = convert_to_int(data[i][j].strip())  

title = data[0][0] 
title = title.replace(' - ', '_')  
title = title.replace(' ', '_')  

wb = Workbook()
ws = wb.active
ws.title = "Tabela de Vendas"

ws.append(data[0]) 

for row in data[1:]:
    ws.append(row) 

folder_name = 'planilhas'
os.makedirs(folder_name, exist_ok=True) 
file_path = os.path.join(folder_name, f"{title}.xlsx") 
wb.save(file_path)

print(f"Arquivo XLSX '{file_path}' criado com sucesso!")