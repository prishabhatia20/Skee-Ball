## serial communication jazz
import serial

from model import Model

def parse_message(arduino_port, baud_rate, model):
    scores = [100, 100, 50, 40, 30, 10, 0]
    score = 0

    try:
        arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    except:
        print("Please check the port")

    raw_data = arduino.readline().decode()
    data = raw_data.rstrip("\"")

    for i in range(0, len(scores)):
        if data[i] == 1:
            score += scores[i]
        else:
            score += 0
    
    return score






# if __name__ == "__main__":
#     ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
#     ser.reset_input_buffer()

#     while True:
#         if ser.in_waiting > 0:
#             line = ser.readline().decode("utf-8").rstrip()
#             print(line)
