
const byte interruptPin = 0;
const byte directionPin = 1;
const byte rightPin = 2;
const byte leftPin = 3;

void setup() {
//  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  pinMode(interruptPin, INPUT);
  pinMode(directionPin, INPUT);
  pinMode(rightPin, OUTPUT);
  pinMode(leftPin, OUTPUT);
  attachInterrupt(digitalPinToInterrupt(interruptPin), handle_interrupt, RISING);
  digitalWrite(leftPin, 0);
  digitalWrite(rightPin, 0);
}

void loop() {
}

void handle_interrupt() {
  int direction = digitalRead(directionPin);
  if (direction == 0){
    digitalWrite(rightPin, 0);
    digitalWrite(rightPin, 1);
    digitalWrite(rightPin, 0);
//    Serial.print("Right\n");
  } else {
    digitalWrite(leftPin, 0);
    digitalWrite(leftPin, 1);
    digitalWrite(leftPin, 0);
//    Serial.print("Left\n");
  }
}
