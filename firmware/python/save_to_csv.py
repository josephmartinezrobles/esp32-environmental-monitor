import serial
import csv
from datetime import datetime

ser = serial.Serial('COM3', 115200)

with open('measurements.csv', 'a', newline='') as file:
    writer = csv.writer(file)

    while True:
        try:
            line = ser.readline().decode().strip()
            print(line)

            # Separar datos
            data = line.split(',')

            if len(data) == 3:
                temperatura = float(data[0])
                humedad = float(data[1])
                luz = int(data[2])

                timestamp = datetime.now()

                writer.writerow([timestamp, temperatura, humedad, luz])

        except:
            print("Error processing data")
