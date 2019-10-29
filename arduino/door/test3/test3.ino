#include <Keypad.h>

 // 적외선 센서 핀번호 선언
int motion = 13; 
// 13번 고정 LED 핀번호 선언
int inte = 12;

//초음파센서 핀번호
int trig = 10;
int echo = 11;


const byte ROWS = 4;    // 행(rows) 개수
const byte COLS = 4;    // 열(columns) 개수
char keys[ROWS][COLS] = {
  {'1','4','7','*'},
  {'2','5','8','0'},
  {'3','6','9','#'},
  {'A','B','C','D'}
};
 
byte rowPins[ROWS] = {6, 7, 8, 9};   // R1, R2, R3, R4 단자가 연결된 아두이노 핀 번호
byte colPins[COLS] = {5, 4, 3, 2};   // C1, C2, C3, C4 단자가 연결된 아두이노 핀 번호
 
Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );
 
void setup() {
  pinMode(motion,INPUT); 
  pinMode(inte,OUTPUT); 
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600);
}
   
void loop() {  


  digitalWrite(trig, LOW);
  digitalWrite(echo, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  
  unsigned long duration = pulseIn(echo, HIGH);
 
  // 초음파의 속도는 초당 340미터를 이동하거나, 29마이크로초 당 1센치를 이동합니다.
  // 따라서, 초음파의 이동 거리 = duration(왕복에 걸린시간) / 29 / 2 입니다.
  float distance = duration / 29.0 / 2.0;
 
  // 측정된 거리 값를 시리얼 모니터에 출력합니다.
  Serial.print(distance);
  Serial.println("cm");
 
  
  // 적외선 인체감지 센서에서 값을 읽는다
  int sensor = digitalRead(motion);
  // 센서값을 시리얼 모니터에 출력
  Serial.println("senser = "); 
  Serial.println(sensor);
//  if (sensor == HIGH) { 
//    digitalWrite(inte,HIGH);
//    Serial.println("in");
//    char pw[4] = {' ',' ',' ',' '};
//    int i=0;
//        while(i<4){
//          char key = keypad.getKey();
//          if(key){
//            pw[i] = key;
//            Serial.println(pw[i++]);
//          }
//        }
//      delay(500);
//    }
    delay(500);
    digitalWrite(inte,LOW);
    delay(500);
}
