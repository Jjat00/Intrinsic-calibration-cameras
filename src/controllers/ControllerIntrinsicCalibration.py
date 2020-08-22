from PySide2 import *
import glob
from IntrinsicAcquisitionWidget import *
from Actions import *


class ControllerIntrinsicCalibration():
    def __init__(self, window):
        super(ControllerIntrinsicCalibration).__init__()
        self.window = window
        self.action = Actions(self.window)
        self.whichImage = 0
        self.loadPatter = False
        self.save = False

    def handlerAcquisitionImage(self):
        intrinsicWidget = IntrinsicAcquisitionWidget()
        intrinsicWidget.exec()

    def handlerLoadPatternImages(self):
        pathImages = self.action.selectDirectoryImages()
        self.patternImages = glob.glob(pathImages+"/*.png")
        self.totalImagesCalibration = len(self.patternImages)
        self.action.showImage(self.patternImages[0])
        self.loadPatter = True
        self.showCurrentImage()

    def handlerStartCalibration(self):
        if self.loadPatter:
            self.action.startIntrinsicCalibration(self.patternImages)
            self.patternImages = self.action.getPatternImage()
            self.save = True
            self.whichImage = 0
            self.showCurrentImage()

    def handlerSaveParameters(self):
        if self.save:
            self.action.saveDialog()

    def handlerClearWorkspace(self):
        self.action.clearWorkspace()
        self.action.resetParameters()
        self.loadPatter = False
        self.save = False
        self.patternImages = []
        self.whichImage = 0
        self.window.currentImageLabel.setText('0 / 0')
        self.window.progressBarIntrsc.setValue(0)

    def handlerPreviousParameters(self):
        if self.loadPatter:
            if (self.whichImage > 0):
                self.action.clearWorkspace()
                self.whichImage = self.whichImage - 1
                self.action.showImage(
                    self.patternImages[self.whichImage])
                self.showCurrentImage()

    def handlerNextParameters(self):
        if self.loadPatter:
            if (self.whichImage < self.totalImagesCalibration-1):
                self.action.clearWorkspace()
                self.whichImage = self.whichImage + 1
                self.action.showImage(
                    self.patternImages[self.whichImage])
                self.showCurrentImage()

    def showCurrentImage(self):
        self.currentImage = str(self.whichImage) + \
            ' / ' + str(self.totalImagesCalibration-1)
        self.window.currentImageLabel.setText(self.currentImage)
