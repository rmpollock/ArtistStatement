import Shapes
import numpy
import math
from Tkinter import *

#Functions for drawing onto GUI canvas

def drawPoly(cr,num,length=75):
	#Draws Regular Polygon onto canvas with a stroke and no fill
	poly = Shapes.RegPoly(length,num)
	poly.set_center(175,175)
	poly.vertices(0)
	n = poly.num_sides
	for x in range (n):
		cr.create_line(poly.points[x][0],poly.points[x][1],poly.points[(x+1)%n][0],poly.points[(x+1)%n][1])

def drawPolySh(cr,sh):
	
	n = sh.num_sides
	for x in range (n):
		cr.create_line(sh.points[x][0],sh.points[x][1],sh.points[(x+1)%n][0],sh.points[(x+1)%n][1])

def drawPenrose(cr,num,l):
	cr.delete('all')
	tri = Shapes.RegPoly(150,num)
	tri.set_radius(float(350/4))
	tri.set_center(175,175)
	tri.vertices(0)
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
			


		drawPoly(cr,num,inner_tri.side_length)

		for x in range(0,tri.num_sides):
			a = (x+tri.num_sides-1)%tri.num_sides
			b = (x+1)%tri.num_sides
			cr.create_line(point_tri[x].points[(x-1)%tri.num_sides][0],\
			point_tri[x].points[(x-1)%tri.num_sides][1], point_tri[(x-1)%tri.num_sides].points[x][0], \
			point_tri[(x-1)%tri.num_sides].points[x][1])	
			cr.create_line(point_tri[x].points[a][0],point_tri[x].points[a][1], \
			point_tri[x].points[b][0],point_tri[x].points[b][1])
		
		
		for z in range(tri.num_sides):
			a = (z+tri.num_sides-1)%tri.num_sides
			b = (z+1)%tri.num_sides
			angle = tri.inter_angle*(float((tri.num_sides-3))/(tri.num_sides-2) ) - \
			(tri.inter_angle)*(z)*(float(2)/(tri.num_sides-2))
			
			cr.create_line(inner_tri.points[b][0],inner_tri.points[b][1], \
			inner_tri.points[b][0]+l*math.sin(angle),inner_tri.points[b][1]+l*math.cos(angle))
			
			cr.create_line(inner_tri.points[b][0]+l*math.sin(angle), \
			inner_tri.points[b][1]+l*math.cos(angle),point_tri[z].points[a][0],point_tri[z].points[a][1])

def sierpinski_sq_start(cr,sq,it):
	cr.delete('all')
	#Draws outer and center square of Sierpinski Carpet
	if it == 0:
		return
	drawPoly(cr,4,sq.side_length)
	sq0 = Shapes.RegPoly(float(sq.side_length/3),4)
	sq0.set_center(sq.centerx,sq.centery)
	drawPoly(cr,4,sq0.side_length)
	
	sierpinski_sq_rest(cr,sq0,it-2)

def sierpinski_sq_rest(cr,sq,it):
	#Draws remainder of the squares of Sierpinski Carpet	
	
	if it == 0:
		return
	
	new_sq = Shapes.RegPoly(float(sq.side_length/3),4)
	 
	for x in range(4):
		a=sq.side_length*math.cos(math.pi/4+x*math.pi/2)
		b=sq.side_length*math.sin(math.pi/4+x*math.pi/2)
		c=sq.radius*2*math.cos(x*math.pi/2)
		d=sq.radius*2*math.sin(x*math.pi/2)
		new_sq.set_center(sq.centerx+a,sq.centery+b)
		new_sq.vertices(0)
		drawPolySh(cr,new_sq)
		sierpinski_sq_rest(cr,new_sq,it-1)
		new_sq.set_center(sq.centerx+c,sq.centery+d)
		new_sq.vertices(0)
		drawPolySh(cr,new_sq)
		sierpinski_sq_rest(cr,new_sq,it-1)

def s_gasket_start(cr,sh,it):
	cr.delete('all')
	sierpinski_gasket(cr,sh,it)

def sierpinski_gasket(cr,sh,it):
	if it == 0:
		return
	
	else:
		drawPolySh(cr,sh)
		#side_l = float(sh.side_length/(sh.num_sides-1))
		side_l=float(sh.side_length/2)
		new_sh = Shapes.RegPoly(side_l,sh.num_sides)
		
		if sh.num_sides%2==0:
			radius = 2*new_sh.radius
		else:
			radius = 2*math.sqrt(new_sh.radius**2-(new_sh.side_length/2)**2)

		for x in range(sh.num_sides):
			theta = 2*math.pi*x/sh.num_sides
			a = math.cos(theta)*radius
			b = math.sin(theta)*radius
			new_sh.set_center(sh.centerx+a,sh.centery+b)
			new_sh.vertices(0)
			sierpinski_gasket(cr,new_sh,it-1)

def t_frac_start(cr,it):
	cr.delete('all')
	sq = Shapes.RegPoly(100,4)
	sq.set_center(175,175)
	sq.vertices(0)
	
	t_frac(cr,sq,it)

def t_frac (cr,sq,it):

	if it == 0:
		return
	
	drawPolySh(cr,sq)	

	for x in range(4):
		n_sq = Shapes.RegPoly(float(sq.side_length/2),4)
		n_sq.set_center(sq.points[x][0],sq.points[x][1])
		n_sq.vertices(0)
		t_frac(cr,n_sq,it-1)
	
	
	


