/*
 *
 * Isaac Salier-Hellendag
 * October 3, 2007
 * TUI Assignment 5
 *
 * Ghostbusters!
 * When there's something strange in the neighborhood, or at least when the 
 * lights are turned off, ghouls and spooks come out and it's time for Bill Murray,
 * Dan Aykroyd, and the other two dudes to get to work.
 *
 * The photocell responds when the light goes below a certain level, as the Piezo speaker
 * plays the Ghostbusters theme, the LED lights flash as a siren, and the Piezo sounds
 * the siren tones.
 *
 */

int photocellPin = 0;    // select the input pin for the potentiometer
int speakerPin = 9;
int redLedPin = 11;
int blueLedPin = 7;

int lightVal = 0;
int numFlashes = 25;
int sirenCount = 50;

byte names[] = {'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C'};  
int tones[] = {1915, 1700, 1519, 1432, 1275, 1136, 1014, 956};
byte melody[] = "1f1p1f1p4b1p4g1p4a1p4f8p1d1p1d1p1d1p1d1p2c1p1d8p8p";
// count length: 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
//                                10                  20                  30
int count = 0;
int count2 = 0;
int count3 = 0;
int MAX_COUNT = 24;
int statePin = LOW;

void setup() {
  pinMode(speakerPin, OUTPUT); 
  //beginSerial(9600);
  //Serial.println("ready");
}

void loop() {
  digitalWrite(speakerPin, LOW);
  
  if(nightTime()) {
    playMelody();
    for(int i=0 ; i < numFlashes ; i++) {
      flashSiren();
    }
  }

}

void flashSiren() {
    analogWrite(redLedPin, 255);
    for(int i=0 ; i < sirenCount ; i++) {
      digitalWrite(speakerPin, HIGH);
      delayMicroseconds(tones[7]);
      digitalWrite(speakerPin, LOW);
      delayMicroseconds(tones[7]);
    }
    delay(500);
    analogWrite(redLedPin, 0);
    analogWrite(blueLedPin, 255);
    for(int i=0 ; i < sirenCount ; i++) {
      digitalWrite(speakerPin, HIGH);
      delayMicroseconds(tones[6]);
      digitalWrite(speakerPin, LOW);
      delayMicroseconds(tones[6]);
    }
    delay(500);
    analogWrite(blueLedPin, 0);
}

void playTheme() {
  
}

boolean nightTime() {
  lightVal = analogRead(photocellPin);
  return (lightVal < 200);
}
           

void playMelody() {
  digitalWrite(speakerPin, LOW);     
  for (count = 0; count < MAX_COUNT; count++) {
    statePin = !statePin;
    for (count3 = 0; count3 <= (melody[count*2] - 48) * 30; count3++) {
      for (count2=0;count2<8;count2++) {
        if (names[count2] == melody[count*2 + 1]) {       
          digitalWrite(speakerPin,HIGH);
          delayMicroseconds(tones[count2]);
          digitalWrite(speakerPin, LOW);
          delayMicroseconds(tones[count2]);
        } 
        if (melody[count*2 + 1] == 'p') {
          // make a pause of a certain size
          digitalWrite(speakerPin, 0);
          delayMicroseconds(500);
        }
      }
    }
  }
}
