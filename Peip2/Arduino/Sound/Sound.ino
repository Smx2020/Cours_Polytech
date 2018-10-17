#define input A0
#define output 6
#define check A2

void setup() {
  pinMode(input, INPUT);
  pinMode(output, OUTPUT);
  pinMode(check, INPUT);
  Serial.begin(9600);
}

void loop() {
  int tmp;
  tmp = analogRead(input);
  analogWrite(output,tmp/4);
  Serial.print(5.0*(analogRead(check)-tmp)/1023);
  Serial.print(" ");
  Serial.print(5.0*analogRead(check)/1023);
  Serial.print(" ");
  Serial.print(5.0*tmp/1023);
  Serial.print("\n");
  delay(0);
}
