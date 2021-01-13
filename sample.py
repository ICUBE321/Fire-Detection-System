import http.client
import urllib.request, urllib.parse, urllib.error
import time
key = "LP1T78H3I4WXETW4"  # Put your API Key here

# from 1pm - 2pm, the chances of a fire is very high

def detector():
    fire = 0
    fireStatus = "Green"
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        temp = 28 #int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        humidity = 45

        # preferred relative humidity for burning varies from 30 to 55 percent
        #ignition temperature is 300 degree Celsius
        if temp < 300:
            if humidity > 55:
                fire = 0
                fireStatus = "Green"
            elif humidity < 30: 
                fire = 0.75
                fireStatus = "Orange"
            else :
                fire = 0.25
                fireStatus = "Yellow"
        elif temp > 300 : 
            fire = 1
            fireStatus = "Red"

        params = urllib.parse.urlencode({'field1': temp, 'field2': humidity, 'field4': fire, 'key':key }) # channel field info for thingspeak
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80") # defining thingspeak connection

        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse() 
            print(temp, humidity, fireStatus)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
            
        except:
            print("connection failed") 
        break
if __name__ == "__main__":
        while True:
                detector()
                time.sleep(5) # loops every 5 secs
