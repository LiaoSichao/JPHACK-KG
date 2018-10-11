from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog as tkFileDialog
import cv2
import huniki_change
from tkinter import ttk

pop_1 = [239,145,169]
pop_2 = [254,238,153]
pop_3 = [135, 178, 223]
modern_1 = [159,159,159]
modern_2 = [33,25,22]
modern_3 = [0,125,140]
relax_1 = [255,248,202]
relax_2 = [218,166,119]
relax_3 = [162,136,119]
speed_1 = [35,25,23]
speed_2 = [255,255,255]
speed_3 = [10,93,169]
roman_1 = [210,198,222]
roman_2 = [255,255,255]
roman_3 = [210,235,240]
fresh_1 = [185,215,117]
fresh_2 = [255,248,202]
fresh_3 = [35,181,160]

def select_image():
	global panelA
	global path
	print("画像を選んでください")
	path = tkFileDialog.askopenfilename()
	print(path)
	if len(path) > 0:
		img = cv2.imread(path)
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		img = Image.fromarray(img)
		img = ImageTk.PhotoImage(img)
		if panelA is None:
			panelA = Label(image = img)
			panelA.image = img
			#panelA.pack(side="left", padx=10, pady=10)
			panelA.grid(row=2,column=0,padx=5, pady=5)
		else:
			panelA.configure(image=img)
			panelA.image = img


def change_modern(color_base1, color_base2, color_base3):
	global panelB, path
	if len(path) > 0:
		img = cv2.imread(path)
		height, width = img.shape[:2]
		image_change = huniki_change.change(img, height, width, color_base1, color_base2, color_base3)
		image_change = cv2.cvtColor(image_change, cv2.COLOR_BGR2RGB)
		image_change = Image.fromarray(image_change)
		image_change = ImageTk.PhotoImage(image_change)
		if panelB is None:
			panelB = Label(image = image_change)
			panelB.image = image_change
			#panelB.pack(side="right", padx=10, pady=10)
			panelB.grid(row=2,column=1,padx=5, pady=5)
		else:
			panelB.configure(image=image_change)
			panelB.image = image_change

def change_pop(color_base1, color_base2, color_base3):
	global panelB, path
	print ("kawaii")
	if len(path) > 0:
		img = cv2.imread(path)
		height, width = img.shape[:2]
		image_change = huniki_change.change(img, height, width, color_base1, color_base2, color_base3)
		image_change = cv2.cvtColor(image_change, cv2.COLOR_BGR2RGB)
		image_change = Image.fromarray(image_change)
		image_change = ImageTk.PhotoImage(image_change)
		if panelB is None:
			panelB = Label(image = image_change)
			panelB.image = image_change
			#panelB.pack(side="right", padx=10, pady=10)
			panelB.grid(row=2,column=1,padx=5, pady=5)
		else:
			panelB.configure(image=image_change)
			panelB.image = image_change

def change_relax(color_base1, color_base2, color_base3):
	global panelB, path
	if len(path) > 0:
		img = cv2.imread(path)
		height, width = img.shape[:2]
		image_change = huniki_change.change(img, height, width, color_base1, color_base2, color_base3)
		image_change = cv2.cvtColor(image_change, cv2.COLOR_BGR2RGB)
		image_change = Image.fromarray(image_change)
		image_change = ImageTk.PhotoImage(image_change)
		if panelB is None:
			panelB = Label(image = image_change)
			panelB.image = image_change
			#panelB.pack(side="right", padx=10, pady=10)
			panelB.grid(row=2,column=1,padx=5, pady=5)
		else:
			panelB.configure(image=image_change)
			panelB.image = image_change

def change_speed(color_base1, color_base2, color_base3):
	global panelB, path
	if len(path) > 0:
		img = cv2.imread(path)
		height, width = img.shape[:2]
		image_change = huniki_change.change(img, height, width, color_base1, color_base2, color_base3)
		image_change = cv2.cvtColor(image_change, cv2.COLOR_BGR2RGB)
		image_change = Image.fromarray(image_change)
		image_change = ImageTk.PhotoImage(image_change)
		if panelB is None:
			panelB = Label(image = image_change)
			panelB.image = image_change
			#panelB.pack(side="right", padx=10, pady=10)
			panelB.grid(row=2,column=1,padx=5, pady=5)
		else:
			panelB.configure(image=image_change)
			panelB.image = image_change

