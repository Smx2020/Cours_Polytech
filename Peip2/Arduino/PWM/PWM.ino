#define led_rouge 3
#define button 8

void setup() {
  pinMode(led_rouge, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int i;
  i = 0;
  while (42)
  {
    if (digitalRead(button) == HIGH)
      i++;
    if (i >= 255)
      i = 0;
    analogWrite(led_rouge,i);
    Serial.println(digitalRead(button));
    Serial.println(i);
    delay(10);
  }
}
