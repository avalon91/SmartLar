/*
 Basic ESP8266 MQTT example

 This sketch demonstrates the capabilities of the pubsub library in combination
 with the ESP8266 board/library.

 It connects to an MQTT server then:
  - publishes "hello world" to the topic "outTopic" every two seconds
  - subscribes to the topic "inTopic", printing out any messages
    it receives. NB - it assumes the received payloads are strings not binary
  - If the first character of the topic "inTopic" is an 1, switch ON the ESP Led,
    else switch it off

 It will reconnect to the server if the connection is lost using a blocking
 reconnect function. See the 'mqtt_reconnect_nonblocking' example for how to
 achieve the same result without blocking the main loop.

 To install the ESP8266 board, (using Arduino 1.6.4+):
  - Add the following 3rd party board manager under "File -> Preferences -> Additional Boards Manager URLs":
       http://arduino.esp8266.com/stable/package_esp8266com_index.json
  - Open the "Tools -> Board -> Board Manager" and click install for the ESP8266"
  - Select your ESP8266 in "Tools -> Board"

*/

#include <IRremoteESP8266.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

IRsend irsend(4);
unsigned int Signal_Desliga22_1[] = {3428,1672,520,1196,540,1176,544,332,544,344,516,356,540,1156,536,360,540,344,544,1156,560,1172,540,332,520,1192,560,328,696,260,440,1200,536,1192,512,356,520,1200,540,1156,536,368,520,352,544,1172,544,328,544,344,544,1156,560,332,540,332,520,368,520,356,544,328,544,328,548,348,516,356,540,332,520,352,520,368,544,332,544,332,520,356,540,348,540,332,544,324,548,328,544,344,544,332,520,1192,548,312,560,344,520,1200,512,1200,544,332,640,248,540,332,516,352,520,356,624,264,520,1200,540,328,544,332,520,1212,512,360,544,328,544,328,520,368,520,356,520,1196,620,252,520,368,544,332,544,332,516,356,520,368,520,352,544,332,544,328,520,372,516,356,544,328,544,328,544,344,544,332,544,332,520,352,544,348,540,332,516,356,516,356,520,368,544,332,520,356,540,332,520,368,544,328,544,332,620,228,572,1188,540,332,544,332,512,360,544,344,516,356,516,356,544,332,544,344,544,1172,516,1180,536,352,548,344,516,356,520,328,576,1164,520,1208,512}; //AnalysIR Batch Export (IRremote) - RAW
unsigned int Signal_Liga22_0[] = {3424,1680,524,1192,520,1192,524,352,520,368,520,352,520,1196,520,356,544,344,520,1192,524,1192,524,352,516,1212,524,352,516,356,520,1196,520,1212,516,352,524,1192,524,1192,520,368,524,352,520,1196,520,352,496,396,492,1220,520,352,524,352,520,368,524,352,520,352,520,352,524,368,524,352,524,352,516,356,520,368,520,356,520,352,520,352,500,388,500,376,520,356,516,1200,520,368,516,352,524,1192,524,352,520,368,524,1192,520,1196,544,328,524,364,524,352,516,356,520,356,520,368,520,1196,520,352,520,356,516,1212,520,352,500,376,520,356,516,372,516,356,520,1192,552,324,520,368,520,356,520,356,516,356,520,368,520,352,524,352,524,348,520,368,500,376,520,356,520,352,496,392,520,352,524,352,524,352,516,372,516,356,520,356,520,352,520,368,524,348,520,356,520,356,544,344,516,360,516,356,520,352,520,1212,524,352,520,356,516,356,520,368,548,324,524,352,520,356,516,372,496,1220,516,1196,520,1196,520,368,520,352,548,328,516,1200,520,1200,524}; //AnalysIR Batch Export (IRremote) - RAW
int khz=38;

// Update these with values suitable for your network.

const char* ssid = "LAR-ECT";
const char* password = "senhafacil1234";
const char* mqtt_server = "10.6.1.112";

WiFiClient espClient;
PubSubClient client(espClient);
//long lastMsg = 0;
//char msg[50];
int value = 0;

void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == 'l') {
    irsend.sendRaw(Signal_Liga22_0, sizeof(Signal_Liga22_0)/sizeof(int), khz); //AnalysIR Batch Export (IRremote) - RAW
    digitalWrite(2, LOW);   // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is acive low on the ESP-01)
  } else {
    irsend.sendRaw(Signal_Desliga22_1, sizeof(Signal_Desliga22_1)/sizeof(int), khz); //AnalysIR Batch Export (IRremote) - RAW
    digitalWrite(2, HIGH);  // Turn the LED off by making the voltage HIGH
  }

}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    //String clientId = "ESP8266Client-";
    //clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect("ESP-J", "esp", "senhaesp")) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      //client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe("/ac1");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup() {
  irsend.begin();
  pinMode(2, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  digitalWrite(2, HIGH);
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  /*long now = millis();
  if (now - lastMsg > 2000) {
    lastMsg = now;
    ++value;
    snprintf (msg, 75, "hello world #%ld", value);
    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish("outTopic", msg);
  }*/
}
