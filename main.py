import requests
import json
# import time
from pynasonic_ptz import PTZCamera

#  CAMERA IP ADDRESSES
cam1 = PTZCamera.PTZCamera(address='192.168.0.170')
cam2 = PTZCamera.PTZCamera(address='192.168.0.171')
cam3 = PTZCamera.PTZCamera(address='192.168.0.172')
cam4 = PTZCamera.PTZCamera(address='192.168.0.173')
cam5 = PTZCamera.PTZCamera(address='192.168.0.174')
cam6 = PTZCamera.PTZCamera(address='192.168.0.175')
cam1.enabled = "Enabled"
cam2.enabled = "Enabled"
cam3.enabled = "Enabled"
cam4.enabled = "Disabled"
cam5.enabled = "Disabled"
cam6.enabled = "Disabled"

# GLOBAL VARIABLES
cameraActive = "Active"
micStateChange = 'MicrophoneState'
micStateOn = '"State":"On"'
micStateOff = '"State":"Off"'
seatNumber = "0"
micsActive = []
totalMics = 15
programQuit = False
response_json = ""

# CAMERA VARIABLES
cam1IP = "192.168.0.170"
cameraIPAddress = ["192.168.0.170", "192.168.0.171"]
cameraIP = ""
camPreset = "02"
camera_url = "http://" + cameraIP + "/cgi-bin/aw_ptz?cmd=%23R" + camPreset + "&res=1"
camera_home = "http://" + cameraIP + "/cgi-bin/aw_ptz?cmd=%23R00&res=1"
# cam1home = cam1.moveToPreset(preset_index=99)


# INITIALIZE THE SYSTEM AND CONNECT TO TELEVIC
def initialize():
    global api_url
    api_url = "http://192.168.0.150:8890/CoCon/Connect"
    response = requests.get(api_url)
    response.json()
    print(response.json())
    apiID = response.json()[22:58]
    api_url = "http://192.168.0.150:8890/CoCon/Notification/id=" + apiID
    print(api_url)


# UPDATE CAMERA POSITION FUNCTION
def camUpdate():
    global cameraActive
    for i in range(1, 7):
        cam = globals().get(f"cam{i}")
        if len(micsActive) >= 1 and cam.enabled == "Enabled":
            cameraActive = "Active"
            cam.moveToPreset(preset_index=int(micsActive[0]) + - 1)
            cam2.moveToPreset(preset_index=int(micsActive[0]) + - 1)
            cam3.moveToPreset(preset_index=int(micsActive[0]) + - 1)
        # cam4.moveToPreset(preset_index=int(micsActive[0]) + - 1)
        # cam5.moveToPreset(preset_index=int(micsActive[0]) + - 1)
        # cam6.moveToPreset(preset_index=int(micsActive[0]) + - 1)

        if not micsActive and cam.enabled == "Enabled":
            cameraActive = "Inactive"
            print("No microphones Active")
            cam.moveToPreset(preset_index=99)  # ACTUALLY PRESET 100, STARTS COUNT AT 00


def startProgram():
    global response_json
    global micsActive
    while True:

        # time.sleep(.1)
        response = requests.get(api_url)
        response.json()
        #print (response.json())
        # cam1.moveToPreset(preset_index=0)

        if micStateChange in response.json():
            response_json = response.json()
            data = json.loads(response_json)
            speakers_array = data["MicrophoneState"]["Speakers"]
            print (speakers_array)
            micsActive = speakers_array

            # if micsActive.count (speakers_array[-1]) < 1:
            #     micsActive.append(speakers_array[-1])
            #     print (micsActive)
            # elif micsActive.count (speakers_array[-1]) >= 1:
            #     micsActive.remove(speakers_array[-1])
            # for i in speakers_array:
            #     print (i)

                   # micsActive.append(response.json()[i])

            #print("Mic State Change =", response.json()[32])

            #micsActive.append(response.json()[32])
            #print("State =", response.json()[56:58])
            camUpdate()
            continue

        # elif micStateOff in response.json():
        #     print("Seat Number =", response.json()[45])
        #     micsActive.remove(response.json()[45])
        #     print("State =", response.json()[56:59])
        #     cameraActive = "Inactive"
        #     #camUpdate()
        #     continue

        elif programQuit:
            exit()
            break





# MAIN PROGRAM LOOP:

#initialize()
#startProgram()
