import Shapes
import cairo
import numpy
import math
import Art
import draw
import webbrowser
from Tkinter import *

class app:
	def __init__ (self,master):
		self.AScheck = True
		self.Pcheck = True
		self.Fcheck = True
		self.Tcheck=True	

		self.F_c_v = False

		self.frame = Frame(master,width=1200,height=700)
		self.frame.pack_propagate(0)
		self.frame.pack()
		
		self.state = Button(self.frame,text = "Artist Statement", command = self.statement)
		self.state.pack()

		self.bottomframe = Frame(self.frame)
		self.bottomframe.pack(side=BOTTOM,fill=X)

		self.quit = Button(self.bottomframe, text = "Exit",command=self.frame.quit)
		self.quit.pack(side=RIGHT,anchor=S)

		self.port = Button(self.bottomframe, text = "Portfolio",command=openport)
		self.port.pack(side=LEFT,anchor=S)

		self.source = Button(self.bottomframe, text = "Source Code",command=opensource)
		self.source.pack(side=LEFT,anchor=S)

		
		

	def statement(self):
		if self.AScheck:
			self.w = Message(self.frame,text=Art.statement(),width=950)
			self.w.pack()
			
			subframe = Frame(self.frame,height = 30)

			self.Penrose = Button(subframe,text="Penrose Polygons",command = self.pen)
			self.Penrose.pack(side=LEFT)

			self.nature = Button(subframe,text="Nature",command = self.test)
			self.nature.pack(side=LEFT)	
		
			self.Fractal = Button(subframe,text="Fractals",command = self.frac)
			self.Fractal.pack(side=RIGHT)

	
			subframe.pack()

			self.AScheck=False

	def test(self):
		if self.Tcheck:
			self.imgsubframe = Frame(self.frame,width = 400)
			self.imgc = Canvas(self.imgsubframe,width=350,height=350)
			l = Label(self.imgsubframe,text="Natural Things")
			l.pack()
			df = Button(self.imgsubframe,text="Definition",command=nature)
			df.pack()
			mb = Menubutton(self.imgsubframe,text="Nature Images")
			mb.grid()
			mb.menu=Menu(mb,tearoff=0)
			mb["menu"] = mb.menu
			mb.pack(anchor = W)
			img_item = ["Flower","Tree","Mushroom"]
			for x in range(len(img_item)):
				mb.menu.add_command(label="%s" %img_item[x],command=lambda x=x: self.img_switch(x))
			
			self.imgc.pack()
			self.imgsubframe.pack_propagate(0)
			self.imgsubframe.pack(side=LEFT,anchor=N,fill=Y)
			self.Tcheck=False
	def frac(self):
		if self.Fcheck:
			self.fracsubframe = Frame(self.frame,width = 400)
			l = Label(self.fracsubframe, text="Fractals")
			l.pack(fill=X)
			df = Button(self.fracsubframe, text="Definition",command=Fracdef)
			df.pack()
			mb = Menubutton(self.fracsubframe,text="Fractals")
			mb.grid()
			mb.menu=Menu(mb,tearoff=0)
			mb["menu"] = mb.menu
			mb.pack(anchor = W)
			frac_item = ["Sierpinski Triagle","Sierpinski Carpet","T Fractal"]
			for x in range(len(frac_item)):
				mb.menu.add_command(label="%s" %frac_item[x],command=lambda x=x: self.fractest(x))

			self.fraccr = Canvas(self.fracsubframe,width = 350, height =350)
			self.fraccr.pack()

			self.fracsubframe.pack_propagate(0)
			self.fracsubframe.pack(side=LEFT,anchor=N,fill=Y)
			self.Fcheck=False

	def pen(self):
		if self.Pcheck:
			self.pen_subframe = Frame(self.frame,width = 400)
			l = Label(self.pen_subframe, text="Penrose Polygons")
			l.pack(fill=X)
			d = Button(self.pen_subframe,text="Definintion",command=Pendef)
			d.pack()
			mb = Menubutton(self.pen_subframe,text="Number of Sides")
			mb.grid()
			mb.menu = Menu(mb,tearoff=0)
			mb["menu"] = mb.menu
			mb.pack(anchor = W)
			for x in range(3,11):
				mb.menu.add_command(label="%s" %x, command=lambda x=x: self.drawPen(x))

			self.pencr = Canvas(self.pen_subframe,width = 350, height =350)		
			self.pencr.pack()		
			self.pen_subframe.pack_propagate(0)
			self.pen_subframe.pack(side=LEFT,anchor=N,fill=Y)

			self.pen_vis = False
			self.penrose_Num = 0
			self.Pcheck=False

	def drawPen(self,num):
		if not self.pen_vis:
			self.d3 = Button(self.pen_subframe, text = "3D Print",command=print3d)
			self.pensave = Button(self.pen_subframe, text = "Save to SVG",command=self.savePen)
			self.pensave.pack(side=LEFT,anchor=N)
			self.d3.pack(side=RIGHT,anchor=N)
			self.pen_vis = True
		self.penrose_Num = num;
		draw.drawPenrose(self.pencr,num,15)


	def savePen(self):
		self.filename_input = Tk()
		self.filename_input.title("Save File")
		self.fileframe=Frame(self.filename_input,width=400,height=100)
		self.fileframe.pack_propagate(0)
		self.fileframe.pack()
		save = Button(self.fileframe,text="Save",command=self.CloseSave)
		name = Message(self.fileframe,text="Filename: ",width=100)
		self.inpu = Entry(self.fileframe,width=100)
		save.pack(side=BOTTOM)
		name.pack(side=LEFT)
		self.inpu.pack(side=LEFT)
		
		self.filename_input.mainloop()

	def CloseSave(self):
		savename = self.inpu.get()
		self.fileframe.quit()
		self.filename_input.destroy()
		save_svg_pen(savename,self.penrose_Num)

	def img_switch(self,item):
		if item == 0:
			self.imgc.delete('all')
			self.photo = PhotoImage(file = './img/flower.gif')
			self.imgc.create_image(175,175,image=self.photo)
		elif item == 1:
			self.imgc.delete('all')
			self.photo = PhotoImage(file = './img/tree.gif')
			self.imgc.create_image(175,175,image=self.photo)
		elif item ==2:
			self.imgc.delete('all')
			self.photo = PhotoImage(file = './img/mushroom.gif')
			self.imgc.create_image(175,175,image=self.photo)
		

	def fractest(self,item,it=3):
		self.frac_choice = item
		if not self.F_c_v:
			self.F_c_v = True
			mb = Menubutton(self.fracsubframe,text="Iterations")
			mb.grid()
			mb.menu = Menu(mb,tearoff=0)
			mb["menu"] = mb.menu
			
			for x in range(3,7):
				mb.menu.add_command(label="%s" %x, command = lambda x=x: self.fractest(self.frac_choice,x)) 
			mb.pack(side=BOTTOM,anchor=W)
			
		if item == 1:
			sq = Shapes.RegPoly(150,4)
			sq.set_center(175,175)
			sq.vertices(0)
			draw.sierpinski_sq_start(self.fraccr,sq,it)

		if item == 2:
			draw.t_frac_start(self.fraccr,it)
		
		elif item ==0:
			sq = Shapes.RegPoly(160,3)
			sq.set_center(175,175)
			sq.vertices(0)
			draw.s_gasket_start(self.fraccr,sq,it)



