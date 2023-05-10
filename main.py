# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import time
import random

from simple_ai import *
from uart import *
from Adafruit_IO import MQTTClient

AIO_FEED_IDs = ["button1", "button2"]
AIO_USERNAME = "QuanNguyen1"
AIO_KEY = "aio_qHHW56OvtNdo4LpdyL34fCgxxZoK"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + ", feed id:" + feed_id)
    if feed_id == "button1":
        if payload == "0":
            writeData("1")
        else:
            writeData("2")
    if feed_id == "button2":
        if payload == "0":
            writeData("3")
        else:
            writeData("4")

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
sensor_type = 0
counter_ai = 5
ai_result = ""
previous_result = ""
while True:
    # counter = counter - 1
    # if counter <= 0:
    #     counter = 10
    #     #TODO
    #     print("random data is publishing...")
    #     if sensor_type == 0:
    #         print("Temperature...")
    #         temp = random.randint(10,20)
    #         client.publish("sensor1",temp)
    #         sensor_type = 1
    #     elif sensor_type == 1:
    #         print("Humidity...")
    #         humi = random.randint(50,70)
    #         client.publish("sensor2",humi)
    #         sensor_type = 2
    #     elif sensor_type == 2:
    #         print("Light...")
    #         light = random.randint(100,500)
    #         client.publish("sensor-3",light)
    #         sensor_type = 0

    counter_ai = counter_ai - 1
    if counter_ai <= 0:
        counter_ai = 5
        previous_result = ai_result
        ai_result = image_detector()
        print("AI output :", ai_result)
        if previous_result != ai_result:
            client.publish("ai", ai_result)

    readSerial(client)
    time.sleep(1)
    #pass
