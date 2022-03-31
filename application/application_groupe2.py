

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
import face
import PIL
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import Tk, Text, BOTH, W, N, E, S
from PIL import ImageTk, Image
from tkinter import filedialog as fd
import cv2
import argparse
import sys
import time
import os
import tensorflow.compat.v1 as tf 

import tensorflow.compat.v1 as tf  # compatibility mode of tf1 in tf2

physical_devices=tf.config.list_physical_devices('GPU')

allowedUser = ["Sidi", "Pierre", "Aurelie", "Sedrick", "Tarik", "Francois", "Axel", "Belarbi"]

authentifie=None


def add_overlays(frame, faces, frame_rate, ok):
	names=[]
	authentifie=0
	if faces is not None:
		for face in faces:
			if face.name is not None:
				if face.name in allowedUser:                                            # Green
					ok += 1
					if (ok==50):
						print ("Congratulations, you are well authentified")
						authentifie=1
			face_bb = face.bounding_box.astype(int)
			cv2.rectangle(frame,
			(face_bb[0], face_bb[1]), (face_bb[2], face_bb[3]),
			(0, 255, 0), 2)
			if face.name is not None:
				cv2.putText(frame, face.name, (face_bb[0], face_bb[3]),
				cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
				thickness=2, lineType=2)

	cv2.putText(frame, str(frame_rate) + " fps", (10, 30),
	cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
	thickness=2, lineType=2)
	return ok, authentifie



class AccueilPage(tk.Frame):
	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)

		load = Image.open("assets/image_1.png")
		photo = ImageTk.PhotoImage(load)
		label = tk.Label(self, image=photo)
		label.image = photo
		label.place(x=0, y=0, width=1300.0, height=866.0)

		#border = tk.LabelFrame(self, text='Login', bg='ivory', bd=10, font=("Arial", 20))
		#border.pack(fill="both", expand="yes", padx=150, pady=150)

		Label = tk.Label(self,
				 text="Welcome !",
				 bg="white", font=("Arial Bold", 25), borderwidth=2, bd=2, relief="groove", justify='center')
		Label.place(x=300, y=30, width=200)



		load = Image.open("assets/image_7.png")
		resize_image = load.resize((120, 50))
		photo1 = ImageTk.PhotoImage(resize_image)
		label = tk.Label(self, image=photo1)
		label.image = photo1
		label.place(x=650, y=10)


		Button = tk.Button(self, bg='#BD0E3A', text="Connexion", font=("Arial", 15), command=lambda: os.system('python /home/ilia/HackIA22_Input/Edge_AI_Module/EdgeAI_Smart.py'))
		Button.place(x=300.0, y=120.0, width=200.0, height=60.0)
		Button2 = tk.Button(self, bg='#BD0E3A', text="Inscription", font=("Arial", 15))
		Button2.place(x=300.0, y=220.0, width=200.0, height=60.0)
		Button3 = tk.Button(self, bg='#BD0E3A', text="Quitter", font=("Arial", 15),
				   command=lambda: self.destroy())
		Button3.place(x=300.0, y=320.0, width=200.0, height=60.0)

		load = Image.open("assets/image_2.png")
		resize_image = load.resize((135, 50))
		photo1 = ImageTk.PhotoImage(resize_image)
		label = tk.Label(self, image=photo1)
		label.image = photo1
		label.place(x=25, y=410)

		load = Image.open("assets/image_3.png")
		resize_image = load.resize((135, 50))
		photo1 = ImageTk.PhotoImage(resize_image)
		label = tk.Label(self, image=photo1)
		label.image = photo1
		label.place(x=175, y=410)

		load = Image.open("assets/image_4.png")
		resize_image = load.resize((135, 50))
		photo1 = ImageTk.PhotoImage(resize_image)
		label = tk.Label(self, image=photo1)
		label.image = photo1
		label.place(x=330, y=410)

		load = Image.open("assets/image_5.png")
		resize_image = load.resize((135, 50))
		photo1 = ImageTk.PhotoImage(resize_image)
		label = tk.Label(self, image=photo1)
		label.image = photo1
		label.place(x=495, y=410)

		load = Image.open("assets/image_6.png")
		resize_image = load.resize((135, 50))
		photo1 = ImageTk.PhotoImage(resize_image)
		label = tk.Label(self, image=photo1)
		label.image = photo1
		label.place(x=650, y=410)

	def authentification():
		frame_interval = 3  # Number of frames after which to run face detection
		fps_display_interval = 5  # seconds
		frame_rate = 0
		frame_count = 0
		face_count=0
		ok = 0
		#video_capture = cv2.VideoCapture("video.mp4")
		video_capture = cv2.VideoCapture(0)
		face_recognition = face.Recognition()
		start_time = time.time()
		authentifie=0
		while (ok < 50):
			# Capture frame-by-frame
			ret, frame = video_capture.read()
			frame = cv2.resize(frame, (640,480), interpolation=cv2.INTER_AREA)
			if (frame_count % frame_interval) == 0:
	    			faces = face_recognition.identify(frame)

	    			# Check our current fps
	    			end_time = time.time()
			if (end_time - start_time) > fps_display_interval:
				frame_rate = int(frame_count / (end_time - start_time))
				start_time = time.time()
				frame_count = 0

			ok, authentifie=add_overlays(frame, faces, frame_rate, ok)
			print(authentifie)
			frame_count += 1
			cv2.imshow('Video', frame)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break


		# When everything is done, release the capture
		video_capture.release()
		cv2.destroyAllWindows()

		return authentifie

		



class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        
        frame = AccueilPage(window, self)
        self.frames[AccueilPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(AccueilPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")




if __name__ == '__main__':
	tf.disable_v2_behavior()  # compatibility mode of tf1 in tf2
	# allow gpu g
	
	gpus = tf.config.experimental.list_physical_devices('GPU')
	if gpus:
		try:
			for gpu in gpus:
				tf.config.experimental.set_memory_growth(gpu, True)
		except RuntimeError as e:
			print(e)
    
	app = Application()
	#app.geometry("800x500")
	#app.configure(bg = "#FFFFFF")
	app.mainloop()

	

