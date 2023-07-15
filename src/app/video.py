import cv2
import numpy as np
from PIL import ImageTk, Image


class Video:
    def __init__(self, path: str):
        self.videoCap = cv2.VideoCapture(path, apiPreference=cv2.CAP_FFMPEG)

        if not self.videoCap.isOpened():
            raise Exception("Read video failed")

    def getFirstFrame(self, width: int, height: int) -> ImageTk.PhotoImage:
        _, image = self.videoCap.read()
        (h, w) = image.shape[:2]
        ratio = w / width

        if w / h <= width / height:
            # image width is bigger than label width (ratio)
            imageResize = cv2.resize(image, (width, int(h / ratio)))
        else:
            imageResize = cv2.resize(image, (int(w / ratio), height))

        imageRGB = cv2.cvtColor(imageResize, cv2.COLOR_BGR2RGB)

        result = ImageTk.PhotoImage(Image.fromarray(imageRGB))

        return result

    def cropVideo(self, sX: int, sY: int, eX: int, eY: int):
        pass
