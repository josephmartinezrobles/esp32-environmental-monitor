import serial

# Cambia COM3 según tu PC
ser = serial.Serial('COM3', 115200)

while True:
    try:
        line = ser.readline().decode().strip()
        print(line)
    except:
        print("Error reading data")
