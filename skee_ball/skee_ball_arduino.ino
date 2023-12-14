int hundred = A0;
int fifty = A1;
int forty = A2;
int twenty = A3;
int ten = A4;
int zero = A5;

#define enA 9
#define enB 10
#define in1 6
#define in2 7
#define in3 4
#define in4 5

int sensorThreshold = 100;

// Define motorRunTime variable
int motorRunTime = 3500;

// Declare motorTime variable
unsigned long motorTime = 0;


// Index 0 = hundred
// Index 1 = fifty
// Index 2 = forty
// Index 3 = twenty
// Index 4 = ten
// Index 5 = zero

// [hundred, fifty, forty, twenty, ten, zero]
int sensorVals[6] = {0, 0, 0, 0, 0, 0};

int prevSensorVals[6] = {0, 0, 0, 0, 0, 0};

int sensorReadings[6] = {0, 0, 0, 0, 0, 0};

bool changeReadings[6] = {false, false, false, false, false, false};

int numSensors = 6;

bool sendList = false;


void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Motor setup
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  
  // Set initial rotation direction
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);

}

void spinMotors() {
  if (sendList == true) { // Corrected syntax for if statement
    motorTime = millis();
    sendList = false; // Reset ballDetect after capturing the time
  }

  if (millis() - motorTime < motorRunTime) {
    analogWrite(enA, 255); // Send PWM signal to L298N Enable pin
    analogWrite(enB, 255); // Send PWM signal to L298N Enable pin
  } 
  else {
    analogWrite(enA, 0); // Send PWM signal to L298N Enable pin
    analogWrite(enB, 0); // Send PWM signal to L298N Enable pin
  }

}

void readSensors() {
  int s0 = analogRead(hundred);
  int s1 = analogRead(fifty);
  int s2 = analogRead(forty);
  int s3 = analogRead(twenty);
  int s4 = analogRead(ten);
  int s5 = analogRead(zero);

  sensorReadings[0] = s0;
  sensorReadings[1] = s1;
  sensorReadings[2] = s2;
  sensorReadings[3] = s3;
  sensorReadings[4] = s4;
  sensorReadings[5] = s5;
}

void processState() {

  // For all values in sensorReadings
  for (int i = 0; i < numSensors; i++) {
    int sensor = sensorReadings[i];

    // If the ith index of sensorReadings is below the threshold
    // Change that index to 1
    if (sensor < sensorThreshold) {
      sensorVals[i] = 1;
      // If the ith index of sensorVals equals the ith index
      // of prevSensorVals, set sendList to False
      if (sensorVals[i] == prevSensorVals[i]) {
        changeReadings[i] = false;
      }
      // Else, the threshold has been crossed and the list is changed
      else {
        changeReadings[i] = true;
      }

      prevSensorVals[i] = sensorVals[i];

    }
    else {

      // Change sensorVals to 0 because now the sensor readings are above
      // the sensing threshold
      sensorVals[i] = 0;

      // sendList is now false
      changeReadings[i] = false;
      prevSensorVals[i] = sensorVals[i];

    }

    for (int i = 0; i < numSensors; i++) {
      if (changeReadings[i] == true) {
        sendList = true;
        break;
      }
      else {
        sendList = false;
      }
    }

  }


}

void loop() {
  // Read sensor values
  readSensors();

  // Process state
  processState();

  String data = String("");
  

  if (sendList) {
    for (int i = 0; i < numSensors; i++) {
      data += sensorVals[i];
    }
    Serial.print(data);
    // Spin motors when sensor goes off
    spinMotors();
  }

}
