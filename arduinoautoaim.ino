#include <Servo.h>

Servo xServo;
Servo yServo;

void setup() {
  Serial.begin(9600); // Start serial communication at 9600 baud
  xServo.attach(9);   // Attach the x-axis servo to pin 9
  yServo.attach(10);  // Attach the y-axis servo to pin 10
  
}

void loop() {
  if (Serial.available()) { // if the serial data is available 
    String inputString = Serial.readStringUntil('\n'); // read the string until '\n'
    

    // These two variables are taken from the string, send from python code 
    int xValue = inputString.substring(0, inputString.indexOf(',')).toInt();
    // xValue is the value {x} from f"{x},{y}\n
    int yValue = inputString.substring(inputString.indexOf(',') + 1).toInt();
    // yValue is the value {y}from f"{x},{y}\n
    
    // Map the values to servo angles
    int xAngle = map(xValue, 0, 600, 160, 0); // Adjust mapping range 
    int yAngle = map(yValue, 0, 500, 180, 0); // Adjust mapping range 
    
    // Write the mapped angles to the servos
    xServo.write(xAngle);
    yServo.write(180 - yAngle); // I did it opposite way for mechanical reason 
  }
}
