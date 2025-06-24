import websocket
import json
import threading

def on_message(ws, message):
    data = json.loads(message)
    print("Received:", json.dumps(data, indent=2))

def on_error(ws, error):
    print("WebSocket error:", error)

def on_close(ws, close_status_code, close_msg):
    print("Disconnected from PSX Terminal")

def on_open(ws):
    print("Connected to PSX Terminal")
    
    # Subscribe to market data for REG market
    subscription = {
        "type": "subscribe",
        "subscriptionType": "marketData",
        "params": {
            "marketType": "REG"
        },
        "requestId": "req-001"
    }
    
    ws.send(json.dumps(subscription))

# Connect to PSX Terminal WebSocket
ws = websocket.WebSocketApp("wss://psxterminal.com/",
                          on_open=on_open,
                          on_message=on_message,
                          on_error=on_error,
                          on_close=on_close)

ws.run_forever()