def change_roman(color_base1, color_base2, color_base3):
	global panelB, path
	if len(path) > 0:
		img = cv2.imread(path)
		height, width = img.shape[:2]
		image_change = huniki_change.change(img, height, width, color_base1, color_base2, color_base3)
		image_change = cv2.cvtColor(image_change, cv2.COLOR_BGR2RGB)
		image_change = Image.fromarray(image_change)
		image_change = ImageTk.PhotoImage(image_change)
		if panelB is None:
			panelB = Label(image = image_change)
			panelB.image = image_change
			#panelB.pack(side="right", padx=10, pady=10)
			panelB.grid(row=2,column=1,padx=5, pady=5)
		else:
			panelB.configure(image=image_change)
			panelB.image = image_change

def change_fresh(color_base1, color_base2, color_base3):
	global panelB, path
	if len(path) > 0:
		img = cv2.imread(path)
		height, width = img.shape[:2]
		image_change = huniki_change.change(img, height, width, color_base1, color_base2, color_base3)
		image_change = cv2.cvtColor(image_change, cv2.COLOR_BGR2RGB)
		image_change = Image.fromarray(image_change)
		image_change = ImageTk.PhotoImage(image_change)
		if panelB is None:
			panelB = Label(image = image_change)
			panelB.image = image_change
			#panelB.pack(side="right", padx=10, pady=10)
			panelB.grid(row=2,column=1,padx=5, pady=5)
		else:
			panelB.configure(image=image_change)
			panelB.image = image_change

root = Tk()
panelA = None
panelB = None
path = ""

def callback_pop():
	result = change_pop(pop_1, pop_2, pop_3)

def callback_modern():
	result = change_modern(modern_1, modern_2, modern_3)

def callback_relax():
	result = change_relax(relax_1, relax_2, relax_3)

def callback_speed():
	result = change_speed(speed_1, speed_2, speed_3)

def callback_roman():
	result = change_roman(roman_1, roman_2, roman_3)

def callback_fresh():
	result = change_fresh(fresh_1, fresh_2, fresh_3)


icon1 = PhotoImage(file='pop.png')
icon2 = PhotoImage(file='modern.png')
icon3 = PhotoImage(file='relax.png')
icon4 = PhotoImage(file='speedy.png')
icon5 = PhotoImage(file='romantic.png')
icon6 = PhotoImage(file='fresh.png')
icon7 = PhotoImage(file='choice.png')
frame1 = ttk.Frame(
    root,
    padding=5)
frame1. grid()


button1 = ttk.Button(
    frame1,
    image=icon1,
    text='ポップ',
    compound=TOP,
    command=callback_pop)
button1. grid(row=1,column=1,padx=10, pady=10)
#button1.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")


button2 = ttk.Button(
    frame1,
    image=icon2,
    text='モダン',
    compound=TOP,
    command=callback_modern)
button2. grid(row=1,column=2,padx=10, pady=10)

button3 = ttk.Button(
    frame1,
    image=icon3,
    text='リラックス',
    compound=TOP,
    command=callback_relax)
button3. grid(row=1,column=3,padx=10, pady=10)

button4 = ttk.Button(
    frame1,
    image=icon4,
    text='スピーディ',
    compound=TOP,
    command=callback_speed)
button4. grid(row=1,column=4,padx=10, pady=10)

button5 = ttk.Button(
    frame1,
    image=icon5,
    text='ロマンチック',
    compound=TOP,
    command=callback_roman)
button5. grid(row=1,column=5,padx=10, pady=10)

button6 = ttk.Button(
    frame1,
    image=icon6,
    text='フレッシュ',
    compound=TOP,
    command=callback_fresh)
button6. grid(row=1,column=6,padx=10, pady=10)

#button7= Button(root, text="Select an image"  ,command=select_image)
button7 = ttk.Button(
    frame1,
    image=icon7,
    text='選択',
    compound=TOP,
    command=select_image)
button7. grid(row=1,column=7,padx=10, pady=10)


root.mainloop()
