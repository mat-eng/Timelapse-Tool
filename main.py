"""
Created on 07.10.2023
@author: mat-eng
@description: simple GUI to build Timelapse from pictures folder
"""
########################################################################################################################
# Import libraries
import os
import sys
import io
import threading
import cv2
import moviepy.editor as mp
import fnmatch
import datetime
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import main_window
import GenerateExe

########################################################################################################################
EXE_BUILD = True
# False:  everything is printed on console (sys.stderr, sys.stdout and app log)
# True: sys.stderr and sys.stdout is redirected to be use for Timelapse build progress on GUI, app log only on GUI


########################################################################################################################
class LauncherDialog(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        main_window.Ui_MainWindow.__init__(self)

        self.music_file = ''
        self.duration = 1
        self.folder = ''
        self.jpg_counter = 0
        self.frame_rate = 30
        self.timelapse_file = ''

        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.pushButton_folderSelection.clicked.connect(pushButton_folderSelection)
        self.pushButton_musicSelection.clicked.connect(pushButton_musicSelection)
        self.pushButton_build.clicked.connect(pushButton_build)

        self.horizontalSlider_duration.valueChanged.connect(horizontalSlider_duration)

        self.pushButton_openTimelapse.clicked.connect(pushButton_openTimelapse)

        self.log.textChanged.connect(refresh_log)

    def closeEvent(self, event):
        event.accept()


########################################################################################################################
# Init section
def init_window():
    # Section 1
    win.pushButton_folderSelection.setEnabled(True)

    # Section 2
    win.pushButton_musicSelection.setEnabled(False)

    # Section 3
    win.label_1.setEnabled(False)
    win.horizontalSlider_duration.setEnabled(False)
    win.label_duration.setEnabled(False)

    # Section 4
    win.pushButton_build.setEnabled(False)
    win.log.setEnabled(False)
    win.progressBar.setEnabled(False)

    # Section 5
    win.pushButton_openTimelapse.setEnabled(False)


########################################################################################################################
# Section 1 - pictures folder selection
def pushButton_folderSelection():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    options &= ~(QFileDialog.ShowDirsOnly)
    win.folder = QFileDialog.getExistingDirectory(options=options)

    if win.folder != '':
        win.folder = win.folder + '/'
        log("Folder: "+win.folder)

        win.jpg_counter = len(fnmatch.filter(os.listdir(win.folder), '*.jpg*'))
        log("Number of pictures: " + str(win.jpg_counter))

        # Section 1
        win.pushButton_folderSelection.setEnabled(True)

        # Section 2
        win.pushButton_musicSelection.setEnabled(True)

        # Section 3
        win.label_1.setEnabled(True)
        win.horizontalSlider_duration.setEnabled(True)
        win.label_duration.setEnabled(True)
        win.horizontalSlider_duration.setMinimum(1)
        win.horizontalSlider_duration.setMaximum(win.jpg_counter / win.frame_rate)
        win.label_duration.setText("Duration: 00:00:01 (hh:mm:ss)")

        # Section 4
        win.pushButton_build.setEnabled(True)
        win.log.setEnabled(True)
        win.progressBar.setEnabled(True)

        # Section 5
        win.pushButton_openTimelapse.setEnabled(False)


########################################################################################################################
# Section 2 - music file selection
def pushButton_musicSelection():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    win.music_file, _ = QFileDialog.getOpenFileName(win, "Open", "", "hex (*.mp3)" , options=options)

    if win.music_file != '':
        log("Music file: " + win.music_file)


########################################################################################################################
# Section 3 - desired Timelapse duration selection
def horizontalSlider_duration():
    win.duration = win.horizontalSlider_duration.value()
    hours = int(win.duration / 3600)
    minutes = int((win.duration % 3600) / 60)
    seconds = int((win.duration % 3600) % 60)
    win.label_duration.setText("Duration: "+"{:02d}".format(hours)+":"+"{:02d}".format(minutes)+":"+"{:02d}".format(seconds)+" (hh:mm:ss)")


########################################################################################################################
# Section 4 - build
def pushButton_build(self):
    # Section 1
    win.pushButton_folderSelection.setEnabled(False)

    # Section 2
    win.pushButton_musicSelection.setEnabled(False)

    # Section 3
    win.label_1.setEnabled(False)
    win.horizontalSlider_duration.setEnabled(False)
    win.label_duration.setEnabled(False)

    # Section 4
    win.pushButton_build.setEnabled(False)
    win.log.setEnabled(True)
    win.progressBar.setEnabled(True)
    win.progressBar.setValue(0)

    # Section 5
    win.pushButton_openTimelapse.setEnabled(False)

    QApplication.setOverrideCursor(Qt.WaitCursor)

    t0 = threading.Thread(target=build_video_thread)
    t0.start()

    while t0.is_alive():
        QApplication.processEvents()
        time.sleep(0.5)

        if EXE_BUILD == True:
            progress_text = buffer_stderr.getvalue()
            progress_sub = "t:"

            # All occurrences of substring in string
            res = [i for i in range(len(progress_text)) if progress_text.startswith(progress_sub, i)]

            if res:
                size = len(res)
                value = res[size-1]

                progress = int(buffer_stderr.getvalue()[value+3:value+6])
                win.progressBar.setValue(progress)
    t0.join()

    QApplication.restoreOverrideCursor()

    # Section 1
    win.pushButton_folderSelection.setEnabled(True)

    # Section 2
    win.pushButton_musicSelection.setEnabled(True)

    # Section 3
    win.label_1.setEnabled(True)
    win.horizontalSlider_duration.setEnabled(True)
    win.label_duration.setEnabled(True)

    # Section 4
    win.pushButton_build.setEnabled(True)
    win.log.setEnabled(True)
    win.progressBar.setEnabled(True)
    win.progressBar.setValue(100)

    # Section 5
    win.pushButton_openTimelapse.setEnabled(True)

    log("SUCCESS ! You can now open the Timelapse by clicking below on '5. Open Timelapse'")


def build_video_thread():
    # Loop through list of pictures and append them to our pictures list
    sorted_dir = os.listdir(win.folder)

    # Get resolution of first picture as info
    first_img = cv2.imread(os.path.join(win.folder, sorted_dir[0]))
    size = first_img.shape
    res_y = size[0]
    res_x = size[1]
    log("Pictures resolution: " + str(res_x) + "x" + str(res_y))

    # Create list of pictures with full path
    my_list = [win.folder + x for x in sorted_dir]

    # Define jump size depends on: number of pictures, desired duration and frame rate
    jump = int(win.jpg_counter / (win.duration * win.frame_rate))

    # Create new list with only pictures that will be used, depending on jump size
    my_new_list = []
    j = 0
    for i in my_list:
        if j % jump == 0:
            my_new_list.append(i)
        j = j + 1

    log("Building sequence... it may take a while...")
    video = mp.ImageSequenceClip(my_new_list, fps=win.frame_rate)

    if win.music_file != '':
        log("Music added to sequence")
        audioclip = mp.AudioFileClip(win.music_file)
        music = mp.afx.audio_loop(audioclip, duration=video.duration)
        video = video.set_audio(music)

    # Build final video
    save_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    log("Building final video timelapse-"+save_time+".mp4")
    video.write_videofile(f"./timelapse-{save_time}.mp4")
    win.timelapse_file = "timelapse-"+save_time+".mp4"

    video.close()
    if win.music_file != '':
        audioclip.close()
        music.close()


########################################################################################################################
# Section 5 - open Timelapse
def pushButton_openTimelapse():
    os.startfile(win.timelapse_file)


########################################################################################################################
# Log section
def log(text):
    win.log.append(">"+text)
    win.log.append("")
    if EXE_BUILD == False:
        print(text)


def refresh_log():
    win.log.verticalScrollBar().setValue(win.log.verticalScrollBar().maximum())


########################################################################################################################
# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    win = LauncherDialog()
    win.setWindowTitle(GenerateExe.app)
    win.show()

    # If building exe, stderr and stdout need to be redirected to be use for Timelapse build progress on GUI
    if EXE_BUILD == True:
        sys.stderr = buffer_stderr = io.StringIO()
        sys.stdout = buffer_stdout = io.StringIO()

    init_window()

    sys.exit(app.exec_())
