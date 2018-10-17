//#include <TM1637Display.h>

//#define CLK D6 //Set the CLK pin connection to the display
//#define DIO D5 //Set the DIO pin connection to the display
#define POTO A0

int feu[3] = {11,13,12};
//TM1637Display display(CLK, DIO); //set up the 4-Digit Display.
bool etat_old = false;

void setup() {
  
  int i=0;
  while (i < 3)
  {
    pinMode(feu[i], OUTPUT);
    i++;
  }
  
  //display.setBrightness(0x0f); //set the diplay to maximum brightness
  pinMode(POTO, INPUT);
  pinMode(8, INPUT);

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

void set_led(int c)
{
  int i=0;
  while (i<3)
  {
    if (i >= c)
      digitalWrite(feu[i], HIGH);
    else
      digitalWrite(feu[i], LOW);
    i++;
  }
}

// the loop function runs over and over again forever
void loop() {
  int i=0;
  float j;

  while(42)
  {
    j = 5*analogRead(POTO)/1023.0;
    
    //display.showNumberDec(i); //Display i
    set_feu(i%3);
    
    delay(100);
    if (j <= 2.4)
      i = 2;
    else if (j <= 2.6)
      i = 1;
    else
      i = 0;
    //if (etat_old == true && digitalRead(BUTTON) == false)
    //{
    Serial.print(j);
    Serial.print(", ");
    Serial.println(digitalRead(8));
    //}
    //etat_old = digitalRead(BUTTON);
    //if (i > 2)
    //  i = 0;
  }
}
