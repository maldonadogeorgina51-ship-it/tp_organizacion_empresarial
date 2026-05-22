import os
import pandas as pd
import matplotlib.pyplot as plt

# Definimos las rutas manualmente para evitar problemas
BASE_DIR = r"C:\Users\georg\Documents\GitHub\tp_organizacion_empresarial"
DATA_PATH = os.path.join(BASE_DIR, 'datospdf', 'sales_data.csv')
RESULTS_DIR = os.path.join(BASE_DIR, 'resultadospdf')

print("Iniciando proceso...")

if not os.path.exists(DATA_PATH):
    print("ERROR: No encuentro el archivo de datos.")
else:
    df = pd.read_csv(DATA_PATH)
    df['sales_date'] = pd.to_datetime(df['sales_date'])
    df['mes'] = df['sales_date'].dt.to_period('M')
    
    ventas_totales = df['sales_amount'].sum()
    ventas_por_mes = df.groupby('mes')['sales_amount'].sum()
    
    print("Ventas totales calculadas.")
    
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)
        
    with open(os.path.join(RESULTS_DIR, 'metricas_finales.txt'), 'w') as f:
        f.write(str(ventas_totales))
        
    plt.figure()
    ventas_por_mes.plot()
    plt.savefig(os.path.join(RESULTS_DIR, 'grafico.png'))
    print("Archivo terminado correctamente.")