def openport():
	webbrowser.open("https://www.behance.net/rossmpollock")

def opensource():
	webbrowser.open("https://github.com/rmpollock/ArtistStatement")

def nature():
	#Creates a window explaining why I use natural objects in my artwork
	#It's cause they are the only things I can draw
	window=Tk()
	window.title("Nature")
	frame=Frame(window,width=400,height=400)
	frame.pack_propagate(0)
	frame.pack()
	m = Message(frame,text =Art.NaturalThings(),width = 350)
	q = Button(frame, text = "Exit", command=frame.quit)
	q.pack(side=BOTTOM)
	m.pack()
	
	window.mainloop()
	window.destroy()

def print3d():
	#Makes a window that tells user they cannot 3d print an impossible object
	window=Tk()
	window.title("ERROR!")
	frame=Frame(window,width=300,height = 150,bg="Black")
	frame.pack()
	m = Message(frame,fg="Yellow",bg="Black", text =Art.SystemError(),width =250)
	q = Button(frame,highlightbackground="Black", text = "Exit", command=frame.quit)
	q.pack(side=BOTTOM)
	m.pack()
	
	window.mainloop()
	window.destroy()

def Fracdef():
	window = Tk()
	window.title("Fractals")
	mainframe = Frame(window,width=400,height=400)
	mainframe.pack_propagate(0)
	mainframe.pack()

	q = Button(mainframe, text = "Exit", command=mainframe.quit)
	q.pack(side=BOTTOM)

	m = Message(mainframe, text = Art.fractals(),width = 350)
	m.pack()
	window.mainloop()
	window.destroy()


