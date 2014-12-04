#include <SoftwareSerial.h>

#define GREEN 3
#define BLUE 5
#define RED 6
#define delayTime 20

char current_line[16]; // allocate some space for the string

/* RGB LED code taken from a tutorial by cyragia:
http://www.instructables.com/id/Fading-RGB-LED-Arduino/?ALLSTEPS 
and modified by hmurraydavis */

void setup() {

  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
  pinMode(RED, OUTPUT);
  digitalWrite(GREEN, HIGH);
  digitalWrite(BLUE, HIGH);
  digitalWrite(RED, HIGH);
  
  int redVal;
  int blueVal;
  int greenVal;
  Serial.begin(9600);
}

void read_line(char *line) {
    // read characters from serial into line until a newline character
    char c;
    int index;
    for (index = 0; index < 5; index++) {
        // wait until there is a character
        while (Serial.available() == 0);
        // read a character
        c = Serial.read();
        if (c == '\n') {
            break;
        } else {
            line[index] = c;
        }
    }
    // terminate the string
    line[index] = '\0';
}

int get_amount(char *line) {
    // return the number in a string such as "r1200" as an int
    int amount;
    amount = (int) strtol(line+1, NULL, 10);
    return amount;
}


int redV(){
    char redChar[3];
    for (int index = 2; index < 5; index++) {
       redChar[index-2] = current_line[index]; 
    }
    redChar[3]='\0';
    Serial.println("Out of loop: ");
    Serial.println(redChar);
    int red = atol(redChar); //, NULL, 5);
    Serial.println(red);
    return red;
}

void writeColorToLED(int redVal, int greenVal, int blueVal) {
/*
Writes color to RGB LEDs
String format: 
    n#rrrgggbbb where:
        n is the character "n" denoting the start of a new string
        # is the number of the desired chanel
        rrr is three characters representing the value for the red chanel
        ggg is three characters representing the value for the green chanel
        bbb is three characters representing the value for the blue chanel
*/
    analogWrite( GREEN, 255 - greenVal );
    analogWrite( RED, 255 - redVal );
    analogWrite( BLUE, 255 - blueVal );
}


 
void loop() {

    read_line(current_line);
    if (current_line[0]=='n'){
        redV();
    }
    writeColorToLED(100,100,100);
  /*
  int redVal = 255;
  int blueVal = 0;
  int greenVal = 0;
  for( int i = 0 ; i < 255 ; i += 1 ){
    greenVal += 1;
    redVal -= 1;
    analogWrite( GREEN, 255 - greenVal );
    analogWrite( RED, 255 - redVal );

    delay( delayTime );
  }
 
  redVal = 0;
  blueVal = 0;
  greenVal = 255;
  for( int i = 0 ; i < 255 ; i += 1 ){
    blueVal += 1;
    greenVal -= 1;
    analogWrite( BLUE, 255 - blueVal );
    analogWrite( GREEN, 255 - greenVal );

    delay( delayTime );
  }
 
  redVal = 0;
  blueVal = 255;
  greenVal = 0;
  for( int i = 0 ; i < 255 ; i += 1 ){
    redVal += 1;
    blueVal -= 1;
    analogWrite( RED, 255 - redVal );
    analogWrite( BLUE, 255 - blueVal );

    delay( delayTime );
  }
  */
}
