#include <LiquidCrystal.h>

#define rs 6
#define enable 7

#define D4 8
#define D5 9
#define D6 10
#define D7 11

LiquidCrystal lcd(rs,enable,D4,D5,D6,D7);
byte smiley[8] = {
  B00000,
  B10001,
  B00000,
  B00000,
  B10001,
  B01110,
  B00000,
};


void setup() {
  // put your setup code here, to run once:
  pinMode(rs,OUTPUT);
  pinMode(enable,OUTPUT);

  pinMode(D4,OUTPUT);
  pinMode(D5,OUTPUT);
  pinMode(D6,OUTPUT);
  pinMode(D7,OUTPUT);

  lcd.createChar(0, smiley);
  lcd.begin(16,2);
}

void loop() {
  int i;
  
  lcd.setCursor(0,0);
  lcd.write(byte(0));
  
  while (42)
  {
    lcd.scrollDisplayRight();
    delay(100);
  }
}
