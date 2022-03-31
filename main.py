# code base from https://solarianprogrammer.com/2018/04/21/python-opencv-show-video-tkinter-window/

import sys
import time
import tkinter
import PIL
from PIL import Image, ImageTk
import cv2


class App:
    def __init__(self, window, title, source=0):
        self.photo = None
        self.window = window
        self.window.title(title)
        self.source = source

        self.video = VideoCapture(self.source)

        self.canvas = tkinter.Canvas(window, width=self.video.width, height=self.video.height)
        self.canvas.pack()

        self.button_snapshot = tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
        self.button_snapshot.pack(anchor=tkinter.CENTER, expand=True)

        self.delay = 30
        self.update()

        self.window.mainloop()

    def snapshot(self):
        ret, frame = self.video.get_frame()
        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update(self):
        ret, frame = self.video.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        self.window.after(self.delay, self.update)


class VideoCapture:
    def __init__(self, source=0):
        self.video = cv2.VideoCapture(source)
        if not self.video.isOpened():
            raise ValueError("Unable to open video source", source)

        self.width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.video.isOpened():
            ret, frame = self.video.read()
            if ret:
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                return ret, None
        else:
            return False, None

    def __del__(self):
        if self.video.isOpened():
            self.video.release()


def main() -> int:
    App(tkinter.Tk(), "EdgeAI")
    return 0


if __name__ == '__main__':
    sys.exit(main())
