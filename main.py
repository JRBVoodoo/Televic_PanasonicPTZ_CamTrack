import requests
# import time
from pynasonic_ptz import PTZCamera

#  CAMERA IP ADDRESSES
cam1 = PTZCamera.PTZCamera(address='192.168.0.170')
cam2 = PTZCamera.PTZCamera(address='192.168.0.171')
cam3 = PTZCamera.PTZCamera(address='192.168.0.172')
cam4 = PTZCamera.PTZCamera(address='192.168.0.173')
cam5 = PTZCamera.PTZCamera(address='192.168.0.174')
cam6 = PTZCamera.PTZCamera(address='192.168.0.175')


# GLOBAL VARIABLES
cameraActive = "Active"
micStateOn = '"State":"On"'
micStateOff = '"State":"Off"'
seatNumber = "0"
micsActive = []
totalMics = 15

# CAMERA VARIABLES
cam1IP = "192.168.0.170"
cameraIPAddress = ["192.168.0.170", "192.168.0.171"]
cameraIP = ""
camPreset = "02"
camera_url = "http://" + cameraIP + "/cgi-bin/aw_ptz?cmd=%23R" + camPreset + "&res=1"
camera_home = "http://" + cameraIP + "/cgi-bin/aw_ptz?cmd=%23R00&res=1"
# cam1home = cam1.moveToPreset(preset_index=99)


# INITIALIZE THE SYSTEM AND CONNECT TO TELEVIC
api_url = "http://localhost:8890/CoCon/Connect"
response = requests.get(api_url)
response.json()
print(response.json())
apiID = response.json()[22:58]
api_url = "http://localhost:8890/CoCon/Notification/id=" + apiID
print(api_url)


# UPDATE CAMERA POSITION FUNCTION
def camUpdate():
    global cameraActive
    if len(micsActive) >= 1 and cameraActive == "Inactive":
        # print (micsActive)
        cameraActive = "Active"
        cam1.moveToPreset(preset_index=int(micsActive[0]) + - 1)
        # cam2.moveToPreset(preset_index=int(micsActive[0]) + - 1)
        # cam3.moveToPreset(preset_index=int(micsActive[0]) + - 1)
        # cam4.moveToPreset(preset_index=int(micsActive[0]) + - 1)
        # cam5.moveToPreset(preset_index=int(micsActive[0]) + - 1)
        # cam6.moveToPreset(preset_index=int(micsActive[0]) + - 1)

    if not micsActive:
        cameraActive = "Inactive"
        print("No microphones Active")
        cam1.moveToPreset(preset_index=99)  # ACTUALLY PRESET 100, STARTS COUNT AT 00


# LOOP TO CONSTANTLY UPDATE WHEN MICS ARE ACTIVATED
while True:

    # time.sleep(.1)
    response = requests.get(api_url)
    response.json()
    # cam1.moveToPreset(preset_index=0)

    if micStateOn in response.json():
        print("Seat Number =", response.json()[45])
        micsActive.append(response.json()[45])
        print("State =", response.json()[56:58])
        camUpdate()
        continue

    elif micStateOff in response.json():
        print("Seat Number =", response.json()[45])
        micsActive.remove(response.json()[45])
        print("State =", response.json()[56:59])
        cameraActive = "Inactive"
        camUpdate()
        continue

# if micsActive == "1":
# 	print (camera_url)
# 	response = requests.get(camera_url)
# 	continue

# elif micsActive == 0:
# 	print (camera_home)
# 	response = requests.get(camera_home)
# 	continue


# # response = requests.get(camera_url)
# # print (response)
