#define led_red   8
#define led_blue  10
#define led_green 9

void setup() {
  pinMode(led_red,INPUT);
  pinMode(led_blue,INPUT);
  pinMode(led_green,INPUT);
}

void loop() {
  digitalWrite(led_red,HIGH);
  digitalWrite(led_blue,HIGH);
  digitalWrite(led_green,HIGH);

}
