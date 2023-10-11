# Desafio

1. Crie uma API RESTful que permita aos usuários consultar informações de uma carteira de crédito. A API deve ter os seguintes endpoints:

- **GET /companies** - Retorna todas as informações de crédito das empresas cadastradas.
- **GET /companies/:cnpj** - Retorna as informações de crédito específico com base no CNPJ.
- **POST /companies** - Permite aos usuários adicionar uma nova empresa à carteira.
- **PUT /companies/:id** - Permite aos usuários atualizar as informações de uma empresa específica com base no ID.
- **DELETE /companies/:id** - Permite aos usuários remover uma empresa específica com base no ID.

2. Crie um banco de dados MySQL para armazenar as informações da carteira de investimentos. O banco de dados deve ter uma tabela chamada "companies" com os seguintes campos:

- **id**: Identificador único da empresa (chave primária).
- **name**: Nome da empresa.
- **cnpj**: CNPJ da empresa.
- **cnae**: Atividade econômica da empresa (ex: agricultura, construção, indústria de transformação).
- **monthly_income**: Faturamento mensal.
- **date**: Data de abertura da empresa.
- **registration_date**: Data e hora de inserção no banco de dados.

3. Implemente os endpoints da API usando FastAPI com SQLAlchemy para realizar as operações no banco de dados.

4. Adicione validação de entrada de dados para os endpoints de adição e atualização das empresas para garantir que os dados inseridos sejam válidos e estejam no formato correto.
