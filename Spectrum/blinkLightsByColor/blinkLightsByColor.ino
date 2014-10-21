int yellow=A2;
int green=A1;
int red=A0;


void setup() {  
  pinMode(red, OUTPUT);
  pinMode(yellow,OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(A0, OUTPUT);
}

void loop() {
  digitalWrite(green, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);
  digitalWrite(green,LOW);
  digitalWrite(red, HIGH);
  delay(1000);
  digitalWrite(red,LOW);
  digitalWrite(yellow,HIGH);
  delay(1000);
  digitalWrite(yellow,LOW);
}
