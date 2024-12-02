
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
pip install -r requirements.rtf


### Passos para Execução
Clone o Repositório

git clone https://github.com/edermau/basedecaminhos
cd basedecaminhos
Pré-processamento da Base Execute o script process_base.py para processar a base de caminhos:

python scripts/process_base.py
Entrada: data/caminhos_brutos.json
Saída: data/caminhos_processados.json
Execução do Script com a Heurística Temporal Após o pré-processamento, utilize o script analyze_paths.py para aplicar a heurística temporal:

python scripts/analyze_paths.py --interval 5
Parâmetro --interval: Define o intervalo de tempo em minutos (padrão: 5 minutos).
Configuração da Heurística Temporal
Por padrão, o intervalo temporal é de 5 minutos, mas você pode ajustá-lo no script analyze_paths.py ou passar o parâmetro --interval ao executá-lo.

### Exemplo com intervalo de 10 minutos:


python scripts/analyze_paths.py --interval 10
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias, correções ou novos recursos.

### Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo de licença para mais detalhes.

### Autor
Desenvolvido por Eder Mauricio Barbosa Para dúvidas ou sugestões, entre em contato pelo repositório ou pelo e-mail disponível no perfil do autor.
