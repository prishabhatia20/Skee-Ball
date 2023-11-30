import serial
import pandas as pd

# def parse_message(arduino_port, baud_rate):
#     # scores = [50, 40, 30, 20, 10]
#     scores = [50, 40]
#     score = 0

while True:

    arduino_port = "/dev/ttyACM0"
    baud_rate = 9600

    # try:
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    # except Exception as e:
    #     print("Error: {e}")
    #     # return score

    # print("test")
    # raw_data = arduino.readline().decode()
    # data = raw_data.rstrip("\"")

    # if arduino.in_waiting > 0:
    # raw_data = arduino.readline().decode()
    raw_data = arduino.readline()
    # print(f"Raw data: {raw_data}")
    string_data = raw_data.decode()
    print(f"String data: {string_data}")
    filtered_data = string_data[0:2]
    print(f"Filtered data: {filtered_data}")
    # data = string_data[2]
    # print(data)
    
        # print(f"Message: {raw_data}")
    # data = list(map(int, raw_data))
    # print(data)

    # if len(data) == len(scores):
    #     for i in range(len(scores)):
    #         if data[i] == 1:
    #             score += scores[i]



    # for i in range(0, len(scores)):
    #     if data[i] == 1:
    #         score += scores[i]
    #     else:
    #         score += 0
    
    # return score
    


# def main():
#     # score = 0
#     total_tries = 8
#     num_tries = 0
#     message = parse_message("/dev/ttyACM0", 9600)

#     while num_tries < total_tries:
#     #     if message > 0:
#     #         score += message
#     #         print(f"YOUR SCORE: {score}")
#     #         num_tries += 1
#     #     # else:
#     #     #     print("NO SCORE")

    
#     # print(f"GAME OVER. FINAL SCORE: {score}")
#         print(f"Message: {message}")

# if __name__ == "__main__":
#     main()

