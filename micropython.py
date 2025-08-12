import time

import network
import ujson
import urequests

# WiFi credentials
SSID = ""
PASSWORD = ""

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        time.sleep(1)
    print("Connected to WiFi:", wlan.ifconfig())

def send_request():
    url = "http://xxx.xxx.xxx.xx:1234/v1/chat/completions"  # Replace with your PC's local IP
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": "local-model", 
        "messages": [{"role": "user", "content": "Tell me a joke!"}],
        "max_tokens": 50
    }

    try:
        print("Sending request to:", url)
        response = urequests.post(url, headers=headers, data=ujson.dumps(data))
        json_data = response.json()  # Convert response to a Python dictionary
        response.close()  # Always close the response to free memory

        # Extract assistant response
        if "choices" in json_data and len(json_data["choices"]) > 0:
            ai_response = json_data["choices"][0]["message"]["content"]
            print("AI Response:", ai_response)
        else:
            print("Error: No response from model")

    except Exception as e:
        print("Request failed:", e)

connect_wifi()
send_request()
