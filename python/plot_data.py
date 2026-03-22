import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
df = pd.read_csv('measurements.csv', header=None)

# Asignar nombres de columnas
df.columns = ['timestamp', 'temperatura', 'humedad', 'luz']

# Convertir timestamp a formato datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Graficar temperatura
plt.figure()
plt.plot(df['timestamp'], df['temperatura'])
plt.title('Temperatura vs Tiempo')
plt.xlabel('Tiempo')
plt.ylabel('Temperatura (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Graficar humedad
plt.figure()
plt.plot(df['timestamp'], df['humedad'])
plt.title('Humedad vs Tiempo')
plt.xlabel('Tiempo')
plt.ylabel('Humedad (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Graficar luz
plt.figure()
plt.plot(df['timestamp'], df['luz'])
plt.title('Luz vs Tiempo')
plt.xlabel('Tiempo')
plt.ylabel('Nivel de luz')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
