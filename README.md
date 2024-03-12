# Web Rotas - Aplicação de Autenticação e Renderização de Mapa

Este projeto consiste em uma aplicação web que oferece funcionalidades de autenticação de usuários e renderização de um mapa com base em um arquivo JSON contendo coordenadas de trajetos cronológicos.

## Funcionalidades

- **Autenticação de Usuários**: Os usuários podem se autenticar na aplicação fornecendo suas credenciais de login.
- **Armazenamento de Usuários**: As informações dos usuários são armazenadas em um banco de dados MySQL.
- **Renderização de Mapa**: Utilizando a API Leaflet.js, a aplicação renderiza um mapa com marcadores em cada coordenada contida no arquivo `Posicoes.json`.
- **Trajeto Cronológico**: O sistema cria uma linha poligonal unindo as coordenadas do arquivo `Posicoes.json`, mostrando um trajeto cronológico.


## Tecnologias Utilizadas

- **Flask**: Framework web em Python para o desenvolvimento de aplicativos web.
- **MySQL**: Banco de dados relacional utilizado para armazenar as informações dos usuários.
- **Leaflet.js**: Biblioteca JavaScript de código aberto para renderização interativa de mapas.
- **HTML/CSS**: Linguagens de marcação e estilo para criar a interface do usuário.
- **JavaScript**: O frontend da aplicação utiliza JavaScript para interações dinâmicas.

## Instruções de Execução

1. Clone o repositório para o seu ambiente local.
2. Configure a conexão com o banco de dados de sua escolha no arquivo `config.py`.
3. Execute o arquivo `index.py` para iniciar a aplicação.
4. Acesse a aplicação em seu navegador e utilize as funcionalidades de autenticação e visualização do mapa.
