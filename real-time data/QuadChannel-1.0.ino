// Defining the Analog inputs
int vol0 = A0;
int vol1 = A1;
int vol2 = A2;
int vol3 = A3;

// Void Setup -> Just for initiating the baud rate
void setup() {
  Serial.begin(9600);
}

void loop() {
  // sensor #1
  Serial.print(analogRead(vol0));
  Serial.print("-");
  
  // sensor #2
  Serial.print(analogRead(vol1));
  Serial.print("-");
  
  // sensor #3
  Serial.print(analogRead(vol2));
  Serial.print("-");
  
  // sensor #4
  Serial.println(analogRead(vol3));
  
  delay(850); // this parameter can be adjusted due to the sensors and real-time analysis complexity
}
