from requests import get
from time import sleep
import json

name = "" #minecraft name

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

if __name__ == "__main__":
    Main()
    
