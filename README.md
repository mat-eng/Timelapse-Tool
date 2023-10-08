# Timelapse Tool
***

# Description
Timelapse Tool is a simple GUI to build video Timelapse from pictures. It uses moviepy.

# Step by step guide
## 1. Folder selection
First choose the folder that contains all the pictures for the Timelapse. Note that all pictures should have the same resolution.

## 2. Add a music (optional)
You can optionally add a background music for the Timelapse (mp3 file supported).

## 3. Define the Timelapse duration
Choose the duration of the Timelapse by adjusting the cursor.
### Minimum duration
The minimum duration is 1 second.
### Maximum duration
The maximum duration is defined by the total number of pictures available and the frame rate (30fps hardcoded in script, see Notes below).
For example, the maximum duration with 900 pictures is: 900pictures/30fps = 30 seconds.
### Intermediate duration
If the chosen duration is smaller than the maximum duration, some frames (pictures) will be jumped.
For example, if duration is set at 10 seconds with 900 pictures available, then only 1 picture out of 3 will be used.

## 4. Build Timelapse
Click on Build Timelapse and wait for the process to finish.

## 5. Open Timelapse
Once the process is finished, you can click on Open Timelapse to open the resulting video. Timelapse is automatically saved on same path as the script/executable location. 

# Notes
Frame rate is fixed at 30fps in the script. It can be increased at processing time/resources cost.