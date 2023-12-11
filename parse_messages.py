"""
File containing parse messages function
"""
import serial

# from model import Model

def parse_message(arduino_port, baud_rate, serial_object):
    """
    Return what the player most recently scored

    Args: 
        arduino_port: a String representing the port the Arduino is
        connected from

        baud_rate: an integer representing the baud_rate
    
    Returns:
        a String that is the message sent from the Arduino IDE
    """

    # num_sensors = 6
    num_sensors = 4

    # Read and parse serial data
    raw_data = serial_object.readline()
    string_data = raw_data.decode()
    data = string_data[0: num_sensors]
    print(f"Parse messages Data: {data}")

    return data






