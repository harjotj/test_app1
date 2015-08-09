#!/usr/bin/python
import dweepy
from pubnub import Pubnub
import json
with open('/usr/share/funstore/funstore/api/InfoAPI.json') as data_file:
    data = json.load(data_file)
def callback(message):
     print(message)

WLAccess=data[1]["access"]
PubNubAccess=data[0]["access"]
DweetAccess=data[2]["access"]

def Dweet(namevar, var):
        thingname=data[2]["fields"][1]["data"]
        dweepy.dweet_for(thingname, {namevar: var})

