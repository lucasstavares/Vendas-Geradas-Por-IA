# Gerador de Tabelas de Vendas Sintéticas

Este projeto foi criado com o intuito de praticar fórmulas básicas do Excel utilizando diferentes tipos de base de dados. O objetivo é gerar tabelas de vendas sintéticas para diferentes tipos de comércio, utilizando a API do Google Generative AI (modelo Gemini 1.5 Pro) e o pacote OpenPyXL para manipulação de arquivos Excel.

## Descrição do Projeto

O projeto permite a criação de uma tabela de vendas sintéticas, levando em consideração diversos campos como data da venda, hora da venda, loja, produto, quantidade, valor unitário, valor total, forma de pagamento, idade e sexo do cliente. Os dados gerados são salvos em um arquivo Excel ('.xlsx') na pasta 'planilhas'.

## Funcionalidades

- Geração automática de dados sintéticos de vendas.
- Personalização do tipo de comércio e do período de vendas.
- Exportação dos dados gerados para um arquivo Excel.

## Pré-requisitos

Você precisa ter o seguinte instalado em seu ambiente:

- Python 3.7 ou superior
- Biblioteca 'openpyxl'
- Biblioteca 'google-generativeai'
- Biblioteca 'python-dotenv'
- Acesso à API do Google Generative AI