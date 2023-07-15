import tkinter as tk
import tkinter.font as tkFont
import pathlib
import numpy as np
from tkinter.filedialog import askopenfilename
from video import Video
from PIL import ImageTk, Image


class App:
    def __init__(self, root: tk.Tk):
        srcPath = pathlib.Path(__file__).parent.parent.resolve()
        iconPath = srcPath.joinpath("assets/icon.png")
        root.iconphoto(False, tk.PhotoImage(file=iconPath))

        root.title("FCASA")
        width = 520
        height = 420
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignStr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        root.geometry(alignStr)
        root.resizable(width=False, height=False)

        btnFile = tk.Button(root)
        btnFile["bg"] = "#efefef"
        btnFile["font"] = tkFont.Font(family="Times", size=10)
        btnFile["fg"] = "#000000"
        btnFile["justify"] = "center"
        btnFile["text"] = "Select File"
        btnFile.place(x=20, y=20, width=122, height=39)
        btnFile["command"] = self.doSelectFile

        labPreview = tk.Label(root)
        labPreview["font"] = tkFont.Font(family="Times", size=16)
        labPreview["fg"] = "#333333"
        labPreview["justify"] = "center"
        labPreview["text"] = "Image Preview Area"
        labPreview.place(x=20, y=70, width=481, height=254)

        btnReset = tk.Button(root)
        btnReset["bg"] = "#aa0000"
        btnReset["font"] = tkFont.Font(family="Times", size=10)
        btnReset["fg"] = "#ffffff"
        btnReset["justify"] = "center"
        btnReset["text"] = "RESET"
        btnReset.place(x=20, y=340, width=70, height=25)
        btnReset["command"] = self.doReset

        btnSetA = tk.Button(root)
        btnSetA["bg"] = "#efefef"
        btnSetA["font"] = tkFont.Font(family="Times", size=10)
        btnSetA["fg"] = "#000000"
        btnSetA["justify"] = "center"
        btnSetA["text"] = "Set A point"
        btnSetA.place(x=270, y=340, width=70, height=25)
        btnSetA["command"] = self.doSetAPoint

        btnSetB = tk.Button(root)
        btnSetB["bg"] = "#efefef"
        btnSetB["font"] = tkFont.Font(family="Times", size=10)
        btnSetB["fg"] = "#000000"
        btnSetB["justify"] = "center"
        btnSetB["text"] = "Set B point"
        btnSetB.place(x=350, y=340, width=70, height=25)
        btnSetB["command"] = self.doSetBPoint

        btnStart = tk.Button(root)
        btnStart["bg"] = "#efefef"
        btnStart["font"] = tkFont.Font(family="Times", size=10)
        btnStart["fg"] = "#000000"
        btnStart["justify"] = "center"
        btnStart["text"] = "Start"
        btnStart.place(x=430, y=340, width=70, height=25)
        btnStart["command"] = self.doStart

        labStatus = tk.Label(root)
        labStatus["font"] = tkFont.Font(family="Times", size=12)
        labStatus["anchor"] = "w"
        labStatus.place(x=20, y=380, width=500, height=30)

        self.btnFile = btnFile
        self.btnReset = btnReset
        self.btnSetA = btnSetA
        self.btnSetB = btnSetB
        self.btnStart = btnStart
        self.labPreview = labPreview
        self.labStatus = labStatus
        self.selectedFilePath: str = ""
        self.ptA: tuple[int, int] = (0, 0)
        self.ptB: tuple[int, int] = (0, 0)
        self.videoObject: Video
        self.image: ImageTk.PhotoImage

        self.updateStatus()

    def doSelectFile(self):
        filename = askopenfilename(
            title="Select Video File",
            defaultextension=".mp4",
            filetypes=[
                ("MP4 Video", ".mp4"),
                ("MPEG Video", ".mpeg"),
                ("WEBM Video", ".webm"),
                ("AVI Video", ".avi"),
                ("All Files", ".*"),
            ],
        )

        if filename:
            self.selectedFilePath = filename
            print(filename)

            self.updateStatus("Reading File...")

            try:
                self.videoObject = Video(filename)
            except Exception as e:
                self.updateStatus(
                    f"Failed to read file, maybe the file you selected is not a valid video file?",
                    "#ff0000",
                )
            else:
                self.image = self.videoObject.getFirstFrame(self.labPreview.winfo_width(), self.labPreview.winfo_height())
                
                self.labPreview.config(image=self.image)
                self.updateStatus()

    def doReset(self):
        self.selectedFilePath = ""
        self.labPreview.config(image="")

    def doSetAPoint(self):
        print("command")

    def doSetBPoint(self):
        print("command")

    def doStart(self):
        print("command")

    def updateStatus(self, message: str = "Ready", colorHex: str = "#000000"):
        self.labStatus["text"] = message

        if colorHex != "":
            self.labStatus["fg"] = colorHex


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
