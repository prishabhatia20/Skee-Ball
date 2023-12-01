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
        a String that is the message sent from the Arduino IDE
    """

    num_sensors = 6
    scores = [100, 50, 40, 30, 10, 0]
    score = 0

    try:
        arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    except:
        print("Please check the port and baud rate")

    raw_data = arduino.readline()
    string_data = raw_data.decode()
    data = string_data[0: num_sensors]

    return data

    # for i in range(0, len(scores)):
    #     if data[i] == 1:
    #         score += scores[i]
    #     else:
    #         score += 0
    
    # return score





