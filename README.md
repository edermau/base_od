
# Base de Origem e Destino

Este repositório contém dados e scripts relacionados a uma **base de caminhos** para análises de origem e destino. É particularmente útil em aplicações como logística, mobilidade urbana, telecomunicações e processamento de fluxos dinâmicos. 

## Contexto

A análise principal utiliza uma **heurística temporal** com intervalos de 5 minutos. Este intervalo pode ser ajustado conforme a necessidade de granularidade e o desempenho do sistema. Antes de executar os scripts que utilizam essa heurística, é necessário processar a base de caminhos disponível neste repositório.

---

## Estrutura do Repositório

- **`data/`**: Contém os arquivos de dados brutos e processados.
  - `caminhos_brutos.json`: Dados brutos da base de caminhos.
  - `caminhos_processados.json`: Dados processados após a execução do script principal.
  
- **`scripts/`**: Scripts para manipulação e análise da base.
  - `process_base.py`: Script para pré-processar a base de caminhos.
  - `analyze_paths.py`: Script para aplicar análises usando a heurística temporal.

- **`README.md`**: Este arquivo com as instruções e documentação do projeto.

---

## Pré-requisitos

Certifique-se de que as seguintes ferramentas estão instaladas no seu ambiente:

- Python 3.8 ou superior.
- Bibliotecas necessárias (listadas em `requirements.txt`).

### Instalação das Dependências
Execute o comando abaixo para instalar todas as dependências:

```bash
pip install -r requirements.txt

