"""
Created on 07.10.2023
@author: mat-eng
@description: generate .exe
"""
########################################################################################################################
# Import libraries
import os
import shutil

########################################################################################################################
# Application version
app_name = "Timelapse Tool "
app_version = "v004"
app = app_name + app_version

########################################################################################################################
if __name__ == "__main__":
    print("Starting compilation of main executable... Can take several minutes...")

    # Remove dist folder before building new executable
    if os.path.exists("./dist"):
        shutil.rmtree('./dist')

    # Build main exe file
    os.system("pyinstaller main.py  --clean --onefile --noconfirm --noconsole "
              "--hidden-import pyqtgraph.graphicsItems.ViewBox.axisCtrlTemplate_pyqt5 "
              "--hidden-import pyqtgraph.graphicsItems.PlotItem.plotConfigTemplate_pyqt5 "
              "--hidden-import pyqtgraph.imageview.ImageViewTemplate_pyqt5")

    # Rename exe
    os.rename("./dist/main.exe", "./dist/" + app + ".exe")

    # Remove folder created during exe generation
    shutil.rmtree('./build')

    # Remove file created during exe generation
    os.remove("./main.spec")
