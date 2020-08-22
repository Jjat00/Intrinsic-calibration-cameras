"""
File: IntrinsicCalibrationWidget.py
Author: Jaimen Aza <<Jjat userjjar00@gmail.com>>
Date create: 19-august-2020
Last moditication date : 21-august-2020
"""

import sys
import os

dirs = ['views', 'styles', 'controllers', 'models',
        'components/AcquisitionIntrinsicCalibration/src']

for nameDir in dirs:
    path = os.path.join(sys.path[0], nameDir)
    sys.path.append(path)

import cv2
from PySide2 import *
from StylesIntrinsicCalibration import *
from ViewIntrinsicCalibration import *

class IntrinsicCalibrationWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(IntrinsicCalibrationWidget, self).__init__(*args, **kwargs)
        self.loadForm()
        self.viewIntrinsicCalibration = ViewIntrinsicCalibration(self.window)
        self.initUI()
        StylesIntrinsicCalibration(self)

    def initUI(self):
        self.setWindowTitle("Intrinsic Calibration")
        self.setGeometry(300, 100, 810, 560)
        self.connectButtons()

    def loadForm(self):
        formUI = os.path.join(sys.path[0], 'views/intrinsicCalibration.ui')
        file = QtCore.QFile(formUI)        
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)

    def connectButtons(self):
        self.viewIntrinsicCalibration.connectAcqButton()
        self.viewIntrinsicCalibration.connectLoadButton()
        self.viewIntrinsicCalibration.connectStartButton()
        self.viewIntrinsicCalibration.connectSaveButton()
        self.viewIntrinsicCalibration.connectPreviousButton()
        self.viewIntrinsicCalibration.connectNextButton()
        self.viewIntrinsicCalibration.connectClearButton()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    acquisitionExtrinsicCalibration = IntrinsicCalibrationWidget()
    acquisitionExtrinsicCalibration.show()
    app.exec_()
