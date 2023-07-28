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
cam1.enabled = "Disabled"
cam2.enabled = "Disabled"
cam3.enabled = "Disabled"
cam4.enabled = "Enabled"
cam5.enabled = "Enabled"
cam6.enabled = "Enabled"

# GLOBAL VARIABLES
global televicIP
televicIP = "192.168.0.150"
cameraActive = "Inactive"
micStateChange = 'MicrophoneState'
micStateOn = '"State":"On"'
micStateOff = '"State":"Off"'
seatNumber = "0"
micsActive = []
totalMics = 15
programQuit = False
response_json = ""
programPaused = True

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
    api_url = "http://"+televicIP+":8890/CoCon/Connect"
    response = requests.get(api_url)
    response.json()
    print(response.json())
    apiID = response.json()[22:58]
    api_url = "http://"+televicIP+":8890/CoCon/Notification/id=" + apiID
    print(api_url)


# UPDATE CAMERA POSITION FUNCTION
def camUpdate():
    global cameraActive
    for i in range(1, 7):
        cam = globals().get(f"cam{i}")

        if len(micsActive) >= 1 and cam.enabled == "Enabled" and cameraActive == "Inactive":
            cameraActive = "Active"
            #cam.moveToPreset(preset_index=int(micsActive[0]) + - 1)
            #cam2.moveToPreset(preset_index=int(micsActive[0]) + - 1)
            #cam3.moveToPreset(preset_index=int(micsActive[0]) + - 1)
            cam4.moveToPreset(preset_index=int(micsActive[0]) + - 1)
            cam5.moveToPreset(preset_index=int(micsActive[0]) + - 1)
            cam6.moveToPreset(preset_index=int(micsActive[0]) + - 1)

        # elif len(micsActive) >= 1 and cam.enabled == "Enabled" and cameraActive == "Active":
        #     print("Cameras currently active")

        elif not micsActive and cam.enabled == "Enabled":
            cameraActive = "Inactive"
            print("No microphones Active")
            cam.moveToPreset(preset_index=99)  # ACTUALLY PRESET 100, STARTS COUNT AT 00


def update_micsActive(current_state):
    global micsActive
    global cameraActive
    # Create a copy of the current state to compare with the previous state
    new_state = current_state.copy()

    # Check for newly added microphones (turned on)
    new_microphones = [mic for mic in new_state if mic not in micsActive]
    if new_microphones:
        print("Microphones turned on:", new_microphones)
        micsActive.extend(new_microphones)
        print("micsActive=", micsActive)
        camUpdate()

    # Check for removed microphones (turned off)
    removed_microphones = [mic for mic in micsActive if mic not in new_state]
    if removed_microphones:
        # print("micsActive=",micsActive)
        # print("cameraActive=",cameraActive)
        print("Microphones turned off:", removed_microphones)
        # print("micsActive[0]=", micsActive[0])
        if removed_microphones[0] == micsActive[0]:
            cameraActive = "Inactive"
            # print(cameraActive)
        micsActive = [mic for mic in micsActive if mic in new_state]
        print("micsActive=", micsActive)
        camUpdate()
        # print("micsActive NOW =",micsActive)


def startProgram():
    global response_json
    global micsActive
    while programPaused == True:

        # time.sleep(.1)
        response = requests.get(api_url)
        response.json()
        # print (response.json())
        # cam1.moveToPreset(preset_index=0)

        if micStateChange in response.json():
            response_json = response.json()
            data = json.loads(response_json)
            speakers_array = data["MicrophoneState"]["Speakers"]
            # print (speakers_array)
            # micsActive = speakers_array
            update_micsActive(speakers_array)
            # camUpdate()
            continue

        elif programQuit:
            exit()
            break





# MAIN PROGRAM LOOP:

# initialize()
# startProgram()
