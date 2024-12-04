
# Base de Origem e Destino

Este repositório contém dados e scripts relacionados a uma **base de caminhos** para análises de origem e destino. É particularmente útil em aplicações como logística, mobilidade urbana, telecomunicações e processamento de fluxos dinâmicos. 

## Contexto

A análise principal utiliza uma **heurística temporal** com intervalos de 5 minutos. Este intervalo pode ser ajustado conforme a necessidade de granularidade e o desempenho do sistema. Antes de executar os scripts que utilizam essa heurística, é necessário processar a base de caminhos disponível neste repositório.

---


## Pré-requisitos

Certifique-se de que as seguintes ferramentas estão instaladas no seu ambiente:

- **Python 3.x ou superior**.
- Dependências:
  - `pandas`
  - `openpyxl`

As bibliotecas podem ser instaladas utilizando o comando:
```bash
pip install pandas openpyxl 

Bibliotecas necessárias (listadas em `requirements.txt`).


### Instalação das Dependências
Execute o comando abaixo para instalar todas as dependências:

```bash
pip install -r requirements.rtf

# Script para Criação de Base de Origem-Destino (O-D)

Este repositório contém um script em Python para criar uma base de Origem-Destino (O-D) a partir de uma base de caminhos previamente gerada. O objetivo é automatizar a análise de dados de mobilidade com base em registros de CDR (Call Detail Records).

## Funcionamento do Script

O script realiza as seguintes operações:

1. **Carregamento de Dados**:
   - O script lê um arquivo Excel contendo a base de caminhos gerada anteriormente.

2. **Validação de Dados**:
   - É verificado se todas as colunas necessárias estão presentes no arquivo de entrada:
     - `msisdn`
     - `dt_start_time`
     - `ds_site`
     - `nome_site`
     - `long`
     - `lat`
     - `next_dt_start_time`
     - `next_ds_site`
     - `time_diff`

3. **Conversão de Formatos**:
   - As colunas `dt_start_time` e `next_dt_start_time` são convertidas para o formato datetime.
   - A diferença de tempo entre registros consecutivos (`time_diff`) é recalculada para garantir precisão.

4. **Filtragem por Heurística Temporal**:
   - Apenas registros com diferença de tempo superior a 5 minutos são mantidos, representando trocas de local relevantes.

5. **Criação da Base de Origem-Destino**:
   - São extraídos os seguintes dados para compor a base:
     - Identificador anonimizado do usuário (`msisdn`).
     - Dados da origem (site, coordenadas e timestamp inicial).
     - Dados do destino (site, coordenadas e timestamp final).
     - Diferença de tempo entre os eventos.

6. **Limpeza de Dados**:
   - Registros com valores nulos resultantes de operações de `shift` são removidos.

7. **Exportação dos Resultados**:
   - A base de Origem-Destino é salva em um novo arquivo Excel.

Estrutura do Código
Função create_origin_destination_base:

Responsável por processar os dados da base de caminhos e gerar a base de Origem-Destino.
Entradas:

caminhos_file_path: Caminho do arquivo Excel contendo a base de caminhos.
od_output_file_path: Caminho onde será salvo o arquivo Excel com a base O-D.
Saídas:

Um arquivo Excel com a base de Origem-Destino.
Exemplo de Execução
Certifique-se de que o arquivo de caminhos (base_de_caminhos9.xlsx) foi gerado previamente e está localizado no caminho correto.

# Caminho do arquivo de entrada (base de caminhos gerada previamente)
caminhos_file_path = '/Users/emau/Documents/base_de_caminhos9.xlsx'

# Caminho do arquivo de saída (base O-D)
od_output_file_path = '/Users/emau/Documents/base_origem_destino.xlsx'

# Executar o script
create_origin_destination_base(caminhos_file_path, od_output_file_path)

Observações
Este script deve ser executado após a criação da base de caminhos, no repositorio tem um arquivo de base de caminhos.
Certifique-se de que os arquivos Excel possuem a estrutura de dados correta antes de executar o script.

# Contribuição
Sinta-se à vontade para contribuir com este projeto através de pull requests. Qualquer sugestão ou melhoria é bem-vinda!

# Público-Alvo
Esse Script Pythonfoi projetado para vários usuários, incluindo:
Desenvolvedores de software
Administradores de sistema
Gerentes de TI
Arquitetos de TI
Engenheiros de Telecomunicações

# Licença
Este projeto está licenciado sob os termos da licença do MIT.

