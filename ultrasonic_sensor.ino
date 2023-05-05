#include <NewPing.h>  // Including the relavent library 

// Initialising trig and echo pins 
#define TRIGGER_PIN 7
#define ECHO_PIN 6

// Defining a new variable, with the max distance in cm of the sensor
#define MAX_DISTANCE 150

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // Inputting the relavent informatoin to form the object 'sonar'

// Defining each of the four vibration motors a variable name and also defining the pin it is connected to on the Arduino Nano
int motor_1 = 2;
int motor_2 = 3;
int motor_3 = 4;
int motor_4 = 5;

void setup() {
  // Setting the vibration motors' pins as output pins 
  pinMode(motor_1, OUTPUT);
  pinMode(motor_2, OUTPUT);
  pinMode(motor_3, OUTPUT);
  pinMode(motor_4, OUTPUT);

  Serial.begin(9600); // Initialisaing serial communication 
}

void loop() {
  delay(50); // Ultrasonic sensor taking readings every 50milliseconds
  // Following lines of code calls the ping_cm() function of the sonar object to obtain the 
  // distance in cm, this measurement is then stored in the distance variable
  int distance = sonar.ping_cm();

  Serial.println(distance); // printing the distance to serial monitor in order to be plotted 
  // in the serial plotter
  
  // A an if statement is implemented to distinguish which range the distance falls into. Accordingly,
  // the number of vibration motors 'on' (high) or 'off' (low) at any one time is varied.
  if (distance == 0) {
    // No motors should be vibrating
    digitalWrite(motor_1, LOW);
    digitalWrite(motor_2, LOW);
    digitalWrite(motor_3, LOW);
    digitalWrite(motor_4, LOW);
  }
   else if (distance > MAX_DISTANCE) {
     // No motors should be vibrating 
    digitalWrite(motor_1, LOW);
    digitalWrite(motor_2, LOW);
    digitalWrite(motor_3, LOW);
    digitalWrite(motor_4, LOW);
  } 
  else if (distance < 50) {
    // All four motors should vibrate
    digitalWrite(motor_1, HIGH);
    digitalWrite(motor_2, HIGH);
    digitalWrite(motor_3, HIGH);
    digitalWrite(motor_4, HIGH);
  } 
  else if (distance < 75) {
    // The first three motors should vibrate
    digitalWrite(motor_1, HIGH);
    digitalWrite(motor_2, HIGH);
    digitalWrite(motor_3, HIGH);
    digitalWrite(motor_4, LOW);
  } 
  else if (distance < 100) {
    // The first two motors should vibrate
    digitalWrite(motor_1, HIGH);
    digitalWrite(motor_2, HIGH);
    digitalWrite(motor_3, LOW);
    digitalWrite(motor_4, LOW);
  } 
  else if (distance < 150) {
    // Only the first motors should vibrate
    digitalWrite(motor_1, HIGH);
    digitalWrite(motor_2, LOW);
    digitalWrite(motor_3, LOW);
    digitalWrite(motor_4, LOW);
  }

  // In order to keep the y-axis of the serial plotter consistent, lines are drawn at y=0 and y = 150, 
  // alongisde the continuous distance measurements that are being detected from the ultrasonic sensor.
  Serial.print(0);
  Serial.print(",");
  Serial.print(150);
  Serial.print(",");

}