"""
File containing parse messages function
"""
import serial

from model import Model

def parse_message(arduino_port, baud_rate):
    """
    Return what the player most recently scored

    Args: 
        arduino_port: a String representing the port the Arduino is
        connected from

        baud_rate: an integer representing the baud_rate
    
    Returns:
        an integer representing how much to increment the score by
    """
    scores = [100, 50, 40, 30, 10, 0]
    score = 0

    try:
        arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    except:
        print("Please check the port and baud rate")

    raw_data = arduino.readline()
    string_data = raw_data.decode()
    data = string_data[0: len(scores)]

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
