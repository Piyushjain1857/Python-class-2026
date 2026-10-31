#include <Servo.h>

Servo myServo;
void setup() {
myServo.attach(6); // signal wire on Pin 6
}
void loop() {
for (int angle = 0; angle <= 180; angle++) {
myServo.write(angle);
delay(15);
}
for (int angle = 180; angle >= 0; angle--) {
myServo.write(angle);
delay(15);
}
}

