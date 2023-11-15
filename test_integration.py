import serial

def parse_message(arduino_port, baud_rate):
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


def main():
    score = 0
    total_tries = 8
    num_tries = 0
    message = parse_message("/dev/ttyACM0", 9600)

    while num_tries < total_tries:
        if message > 0:
            score += message
            print(f"YOUR SCORE: {score}")
        else:
            score += message
            print(f"YOU DID NOT SCORE")
        num_tries += 1
    
    print(f"GAME OVER. FINAL SCORE: {score}")

