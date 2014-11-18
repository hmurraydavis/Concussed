#include <SoftwareSerial.h>

//Declare globals:
char current_line[8]; // allocate some space for the string
int yellow=A2;
int green=A1;
int red=A0;

void setup(){
	Serial.begin(9600);
        pinMode(red, OUTPUT);
        pinMode(yellow,OUTPUT);
        pinMode(green, OUTPUT);
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

void windDirection(){
	Serial.print("$d45\n");
}

void compassRead(){
	Serial.println("$c66");
}

void loop() {  
    
    //Serial.println(current_line);
    //Serial.println("$hoi");   
	read_line(current_line);
    int amount;

    switch (current_line[0]){
        case 'q': // compass 
                digitalWrite(green, HIGH);
                Serial.println("Greem light on");
        	break;
        case 'a':
        	digitalWrite(red, HIGH);
                Serial.println("red light on");
        	break;
        case 'z':
                digitalWrite(yellow,HIGH);
                Serial.println("Yellow light on");
                break;
        case 'w':
                digitalWrite(green, LOW);
                Serial.println("Green light off");
        	break;
        case 's':
                digitalWrite(red, LOW);
                Serial.println("Red light off");
        	break;
        case 'x':
                digitalWrite(yellow, LOW);
                Serial.println("Yellow light off");
        	break;
        case '/n':
        	break;
	}
}
