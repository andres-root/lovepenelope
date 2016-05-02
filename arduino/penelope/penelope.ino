/*
Penélope
Adriana Marmorek

By: Andrés Luján y Karo Ladino
*/

#include <SPI.h>
#include <Ethernet.h>
#include <SoftwareSerial.h>
#include <ArduinoJson.h>

SoftwareSerial Thermal(5, 6);
// Enter a MAC address for your controller below.
// Newer Ethernet shields have a MAC address printed on a sticker on the shield
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
// if you don't want to use DNS (and reduce your sketch size)
// use the numeric IP instead of the name for the server:
//IPAddress server(74,125,232,128);  // numeric IP for Google (no DNS)
char server[] = "lovefrompenelope.herokuapp.com";    // name address for Google (using DNS)

int heatTime = 80;
int heatInterval = 255;
char printDensity = 15;
char printBreakTime = 15;
//int 3,5,8 
int zero=0;
boolean connected = false;

// Set the static IP address to use if the DHCP fails to assign
IPAddress ip(192, 168, 0, 177);

// Initialize the Ethernet client library
// with the IP address and port of the server
// that you want to connect to (port 80 is default for HTTP):
EthernetClient client;

void setup() {
  pinMode(3, OUTPUT); //Twitter
    pinMode(9, OUTPUT); // Printing
      pinMode(8, OUTPUT); //Shredder
       
  // Open serial communications and wait for port to open:
  Serial.begin(57600);
  Thermal.begin(19200); // to write to our new printer
  initInternet();
  initPrinter();

}

void initInternet() {
  // start the Ethernet connection:
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
    // try to congifure using IP address instead of DHCP:
    Ethernet.begin(mac, ip);
  }
  // give the Ethernet shield a second to initialize:
  delay(1000);
  Serial.println("connecting...");

  // if you get a connection, report back via serial:
  if (client.connect(server, 80)) {
    Serial.println("connected");
    connected = true;
  } else {
    // if you didn't get a connection to the server:
    Serial.println("connection failed");
    Thermal.println("I can't find you love");
    connected = false;
    Thermal.write(10);
    Thermal.write(10);
    Thermal.write(10);
  }  
}

void initPrinter()
{
 //Modify the print speed and heat
 Thermal.write(27);
 Thermal.write(55);
 Thermal.write(7); //Default 64 dots = 8*('7'+1)
 Thermal.write(heatTime); //Default 80 or 800us
 Thermal.write(heatInterval); //Default 2 or 20us
 //Modify the print density and timeout
 Thermal.write(18);
 Thermal.write(35);
 int printSetting = (printDensity<<4) | printBreakTime;
 Thermal.write(printSetting); //Combination of printDensity and printBreakTime
 Serial.println("Printer ready");
 Thermal.println("Where are you, love?");
 Thermal.println("Adriana Marmorek");
 Thermal.write(10);
 Thermal.write(10);
}

void loop() {
  // if there are incoming bytes available
  // from the server, read them and print them:
  // Make a HTTP request:

  if (connected) {
   digitalWrite(3, HIGH);
   delay(1000);
   digitalWrite(3, LOW); 
   delay(1000);
   digitalWrite(3, HIGH);
   delay(1000);
   digitalWrite(3, LOW); 

    client.println("GET / HTTP/1.1");
    client.println("Content-Type: application/json;charset=utf-8");
    client.println("Host: lovefrompenelope.herokuapp.com");
    client.println("Connection: keep-alive");
    client.println();
    String tweet = ""; ///-
    boolean read = false; ///- 
    while (client.available()) {
      char c = client.read();
      if (c == '{') {
        read = true;
      } 
//    else if (c == '}') {
//      read = false;
//    }
      if (read == true) {
        tweet += c;
      }
    }
// tweet += "}";
  Serial.println(tweet);
  Serial.println(tweet.length());
    //char json[300];
  //tweet.toCharArray(json, 300);
  StaticJsonBuffer<400> jsonBuffer;
  JsonObject& root = jsonBuffer.parseObject(tweet);
  const char* name = root["name"];
  const char* user = root["user"];
  const char* text = root["text"];
  const char* date = root["date"];
  
  String header = "";
  Serial.println(name);
  Serial.println(user);
  Serial.println(text);
  Serial.println(date);
   
   
   // Name and date
   Thermal.println(name);
   Thermal.write(27);
   Thermal.write(45);
   Thermal.write(1);
   Thermal.println(date);
  
   // User and text
   Thermal.write(27); 
   Thermal.write(45);
   Thermal.write(zero);
   Thermal.println(user); //31 caracteres, 
   Thermal.println(text); //31 caracteres, 
   Thermal.write(10);
   Thermal.write(10);
   Thermal.write(10);
   digitalWrite(9, HIGH); 
   delay(1000);
   digitalWrite(9, LOW); 

//Shredder
  delay(5000);
   digitalWrite(8, HIGH); 
   delay(2000);
   digitalWrite(8, LOW); 
//Waiting   
  delay(45000);
     
    if (!client.connected()) {
    Serial.println();
    Serial.println("disconnecting.");
    client.stop();
    initInternet();
   }    
  } else {
    initInternet();
  }

}