def Pendef():
	window = Tk()
	window.title("Penrose")
	mainframe = Frame(window,width=400,height=400)
	mainframe.pack_propagate(0)
	mainframe.pack()

	q = Button(mainframe, text = "Exit", command=mainframe.quit)
	q.pack(side=BOTTOM)

	m = Message(mainframe, text = Art.PenroseObjects(),width = 350)
	m.pack()
	window.mainloop()
	window.destroy()	


def save_svg_pen(filename,num):
	img = cairo.SVGSurface("%s.svg" %filename,500,500)
	cr = cairo.Context(img)
	sh=Shapes.RegPoly(200,num)
	sh.set_radius=(200)
	sh.set_center(250,250)
	sh.vertices(0)
	
	draw_PENROSE(cr,sh,20)

	cr.show_page()

def save_svg_frac(filename,it,t):
	#Work in progress
	return
	
	

def canvas_input():
	# Takes user input to determine Size of Drawing Canvas	
	
	Length = raw_input("Enter canvas length: ")
	ulength = Length.decode(encoding='UTF-8',errors='strict')
	while True:
		if ulength.isnumeric():
			Length = float(Length)
			break
		else:
			Length = raw_input("Input Error! Please Enter Numeric Length: ")
			ulength = Length.decode(encoding='UTF-8',errors='strict')
	Width = raw_input("Enter canvas width: ")
	uwidth = Width.decode(encoding='UTF-8',errors='strict')
	while True:
		if uwidth.isnumeric():
			Width = float(Length)
			break
		else:
			Width = raw_input("Input Error! Please Enter Numeric Width: ")
			uwidth = Width.decode(encoding='UTF-8',errors='strict')

	return Length,Width

def draw_RegPoly(cr,poly):
	#Draws Regular Polygon onto canvas with a stroke and no fill
	poly.vertices(0)
	cr.move_to(poly.points[0][0],poly.points[0][1])
	for x in range (1,poly.num_sides):
		cr.line_to(poly.points[x][0],poly.points[x][1])
	cr.close_path()
	cr.stroke()

