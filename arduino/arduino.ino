void lenOn(int led);

int redbtn = 7;
int greenbtn = 5;
int bluebtn = 6;

int redlg = 9;
int greenlg = 11;
int bluelg = 10;

int data = 0;

void setup() {
  Serial.begin(9600);
  pinMode(redbtn, INPUT);
  pinMode(greenbtn, INPUT);
  pinMode(bluebtn, INPUT);
  pinMode(redlg, OUTPUT);
  pinMode(greenlg, OUTPUT);
  pinMode(bluelg, OUTPUT);
}

void loop() {
  int red = digitalRead(redbtn);
  int green = digitalRead(greenbtn);
  int blue = digitalRead(bluebtn);

  if(red == HIGH) {
    Serial.println("U Red");
  }
  else if(green == HIGH) {
    Serial.println("U Green");
  }
  else if(blue == HIGH) {
    Serial.println("U Blue");
  }
  else {
    Serial.println("R Color");
    while(!Serial.available());
    data = Serial.readString().toInt();
    ledOn(data);
  }
  delay(1000);
}

void ledOn(int led) {
  if(led == 0) {
    analogWrite(redlg, 0);
    analogWrite(greenlg, 0);
    analogWrite(bluelg, 0);
  }
  else if(led == 1) {
    analogWrite(redlg, 255);
    analogWrite(greenlg, 0);
    analogWrite(bluelg, 0);
  }
  else if(led == 2) {
    analogWrite(redlg, 0);
    analogWrite(greenlg, 255);
    analogWrite(bluelg, 0);
  }
  else if(led == 3) {
    analogWrite(redlg, 0);
    analogWrite(greenlg, 0);
    analogWrite(bluelg, 255);
  }
  else {
    Serial.println("Error");
  }
}
