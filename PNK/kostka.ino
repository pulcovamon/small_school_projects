#define led_01 A0
#define led_04 A1
#define led_06 A2
#define led_02 6
#define led_03 5
#define led_05 4
#define led_07 3
#define button 7


void setup() {
  // put your setup code here, to run once:
  pinMode(led_01, OUTPUT);
  pinMode(led_02, OUTPUT);
  pinMode(led_03, OUTPUT);
  pinMode(led_04, OUTPUT);
  pinMode(led_05, OUTPUT);
  pinMode(led_06, OUTPUT);
  pinMode(led_07, OUTPUT);
  pinMode(button, INPUT);

  digitalWrite(led_01, HIGH);
  digitalWrite(led_02, HIGH);
  digitalWrite(led_03, HIGH);
  digitalWrite(led_04, HIGH);
  digitalWrite(led_05, HIGH);
  digitalWrite(led_06, HIGH);
  digitalWrite(led_07, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  bool pushed = digitalRead(button);


  if (pushed == 0) {
    digitalWrite(led_01, HIGH);
    digitalWrite(led_02, HIGH);
    digitalWrite(led_03, HIGH);
    digitalWrite(led_04, HIGH);
    digitalWrite(led_05, HIGH);
    digitalWrite(led_06, HIGH);
    digitalWrite(led_07, HIGH);
    
    int num = random(1,7);

    if (num == 1) {
      digitalWrite(led_02, LOW);
    } else if (num == 2) {
      digitalWrite(led_04, LOW);
      digitalWrite(led_05, LOW);
    } else if (num == 3) {
      digitalWrite(led_02, LOW);
      digitalWrite(led_06, LOW);
      digitalWrite(led_07, LOW);
    } else if (num == 4) {
      digitalWrite(led_01, LOW);
      digitalWrite(led_03, LOW);
      digitalWrite(led_06, LOW);
      digitalWrite(led_07, LOW);
    } else if (num == 5) {
      digitalWrite(led_02, LOW);
      digitalWrite(led_04, LOW);
      digitalWrite(led_05, LOW);
      digitalWrite(led_06, LOW);
      digitalWrite(led_07, LOW);
    } else {
      digitalWrite(led_01, LOW);
      digitalWrite(led_03, LOW);
      digitalWrite(led_04, LOW);
      digitalWrite(led_05, LOW);
      digitalWrite(led_06, LOW);
      digitalWrite(led_07, LOW);
    }
  }

  delay(100);
  

}
