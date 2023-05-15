from requests import get, post
from time import sleep
import json

name = "" #minecraft name
WEBHOOK_URL = ""

def Discord(hours):
    global WEBHOOK_URL
    
    data = {
        "content" : f"Connected in {hours}",
        "username" : "2b2t",
        "avatar_url" : "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/IronException_2b2t_Spawn_Render_July_2019.png/220px-IronException_2b2t_Spawn_Render_July_2019.png"}

    r = post(WEBHOOK_URL, data = data)

    if r.status_code != 204:
        print("Error while sending discord webhook:", r.text)

def Main():
    global name
    connected = False
    minutes = 0
    
    while not connected:
        if get("https://api.2b2t.dev/status").json()[1][0] != 0:
            players = [str(i) for i in list(get("https://api.2b2t.dev/status").json()[1][0])]

            if name not in players:
                print("Not connected yet (counting", str(minutes), "minutes since the start)")
            
            else:
                connected = True
    
            sleep(60)
            minutes += 1
        else:
            print("API/Server offline (counting", str(minutes), "minutes since the start)")
            sleep(60)
            minutes += 1

    hours = str(minutes // 60) + "h" + str(minutes - (minutes // 60) * 60) + "m"
    print("Connected in", hours)
    Discord(hours)

if __name__ == "__main__":
    Main()
    
