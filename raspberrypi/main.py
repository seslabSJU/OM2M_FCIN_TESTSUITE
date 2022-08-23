import setting
import interact
import onem2m
import jsonmodule as jm
import logging
import json

logging.basicConfig(filename='../info.log', filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s [%(filename)s]: %(name)s %(funcName)20s - Message: %(message)s')


def setColor(json, r, g, b):
    json["red"] = r
    json["green"] = g
    json["blue"] = b
    return True


if __name__ == "__main__":
    body = jm.get_secret("body")["UPDATE"]["color"]
    setting.settingFlexContainer()
    input("Enter for continue...")
    while True:
        read = interact.readSerial()
        if read[0] == "U":
            if read == "U Red":
                setColor(body["hd:color"], 255, 0, 0)
            elif read == "U Green":
                setColor(body["hd:color"], 0, 255, 0)
            elif read == "U Blue":
                setColor(body["hd:color"], 0, 0, 255)
            onem2m.updateFlexContainer(body, "/Light/Color")
            print("Update LED Color")
        elif read[0] == "R":
            res = json.loads(onem2m.retrieveFlexContainer("/Light/Color"))
            try:
                if int(res["hd:color"]["m2m:fcin"][-1]["red"]) == 255: led = "1"
                elif int(res["hd:color"]["m2m:fcin"][-1]["green"]) == 255: led = "2"
                elif int(res["hd:color"]["m2m:fcin"][-1]["blue"]) == 255: led = "3"
                else: led = "0"
            except KeyError:
                led = "0"
            interact.writeSerial(led)
            print("Retrieve LED Color: " + led)
        else:
            print(read)
            continue