def draw_PENROSE(cr,tri,l):
	#Draws Penrose N-sided regular polygon onto canvas with a stroke and no fill
	
	#Checks if possible to draw with given polygon side length and offset length
	if 0 >= tri.side_length-4*l*(math.cos(tri.inter_angle)+1):
		print "INVALID"
		return

	else:
		inner_tri = Shapes.RegPoly(tri.side_length-4*l*(math.cos(tri.inter_angle)+1),tri.num_sides)
		inner_tri.set_center(tri.centerx,tri.centery)
		inner_tri.vertices(tri.offset)
		point_tri = [] 
		for y in range(tri.num_sides):
			point_tri.append(Shapes.RegPoly(l,tri.num_sides))
			point_tri[y].set_center(tri.centerx+(tri.radius-point_tri[y].radius)*math.cos(tri.angle*y \
			+tri.offset),tri.centery+(tri.radius-point_tri[y].radius)*math.sin(tri.angle*y+tri.offset))
			point_tri[y].vertices(tri.offset)
			#draw_RegPoly(cr,point_tri[y])

		#draw_RegPoly(cr,tri)
		draw_RegPoly(cr,inner_tri)
		
		cr.move_to(point_tri[0].points[tri.num_sides-1][0],point_tri[0].points[tri.num_sides-1][1])
		cr.line_to(point_tri[0].points[1][0],point_tri[0].points[1][1])	
		for x in range(1,tri.num_sides):
			a = (x+tri.num_sides-1)%tri.num_sides
			b = (x+1)%tri.num_sides
			cr.line_to(point_tri[x].points[a][0],point_tri[x].points[a][1])	
			cr.line_to(point_tri[x].points[b][0],point_tri[x].points[b][1])
		cr.close_path()
		cr.stroke()

		for z in range(tri.num_sides):
			a = (z+tri.num_sides-1)%tri.num_sides
			b = (z+1)%tri.num_sides
			angle = tri.inter_angle*(float((tri.num_sides-3))/(tri.num_sides-2) ) - \
			(tri.inter_angle)*(z)*(float(2)/(tri.num_sides-2))
			cr.move_to(inner_tri.points[b][0],inner_tri.points[b][1])
			cr.rel_line_to(l*math.sin(angle),l*math.cos(angle))
			cr.line_to(point_tri[z].points[a][0],point_tri[z].points[a][1])	
			cr.stroke()



def sierpinski_sq_start(cr,sq,it):
	#Draws outer and center square of Sierpinski Carpet
	if it == 0:
		return
	draw_RegPoly(cr,sq)
	sq0 = Shapes.RegPoly(sq.side_length/3,4)
	sq0.set_center(sq.centerx,sq.centery)
	draw_RegPoly(cr,sq0)
	
	sierpinski_sq_rest(cr,sq0,it-2)

def sierpinski_sq_rest(cr,sq,it):
	#Draws remainder of the squares of Sierpinski Carpet	
	
	if it == 0:
		return
	
	new_sq = Shapes.RegPoly(sq.side_length/3,4)
	 
	for x in range(4):
		a=sq.side_length*math.cos(math.pi/4+x*math.pi/2)
		b=sq.side_length*math.sin(math.pi/4+x*math.pi/2)
		c=sq.radius*2*math.cos(x*math.pi/2)
		d=sq.radius*2*math.sin(x*math.pi/2)
		new_sq.set_center(sq.centerx+a,sq.centery+b)
		draw_RegPoly(cr,new_sq)
		sierpinski_sq_rest(cr,new_sq,it-1)
		new_sq.set_center(sq.centerx+c,sq.centery+d)
		draw_RegPoly(cr,new_sq)
		sierpinski_sq_rest(cr,new_sq,it-1)
	
def Penrose():
	Length,Width = 1000,1000
	for x in range(3,10):
		img = cairo.SVGSurface("Penrose%s.svg" %x,Length,Width)
		cr = cairo.Context(img) 
		polygon = Shapes.RegPoly(333,x)
		polygon.set_center(Length/2,Width/2)
		draw_PENROSE(cr,polygon,30)
		cr.show_page()

def sierpinski_gasket(cr,sh,it):
	if it == 0:
		return
	
	else:
		draw_RegPoly(cr,sh)
		#side_l = float(sh.side_length/(sh.num_sides-1))
		side_l=float(sh.side_length/2)
		new_sh = Shapes.RegPoly(side_l,sh.num_sides)
		
		if sh.num_sides%2==0:
			radius = 2*new_sh.radius
		else:
			radius = 0

		for x in range(sh.num_sides):
			theta = 2*math.pi*x/sh.num_sides
			a = math.cos(theta)*radius
			b = math.sin(theta)*radius
			new_sh.set_center(sh.centerx+a,sh.centery+b)
			sierpinski_gasket(cr,new_sh,it-1)


# Main Function
def main():

	root = Tk()
	root.title("Artist Statement")
	window = app(root)	

	root.mainloop()


#Executes Main Function
main()
