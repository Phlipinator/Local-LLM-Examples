import time

import network
import ujson
import urequests

# ====== USER CONFIGURABLE VARIABLES ======
SSID = ""  # WiFi SSID
PASSWORD = ""  # WiFi Password

# API endpoint URL
API_URL = "http:XXX.XXX.XXX.XX:1234/v1/chat/completions"  # Replace with your local IP 

# Request data
REQUEST_DATA = {
    "model": "XXXX",  # Replace with your model name
    "messages": [{"role": "user", "content": "Tell me a joke!"}], # For Reference: https://platform.openai.com/docs/api-reference/responses/create
    "max_tokens": 50
}

# =========================================

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        time.sleep(1)
    print("Connected to WiFi:", wlan.ifconfig())

def send_request():

    headers = {
        "Content-Type": "application/json"
    }

    try:
        print("Sending request to:", API_URL)
        response = urequests.post(API_URL, headers=headers, data=ujson.dumps(REQUEST_DATA))
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
