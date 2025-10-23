import pandas as pd
import matplotlib.pyplot as plt

# Dados do monitor serial (tensão capacitor, tensão resistor)
data = """0.00 5.00
0.20 4.80
0.39 4.61
0.57 4.43
0.74 4.26
0.91 4.09
1.07 3.93
1.23 3.77
1.38 3.62
1.52 3.48
1.66 3.34
1.79 3.21
1.92 3.08
2.04 2.96
2.16 2.84
2.27 2.73
2.38 2.62
2.48 2.52
2.58 2.42
2.67 2.33
2.77 2.23
2.85 2.15
2.94 2.06
3.02 1.98
3.10 1.90
3.17 1.83
3.25 1.75
3.31 1.69
3.38 1.62
3.45 1.55
3.50 1.50
3.56 1.44
3.62 1.38
3.68 1.32
3.73 1.27
3.78 1.22
3.83 1.17
3.87 1.13"""

# Ler os dados em DataFrame
df = pd.read_csv(pd.io.common.StringIO(data), sep=r'\s+', engine='python', names=['Vcapacitor(V)', 'Vresistor(V)'])

# Gráfico 1: Carga no capacitor (tensão do capacitor)
plt.figure(figsize=(8, 5))
plt.plot(df.index, df['Vcapacitor(V)'], label='Tensão no Capacitor (V)', marker='o', linestyle='-')
plt.title('Carga do Capacitor em Circuito RC')
plt.xlabel('Tempo (unidades arbitrárias)')
plt.ylabel('Tensão (V)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('grafico_capacitor.png')
plt.show()

# Gráfico 2: Descarga no resistor (tensão do resistor)
plt.figure(figsize=(8, 5))
plt.plot(df.index, df['Vresistor(V)'], label='Tensão no Resistor (V)', marker='x', linestyle='-')
plt.title('Descarga do Resistor em Circuito RC')
plt.xlabel('Tempo (unidades arbitrárias)')
plt.ylabel('Tensão (V)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('grafico_resistor.png')
plt.show()

# Gráfico 3: Comparativo entre capacitor e resistor
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Vcapacitor(V)'], label='Tensão no Capacitor (V)', marker='o', linestyle='-')
plt.plot(df.index, df['Vresistor(V)'], label='Tensão no Resistor (V)', marker='x', linestyle='-')
plt.title('Comparação Tensão Capacitor vs Resistor no Circuito RC')
plt.xlabel('Tempo (unidades arbitrárias)')
plt.ylabel('Tensão (V)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('grafico_comparativo.png')
plt.show()