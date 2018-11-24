from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from time import sleep
from datetime import datetime
from random import randint
import sys

sys.setrecursionlimit(100000000)

w = 800
h = 520
code = -1
attempts = 0
attcount = 247

def f3():
	dt = datetime.now()
	rnd = randint(1, 26)
	return ("1547-\n6" + str(567 - attcount + attempts), dt.strftime("%Y-%m-%d") + "\n" + dt.strftime("%H:%M-%S"), rnd, round(rnd / 0.27))

def f2(a):
	if a == "\n":
		return "<Return>"
	elif a == " ":
		return "<space>"
	else:
		return a

def f(a):
	if a == "\n":
		return "enter"
	elif a == " ":
		return "пробел"
	else:
		return a

def winchecker(event):
	messagebox.showerror("Ты выиграл", "Ты выиграл")
	exit()

def win():
	root.unbind("<Button-1>")
	pilImage = Image.open("Assets/Inf_5.png")
	image = ImageTk.PhotoImage(pilImage)
	c.create_image(400, 260, image=image)
	root.title("Нажмите в любом месте, чтобы выиграть")
	root.bind("<Button-1>", winchecker)
	root.mainloop()


flag = False

fr = f3()

def checker5(event):
	global flag
	x = event.x
	y = event.y
	if x >= 360 and x <= 420 and y >= 440 and y <= 460:
		flag = False
		two()

def checker4(event):
	global flag
	x = event.x
	y = event.y
	if x >= 150 and x <= 225 and y >= 440 and y <= 455:
		flag = True
		two()

def two():
	global flag, attempts, fr
	if flag:
		root.unbind("<Button-1>")
		pilImage = Image.open("Assets/Inf_4.png")
		image = ImageTk.PhotoImage(pilImage)
		c.create_image(400, 260, image=image)
		c.create_text(175, 505, text=fr[0], font="TimesNewRoman 7", fill="#000")
		c.create_text(448, 505, text=fr[1], font="TimesNewRoman 7", fill="#000")
		c.create_text(647, 505, text=fr[2], font="TimesNewRoman 7", fill="#000")
		c.create_text(699, 505, text=fr[3], font="TimesNewRoman 7", fill="#000")
		root.title("Загрузите задачку в систему (осталось %s)" % (attcount - attempts))
		root.bind("<Button-1>", checker5)
		root.mainloop()
	else:
		attempts += 1
		if attempts == attcount:
			win()
			return
		root.unbind("<Button-1>")
		pilImage = Image.open("Assets/Inf_3.png")
		image = ImageTk.PhotoImage(pilImage)
		c.create_image(400, 260, image=image)
		fr = f3()
		c.create_text(175, 503, text=fr[0], font="TimesNewRoman 7", fill="#000")
		c.create_text(448, 503, text=fr[1], font="TimesNewRoman 7", fill="#000")
		c.create_text(647, 503, text=fr[2], font="TimesNewRoman 7", fill="#000")
		c.create_text(699, 503, text=fr[3], font="TimesNewRoman 7", fill="#000")
		root.title("Сдайте задачку (осталось %s)" % (attcount - attempts))
		root.bind("<Button-1>", checker4)
		root.mainloop()

		

def checker3(event):
	x = event.x
	y = event.y
	if x >= 360 and x <= 420 and y >= 370 and y <= 390:
		two()


def one():
	root.unbind("<Button-1>")
	pilImage = Image.open("Assets/Inf_2.png")
	image = ImageTk.PhotoImage(pilImage)
	c.create_image(400, 260, image=image)
	root.title("Загрузите задачку в систему (осталось %s)" % (attcount - attempts))
	root.bind("<Button-1>", checker3)
	root.mainloop()

def checker2(event):
	x = event.x
	y = event.y
	if x >= 150 and x <= 225 and y >= 360 and y <= 380:
		one()

def null(event):
	root.unbind("<Button-1>")
	sleep(1)
	pilImage = Image.open("Assets/Inf_1.png")
	image = ImageTk.PhotoImage(pilImage)
	c.create_image(400, 260, image=image)
	root.title("Сдайте задачку (осталось %s)" % (attcount - attempts))
	root.bind("<Button-1>", checker2)
	root.mainloop()


def Save():
	root.unbind("<Button-1>")
	pilImage = Image.open("Assets/Scr_83.png")
	image = ImageTk.PhotoImage(pilImage)
	c.create_image(400, 260, image=image)
	root.title("Нажмите в любом месте")
	root.bind("<Button-1>", null)
	root.mainloop()

def checker1(event):
	x = event.x
	y = event.y
	if x >= 60 and x <= 80 and y >= 50 and y <= 70:
		Save()

def presave():
	pilImage = Image.open("Assets/Scr_82.png")
	image = ImageTk.PhotoImage(pilImage)
	c.create_image(400, 260, image=image)
	root.title("Нажмите \"Сохранить\"")
	root.bind("<Button-1>", checker1)
	root.mainloop()

def Symbhol(event):
	global code
	ans = "from random import *\nif randint(0, 1)  == 1:\n    print(\"YES\")\nelse:\n    print(\"NO\")\n"
	if code != -1:
		root.unbind(f2(ans[code]))
	else:
		root.unbind("<Return>")
	code += 1
	if code == 83:
		presave()
		return
	pilImage = Image.open("Assets/Scr_" + str(code - 1) + ".png")
	image = ImageTk.PhotoImage(pilImage)
	c.create_image(400, 260, image=image)
	root.title("Нажмите " + f(ans[code]))
	root.bind(f2(ans[code]), Symbhol)
	root.mainloop()

def Code(event):
	c.delete("all")
	global play, ex1t
	play.place_forget()
	ex1t.place_forget()
	c.create_text(400, 250, text="Здравствуйте, Кирилл Клигунов,\nвам предстоит\nсдать задачу №1183.\nПодсказки смотрите в заголовке окна\nДля продолжения нажмите\nEnter", font="Virdinia 22", fill="#f00")
	root.bind("<Return>", Symbhol)
	root.mainloop()

def start():
	global play, ex1t
	play = Button(c, text = "Начать", width = 50, height = 5, bg="#f00", activebackground="#f33", bd=0, highlightthickness=0)
	play.place(x = 200, y = 200)
	play.bind("<Button-1>", Code)
	ex1t = Button(c, text = "Выход", width = 50, height = 5, bg="#f00", activebackground="#f33", bd=0, highlightthickness=0)
	ex1t.bind("<Button-1>", exit)
	ex1t.place(x = 200, y = 275)

def Info(event):
	d = datetime.now().strftime("%Y")
	info = Tk()
	info.title("Info")
	text = Label(info)
	text["text"] = "Симулятор Кирилла Клигунова\n\n© Copyright ShchMax & Ivan1874\n2017 - " + d
	text["font"] = ("New Times Roman", 20)	
	text.pack()
	info.mainloop()

root = Tk()
root.geometry(str(w) + "x" + str(h))
root.bind("<F1>", Info)
c = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="#000", bd=0, highlightthickness=0)
c.pack()
start()
root.mainloop()