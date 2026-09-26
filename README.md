# Atividade Python + SQLite

Projeto acadêmico desenvolvido para praticar a integração entre **Python** e **SQLite**, realizando operações e consultas em um banco de dados.

Os dados utilizados neste projeto são **fictícios** e foram utilizados exclusivamente para fins de estudo.

## Tecnologias utilizadas

- Python
- SQLite
- SQL

## Sobre o projeto

O projeto utiliza um banco de dados SQLite contendo uma tabela de duplicatas com informações como:

- Nome do cliente
- Número da duplicata
- Valor
- Data de vencimento
- Banco

A aplicação em Python permite visualizar e manipular esses dados por meio de um menu no terminal.

## Funcionalidades

Entre as operações desenvolvidas estão:

- Listagem dos registros da tabela;
- Inserção de novos registros;
- Filtros utilizando `WHERE`;
- Ordenação utilizando `ORDER BY`;
- Cálculo de valores utilizando `SUM`;
- Formatação de datas;
- Exclusão de registros com `DELETE`;
- Consultas específicas solicitadas na atividade.

## Estrutura do projeto

```text
atividade-python-sqlite/
├── main.py
├── database_aa.db
├── .gitignore
└── README.md
```

## Para executar o projeto

Clone o repositório:

```bash
git clone https://github.com/oSaxe/atividade-python-sqlite.git
```

Entre na pasta:

```bash
cd atividade-python-sqlite
```

Execute:

```bash
python main.py
```