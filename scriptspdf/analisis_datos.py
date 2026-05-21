import os
import pandas as pd
import matplotlib.pyplot as plt

# Rutas relativas para garantizar reproducibilidad absoluta
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(_file_)))
DATA_PATH = os.path.join(BASE_DIR, 'datos', 'sales_data.csv')
RESULTS_DIR = os.path.join(BASE_DIR, 'resultados')

def ejecutar_analisis():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Error: No se encontro el dataset en {DATA_PATH}")
        
    print("Procesando dataset de ventas comerciales de la empresa...")
    
    # Importar dataset
    df = pd.read_csv(DATA_PATH)
    
    # Formatear la fecha
    df['sales_date'] = pd.to_datetime(df['sales_date'])
    df['mes'] = df['sales_date'].dt.to_period('M')
    
    # Cálculos exigidos por el Escenario B
    ventas_totales = df['sales_amount'].sum()
    top_ventas_registro = df.loc[df['sales_amount'].idxmax()]
    ventas_por_mes = df.groupby('mes')['sales_amount'].sum()
    
    # Imprimir indicadores en consola
    print("\n=== REPORTE DE RESULTADOS OPERATIVOS ===")
    print(f"Ventas Totales Consolidadas: ${ventas_totales:,.2f}")
    print(f"Registro con Mayor Impacto Comercial (ID {top_ventas_registro['id']}): ${top_ventas_registro['sales_amount']:,.2f}")
    print("\nVentas por Periodo Mensual:")
    print(ventas_por_mes)
    
    # Exportar reporte de texto a /resultados
    with open(os.path.join(RESULTS_DIR, 'metricas_finales.txt'), 'w') as f:
        f.write("=== REPORTE EJECUTIVO DE VENTAS UTN ===\n")
        f.write(f"Ventas Totales del Periodo: ${ventas_totales:,.2f}\n")
        f.write("\nDesglose Mensual Realizado:\n")
        f.write(ventas_por_mes.to_string())

    # Generar gráfico de evolución de ventas
    plt.figure(figsize=(10, 5))
    ventas_por_mes.plot(kind='line', marker='o', color='navy', linewidth=2)
    plt.title('Evolucion Mensual de Ventas Comerciales', fontsize=12, fontweight='bold')
    plt.xlabel('Periodo de Venta (Anio-Mes)', fontsize=10)
    plt.ylabel('Monto Total Transaccionado ($)', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    
    # Guardar gráfico en /resultados
    plot_output_path = os.path.join(RESULTS_DIR, 'grafico_resultados.png')
    plt.savefig(plot_output_path, dpi=300)
    plt.close()
    print(f"\nAnalisis completado. Elementos exportados a /resultados.")

if _name_ == "_main_":
    ejecutar_analisis()