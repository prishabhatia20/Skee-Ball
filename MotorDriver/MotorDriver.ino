#define enA 9
#define enB 10
#define in1 6
#define in2 7
#define in3 4
#define in4 5

bool ballDetect = false;
int motorRunTime = 3500; // Define motorRunTime variable
unsigned long motorTime = 0; // Declare motorTime variable

void setup() {
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

void loop() {
  if (ballDetect == true) { // Corrected syntax for if statement
    motorTime = millis();
    ballDetect = false; // Reset ballDetect after capturing the time
  }

  if (millis() - motorTime < motorRunTime) { // Corrected syntax for if statement and logical condition
    analogWrite(enA, 255); // Send PWM signal to L298N Enable pin
    analogWrite(enB, 255); // Send PWM signal to L298N Enable pin
  } else {
    analogWrite(enA, 0); // Send PWM signal to L298N Enable pin
    analogWrite(enB, 0); // Send PWM signal to L298N Enable pin
  }
}