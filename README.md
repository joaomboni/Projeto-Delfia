# Sistema de Gestão de Documentos Criptografados

Este projeto é uma API para upload, armazenamento e recuperação de documentos criptografados. A API é construída com Flask e permite o gerenciamento seguro de documentos PDF criptografados usando criptografia simétrica.

## Estrutura do Projeto

- **app.py**: Arquivo principal da API que define as rotas e a lógica de autenticação.
- **crypto.py**: Contém funções para criptografar e descriptografar arquivos PDF.
- **generate_key.py**: Script para gerar e salvar a chave de criptografia.
- **generate_api_key.py**: Script para gerar e salvar uma chave de API para autenticação.
- **api_key.txt**: Arquivo que contém a chave de API usada para autenticação.
- **secret.key**: Arquivo que contém a chave de criptografia simétrica.
- **test.py**: Arquivo de teste.

### Configuração

### Download de bibliotecas

- pip install flask flask-httpauth cryptography
- pip install flask-testing

### Gerar a Chave de Criptografia

Antes de executar a API, você precisa gerar uma chave de criptografia. Navegue até a raiz do projeto e Execute o seguinte comando para gerar o arquivo `secret.key`:

```bash
python generate_key.py

### Gerar a chave para API

Também será necessário gerar uma chave de API para autenticação. Navegue até a raiz do projeto e Execute o seguinte comando para gerar e salvar a chave em `api_key.txt`:


```bash
python generate_api_key.py

### Executar a API

Navegue até a raiz do projeto e execute o seguinte comando:

```bash
python app.py

### Executar Teste

Navegue até a raiz do projeto e execute o seguinte comando:

```bash
python unittest test.py

## Endpoints da API

### Upload de Arquivo

- **Método:** `POST`
- **URL:** `/upload`
- **Cabeçalhos:**
  - `Authorization`: (Chave de API gerada no arquivo `api_key.txt`)
- **Form-data:**
  - `file`: (Arquivo PDF para upload)
- **Resposta:**
  - **Código:** `201 Created`
  - **Corpo:** `{ "message": "Upload realizado e criptografado com sucesso." }`
- **Código de Erro:**
  - `400 Bad Request`: Se não houver arquivo ou se o arquivo não for PDF.

### Listar Arquivos

- **Método:** `GET`
- **URL:** `/list`
- **Cabeçalhos:**
  - `Authorization`: (Chave de API gerada no arquivo `api_key.txt`)
- **Resposta:**
  - **Código:** `200 OK`
  - **Corpo:** Lista de arquivos criptografados no formato JSON.

### Baixar Arquivo

- **Método:** `GET`
- **URL:** `/download/<filename>`
- **Parâmetros de URL:**
  - `filename`: Nome do arquivo criptografado a ser baixado.
- **Cabeçalhos:**
  - `Authorization`: (Chave de API gerada no arquivo `api_key.txt`)
- **Resposta:**
  - **Código:** `200 OK`
  - **Corpo:** O arquivo PDF descriptografado.
- **Código de Erro:**
  - `401 Unauthorized`: Se a chave de API for inválida.
  - `404 Not Found`: Se o arquivo não for encontrado.

## Relatório

### Escolhas Técnicas

1. **Framework e Biblioteca para API:**
   - **Flask** foi escolhido para o desenvolvimento da API devido à sua simplicidade e flexibilidade. Flask permite a criação rápida de endpoints e integração com bibliotecas externas.
   - **Flask-HTTPAuth** foi utilizado para implementar a autenticação baseada em API Key, substituindo a autenticação básica com usuário e senha.

2. **Criptografia:**
   - **Cryptography** foi selecionada para criptografar e descriptografar documentos. A biblioteca `Fernet` foi usada devido à sua robustez e facilidade de uso, oferecendo criptografia simétrica com um mecanismo de chave seguro.

3. **Armazenamento de Arquivos:**
   - Os arquivos são armazenados no diretório `documents`. Arquivos PDF são criptografados e salvos com a extensão `.enc` para indicar que são criptografados. Isso permite fácil distinção entre arquivos originais e criptografados.

4. **Geração e Armazenamento de Chave de API:**
   - A chave de API é gerada aleatoriamente usando a biblioteca `secrets` e armazenada em um arquivo `api_key.txt`. Esse método fornece uma chave segura e única para autenticação.

### Desafios Encontrados

1. **Criação e Gerenciamento de Chaves de Criptografia:**
   - Garantir a geração e armazenamento seguro da chave de criptografia foi um desafio. A chave deve ser protegida para evitar acesso não autorizado. Decidiu-se armazenar a chave em um arquivo separado para simplificar o gerenciamento.

2. **Manejo de Arquivos Criptografados:**
   - O processo de criptografia e descriptografia dos arquivos teve que ser cuidadosamente implementado para garantir que os arquivos não fossem corrompidos. Também foi necessário garantir que os arquivos fossem corretamente descriptografados antes do download.

3. **Autenticação e Autorização:**
   - A mudança de autenticação básica para uma autenticação baseada em chave API exigiu ajustes na lógica de autorização. Garantir que a autenticação API funcionasse corretamente foi crucial para a segurança do sistema.

4. **Manipulação de Erros e Exceções:**
   - Lidando com erros como arquivos ausentes ou não autorizados, a aplicação deve fornecer respostas claras e úteis. O tratamento apropriado de erros é essencial para a robustez da aplicação.

### Expansões Futuras

1. **Interface de Usuário:**
   - **Desenvolvimento de uma Interface Web:** Criar uma interface gráfica de usuário (GUI) para facilitar o upload e download de arquivos, bem como a visualização da lista de arquivos.

2. **Aprimoramento da Segurança:**
   - **Autenticação e Autorização Adicionais:** Implementar métodos de autenticação mais avançados, como OAuth, para maior segurança e controle de acesso.
   - **Criptografia de Dados em Trânsito:** Usar HTTPS para garantir que todos os dados transmitidos entre o cliente e o servidor estejam criptografados.

3. **Suporte a Múltiplos Tipos de Arquivo:**
   - **Expansão para Outros Formatos de Arquivo:** Adicionar suporte para criptografar e descriptografar outros formatos de arquivo além de PDFs.

4. **Melhorias no Desempenho:**
   - **Otimização de Processos:** Melhorar o desempenho da criptografia e descriptografia, especialmente para arquivos grandes, para reduzir o tempo de processamento.

5. **Logs e Monitoramento:**
   - **Implementar Sistema de Monitoramento:** Adicionar um sistema de monitoramento para rastrear e analisar o uso da API, e gerar alertas em caso de falhas ou atividades suspeitas.

6. **Backup e Recuperação:**
   - **Sistema de Backup:** Implementar soluções de backup para garantir que arquivos criptografados e a chave de criptografia sejam armazenados de forma segura e possam ser recuperados em caso de falhas.

Esse relatório fornece uma visão geral das escolhas técnicas feitas durante o desenvolvimento da API, os desafios encontrados e possíveis caminhos para futuras melhorias e expansões.
