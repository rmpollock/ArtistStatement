import math
import numpy

#SHAPE CLASSES

class Triangle (object):
	#A three sided shape
	def __init__(self,s1,s2,s3):
		self.side1 = s1
		self.side2 = s2
		self.side3 = s3

	def if_tri(self):
		#Checks in valid triangle
		a = self.side1 + self.side2 > self.side3
		b = self.side2 + self.side3 > self.side1
		c = self.side1 + self.side3 > self.side2
		if a and b and c:
			return True
		else:
			return False


class Rectangle (object):
	# 4 Sided Shape
	angle = 90
	def __init__ (self,side1,side2):
		self.side1=side1
		self.side2=side2


class Circle(object):
	def __init__(self,r):
		self.radius = r

class RegPoly(object):
	def __init__ (self,side,num):
		self.side_length = float(side)
		self.num_sides = num
		self.inter_angle = float((num-2)*math.pi/num)
		self.angle = float(2*math.pi/num)
		self.radius = float(side/(2*math.sin(math.pi/num)))
		self.offset = 0
	
	def set_center(self,x,y):
		self.centerx = x
		self.centery = y

	def set_side_len(self,size):
		self.side_length = float(size)
		self.radius = float(size/(2*math.sin(math.pi/self.num_sides)))

	def set_radius(self,r):
		self.radius = float(r)
		self.side_length = float(r * (2*math.sin(math.pi/self.num_sides)))

	def vertices(self,angle):
		#Finds x and y coordinates of each vertex and saves to a n by 2 matrix 
		self.offset = angle
		angle *= (math.pi/180) 
		self.points = numpy.empty([self.num_sides,2])
		for x in range(self.num_sides):
			self.points[x][0] = float(self.centerx+self.radius*math.cos(self.angle*x+angle))
			self.points[x][1] = float(self.centery+self.radius*math.sin(self.angle*x+angle))
		return self.points 
			
			
			

