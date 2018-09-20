#define BUTTON 5
int feu[3] = {2,3,4};

void setup() {
  
  int i=0;
  while (i < 3)
  {
    pinMode(feu[i], OUTPUT);
    i++;
  }
  pinMode(BUTTON, INPUT);

  Serial.begin(9600);
}

void set_feu(int c)
{
  int i=0;
  while (i<3)
  {
    if (i == c)
      digitalWrite(feu[i], HIGH);
    else
      digitalWrite(feu[i], LOW);
    i++;
  }
}

// the loop function runs over and over again forever
void loop() {
  int i=0;

  while(42)
  {
    set_feu(0);
    delay(1000);

    Serial.println(digitalRead(BUTTON));
    //if (digitalRead(BUTTON) == LOW)
    i++;
    if (i > 2)
      i = 0;
  }
}
