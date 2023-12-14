"""
File containing parse messages function
"""
import serial

def parse_message(serial_object):
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

    # Read and parse serial data
    raw_data = serial_object.readline()
    print(f"raw data: {raw_data}")
    string_data = raw_data.decode()
    data = string_data[0: num_sensors]

    return data






