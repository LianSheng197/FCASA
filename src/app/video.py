import cv2
import numpy as np


class Video:
    def __init__(self, path: str):
        self.videoCap = cv2.VideoCapture(path, apiPreference=cv2.CAP_FFMPEG)

        if not self.videoCap.isOpened():
            raise Exception("Read video failed")
        
        

    def getFirstFrame(self):
        pass

    def cropVideo(self, sX: int, sY: int, eX: int, eY: int):
        pass
