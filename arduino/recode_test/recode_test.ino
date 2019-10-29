int REC = 5;
int PLAYE = 6;
int PLAYL = 7;
int FT = 8;

char input;

void setup() {
  Serial.begin(9600);
  pinMode(REC, OUTPUT);
  pinMode(PLAYE, OUTPUT);
  pinMode(PLAYL, OUTPUT);
  pinMode(FT, OUTPUT);
}

void loop() {
  if(Serial.available())
  {
    input = Serial.read();
    
    if(input == 'R')
    {
      digitalWrite(REC,HIGH);
      Serial.println("REC...");
    }
    else if(input == 'E')
    {
      digitalWrite(PLAYE,HIGH);
      Serial.println("PLAYE...");
      digitalWrite(PLAYE,LOW);
    }
    else if(input == 'L')
    {
      digitalWrite(PLAYL,HIGH);
      Serial.println("PLAYL...");
      delay(10000);
      digitalWrite(PLAYL,LOW);
    }
    else if(input == 'F')
    {
      digitalWrite(FT,HIGH);
      Serial.println("FT...");
    }
    else if(input == 'S')
    {
      digitalWrite(REC,LOW);
      digitalWrite(FT,LOW);
      Serial.println("STOP...");
    }
    else
    {
      Serial.println("wrong input value");
    }
  }
