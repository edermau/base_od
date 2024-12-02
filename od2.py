import pandas as pd

def create_origin_destination_base(caminhos_file_path, od_output_file_path):
    # Carregar os dados da base de caminhos gerada anteriormente
    data = pd.read_excel(caminhos_file_path)
    
    # Verificar se as colunas necessárias existem no DataFrame
    required_columns = ['msisdn', 'dt_start_time', 'ds_site', 'nome_site', 'long', 'lat',
                        'next_dt_start_time', 'next_ds_site', 'time_diff']
    if not all(column in data.columns for column in required_columns):
        raise ValueError("O arquivo de caminhos não contém todas as colunas necessárias.")
    
    # Garantir que as colunas de tempo sejam convertidas para o tipo datetime
    data['dt_start_time'] = pd.to_datetime(data['dt_start_time'], errors='coerce')
    data['next_dt_start_time'] = pd.to_datetime(data['next_dt_start_time'], errors='coerce')
    
    # Recalcular a diferença de tempo para garantir que seja um Timedelta
    data['time_diff'] = data['next_dt_start_time'] - data['dt_start_time']
    
    # Filtrar para manter apenas registros com diferença de tempo superior a 5 minutos
    filtered_data = data[data['time_diff'] > pd.Timedelta(minutes=5)]
    
    # Criar a base de origem e destino
    od_data = pd.DataFrame()
    od_data['msisdn'] = filtered_data['msisdn']
    od_data['origem_site'] = filtered_data['ds_site']
    od_data['origem_nome_site'] = filtered_data['nome_site']
    od_data['origem_long'] = filtered_data['long']
    od_data['origem_lat'] = filtered_data['lat']
    od_data['destino_site'] = filtered_data['next_ds_site']
    od_data['destino_nome_site'] = filtered_data['next_ds_site'] 
    od_data['destino_long'] = filtered_data['long'].shift(-1)
    od_data['destino_lat'] = filtered_data['lat'].shift(-1)
    od_data['dt_start_time'] = filtered_data['dt_start_time']
    od_data['next_dt_start_time'] = filtered_data['next_dt_start_time']
    od_data['time_diff'] = filtered_data['time_diff']
    
    # Remover registros com valores nulos resultantes do shift
    od_data = od_data.dropna(subset=['destino_site', 'destino_long', 'destino_lat'])
    
    # Resetar o índice
    od_data.reset_index(drop=True, inplace=True)
    
    # Salvar a base de origem e destino em um novo arquivo Excel
    od_data.to_excel(od_output_file_path, index=False)
    print(f"Base de Origem e Destino salva em: {od_output_file_path}")

# Caminho do arquivo de caminhos gerado anteriormente
caminhos_file_path = '/Users/emau/Documents/base_de_caminhos9.xlsx'

# Caminho do arquivo de saída para a base de origem e destino
od_output_file_path = '/Users/emau/Documents/base_origem_destino.xlsx'

# Criar a base de origem e destino
create_origin_destination_base(caminhos_file_path, od_output_file_path)
