/*  Arduino DC Motor Control - PWM | H-Bridge | L298N */


#define enA 9
#define enB 10
#define in1 6
#define in2 7
#define in3 4
#define in4 5

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
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
}

void loop() {
  
  analogWrite(enA, 250); // Send PWM signal to L298N Enable pin
  analogWrite(enB, 250); // Send PWM signal to L298N Enable pin

  
}
