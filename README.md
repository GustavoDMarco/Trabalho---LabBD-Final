# Trabalho Laboratório de Banco de Dados
<h3>URL STREAMLIT: https://curriculos-e-vagas.streamlit.app

<br>

## Informações de Entrega do Projeto
> Administrador do site = login: admin / senha: admin123

> https://cloud.mongodb.com/v2/691ec15ac98ec91e5d8aa887#/overview

> login e senha mongodb = login: gustavomarco_db_user / senha: labbd123

## Funcionalidades

### Candidatos
- Cadastro completo de currículo (Experiência, Formação, Habilidades).
- Visualização de vagas disponíveis.

### Empregadores/Admin
- Cadastro e gerenciamento de vagas.
- **Recomendação Automática:** O sistema utiliza Full Text Search para cruzar requisitos da vaga com habilidades dos candidatos, gerando um *match score*.
- **Geolocalização:** Visualização interativa (PyDeck) das vagas distribuídas pelo mapa do Brasil.
- **Dashboard Administrativo:** Controle total sobre currículos e vagas cadastrados.

## Tecnologias e Infraestrutura

A infraestrutura foi desenhada pensando em escalabilidade e facilidade de deploy na nuvem.

- **Frontend/Backend:** [Streamlit](https://streamlit.io/) (Python)
- **Banco de Dados:** [MongoDB Atlas](https://www.mongodb.com/atlas/database) (NoSQL)
  - Utilizado para armazenar documentos flexíveis de Vagas e Currículos.
- **Geolocalização:** PyDeck

### Estrutura do Banco de Dados (MongoDB)
Foram utilizadas duas coleções principais como dataset `labbd`:
1. **vagas**: Armazena título, descrição, salário, requisitos, empresa e localização.
2. **curriculos**: Armazena dados pessoais, formação, skills e experiência profissional.

<br>

## Estrutura do Projeto

```
/
├── app.py                      # Ponto de entrada (Login e Home)
├── connection_mongo.py         # Configuração de conexão com MongoDB Atlas
├── pages/
│   ├── cadastro_vaga.py        # Formulário de vagas
│   ├── cadastro_curriculo.py   # Formulário de currículos
│   ├── listar_vagas.py         # Listagem e exclusão de vagas
│   ├── listar_curriculos.py    # Listagem e exclusão de currículos
│   ├── recomendacao.py         # Score Vaga x Candidato
│   ├── localiza_cidades.py     # Mapa de localização das vagas
├── cidades/
│   ├── cidades_brasil.csv       # DataSet de cidades para mapa de localização das vagas
└── requirements.txt            # Dependências do projeto
```  

<br>

## Como rodar o projeto localmente

1. Clone o repositório:
``` bash
    git clone [https://github.com/seu-usuario/seu-repo.git](https://github.com/seu-usuario/seu-repo.git)
    cd seu-repo
```
2. Crie um ambiente virtual (opcional):
```bash
    python -m venv venv
    
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
```
3. Instale as dependências:
```bash
    pip install -r requirements.txt
``` 

4. Execute a aplicação:
```bash
    streamlit run app.py
```
