#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include "nosync.h"

const char *mqclientid ="espmq";
const char *mqtopic="esp32a/alive";

WiFiClient espClient;
PubSubClient client(espClient);

void cbMqtt(char *topic, byte *payload, unsigned int length);

void setup() {
    // initialize communication
    Serial.begin(9600);
    WiFi.begin(ssid,pass);
    while(WiFi.status()!=WL_CONNECTED){
        delay(500);
        Serial.println("Connecting to wifi...");
    }
    Serial.println("Connecetd to wifi");
    client.setServer(mqaddr,mqport);
    client.setCallback(cbMqtt);
    while (!client.connected()) {
        String client_id = "esp32-client-";
        client_id += String(WiFi.macAddress());
        Serial.printf("The client %s connects to the public MQTT broker\n", client_id.c_str());
        if (client.connect(mqclientid)) {
            Serial.println("Public EMQX MQTT broker connected");
        } else {
            Serial.print("failed with state ");
            Serial.print(client.state());
            delay(2000);
        }
    }
    // Publish and subscribe
    //client.publish(mqtopic, "Hi, I'm ESP32 ^^");
    //client.subscribe(topic);
    
}

void loop() {
    //delay(1000);
    //Serial.print("hello\n");
    client.loop();
    delay(5000);
    client.publish(mqtopic, "Hi, I'm ESP32 ^^");
    
}

void cbMqtt(char *topic, byte *payload, unsigned int length)
{
    Serial.print("Message arrived in topic: ");
    Serial.println(topic);
    Serial.print("Message:");
    for (int i = 0; i < length; i++) { Serial.print((char) payload[i]); }
    Serial.println();
    Serial.println("-----------------------");
}