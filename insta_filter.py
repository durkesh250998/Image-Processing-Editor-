from tkinter import Label
import tkinter
from PIL import ImageTk, Image 
from tkinter import Button
from tkinter import filedialog 
import pilgram
import os
def aden_filter():
	x = openfilename() 
	print(x)
	im=Image.open(x)
	print("Inside aden_filter")
#	os.remove("/home/durkesh/Downloads/image.jpg")
	pilgram.aden(im).save("/home/durkesh/Downloads/image.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def Inkwell_filter():
	print("Inside Inkwell")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.inkwell(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def brannan_filter():
	print("Inside brannan")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.brannan(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def brooklyn_filter():
	print("Inside brooklyn")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.brooklyn(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def clarendon_filter():
	print("Inside clarendon")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.clarendon(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
#def css_filter():
#	print("Inside css")
#	x = openfilename() 
#	print(x)
#	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
#	pilgram.css(im).save("/home/durkesh/Downloads/mits.jpg")
#	h="/home/durkesh/Downloads/mits.jpg"
#	open_img(h)
def earlybird_filter():
	print("Inside earlybird")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.earlybird(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def gingham_filter():
	print("Inside gingham")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.gingham(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def hudson_filter():
	print("Inside hudson")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.hudson(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def kelvin_filter():
	print("Inside kelvin")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.kelvin(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def lark_filter():
	print("Inside lark")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.lark(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def lofi_filter():
	print("Inside lofi")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.lofi(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def maven_filter():
	print("Inside maven")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.maven(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def mayfair_filter():
	print("Inside mayfair")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.mayfair(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def moon_filter():
	print("Inside moon")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.moon(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def nashville_filter():
	print("Inside nashville")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.nashville(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def perpetua_filter():
	print("Inside perpetua")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.perpetua(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def reyes_filter():
	print("Inside reyes")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.reyes(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def rise_filter():
	print("Inside rise")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.rise(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def slumber_filter():
	print("Inside slumber")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.slumber(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def stinson_filter():
	print("Inside stinson")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.stinson(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def toaster_filter():
	print("Inside toaster")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.toaster(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
#def util_filter():
#	print("Inside util")
#	x = openfilename() 
#	print(x)
#	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
#	pilgram.util(im).save("/home/durkesh/Downloads/mits.jpg")
#	h="/home/durkesh/Downloads/mits.jpg"
#	open_img(h)
def valencia_filter():
	print("Inside valencia")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.valencia(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def walden_filter():
	print("Inside walden")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.walden(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def willow_filter():
	print("Inside willow")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.willow(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def xpro2_filter():
	print("Inside xpro2")
	x = openfilename() 
	print(x)
	im=Image.open(x)
#	os.remove("/home/durkesh/Downloads/mits.jpg")
	pilgram.xpro2(im).save("/home/durkesh/Downloads/mits.jpg")
	h="/home/durkesh/Downloads/mits.jpg"
	open_img(h)
def open_img(h): 
	img = Image.open(h) 
	img = img.resize((300,300), Image.ANTIALIAS) 
	img = ImageTk.PhotoImage(img) 
	panel = Label(root, image = img) 
	panel.image = img 
	panel.grid(row = 2) 
def openfilename(): 
	filename = filedialog.askopenfilename(title ='open') 
	return filename
def switcher(argument):
		if argument==1:
			aden_filter()
		elif argument==2:
			Inkwell_filter()
		elif argument==3:
			brannan_filter()
		elif argument==4:
			brooklyn_filter()
		elif argument==5:
			clarendon_filter()
		elif argument==6:
			earlybird_filter()
		elif argument==7:
			gingham_filter()
		elif argument==8:
			hudson_filter()
		elif argument==9:
			kelvin_filter()
		elif argument==10:
			lark_filter()
		elif argument==11:
			lofi_filter()
		elif argument==12:
			maven_filter()
		elif argument==13:
			mayfair_filter()
		elif argument==14:
			moon_filter()
		elif argument==15:
			nashville_filter()
		elif argument==16:
			perpetua_filter()
		elif argument==17:
			reyes_filter()
		elif argument==18:
			rise_filter()
		elif argument==19:
			slumber_filter()
		elif argument==20:
			stinson_filter()
		elif argument==21:
			toaster_filter()
		elif argument==22:
			valencia_filter()
		elif argument==23:
			walden_filter()
		elif argument==24:
			willow_filter()
		elif argument==25:
			xpro2_filter()
		else:
			exit(0)
if __name__ == "__main__":
	while(1):
		root = tkinter.Tk() 
		root.title("Image Loader") 
		root.resizable(width = True, height = True) 
		argument=int(input("Enter 1 for Aden\nEnter 2 for Inkwell\nEnter 3 for Brannan\nEnter 4 for brooklyn\nEnter 5 for clarendon\nEnter 6 for earlybird\nEnter 7 for gingham\nEnter 8 for hudson\nEnter 9 for kelvin\nEnter 10 for lark\nEnter 11 for lofi\nEnter 12 for maven\nEnter 13 for mayfair\nEnter 14 for moon\nEnter 15 for nashville\nEnter 16 for perpetua\nEnter 17 for reyes\nEnter 18 for rise\nEnter 19 for slumber\nEnter 20 for stinson\nEnter 21 for toaster\nEnter 22 for valencia\nEnter 23 for walden\nEnter 24 for willow\nEnter 25 for xpro2\n"))
		Button(root, text ='Press Close Icon For New Filter', command = switcher(argument)).grid(row = 1, columnspan = 4) 
		root.mainloop() 