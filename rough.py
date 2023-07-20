import math
pi=math.pi
r_str=input('enter the value of radius of curtain: ')
l_str=input ('enter the number of mass points: ')
r=int(r_str)
l=int(l_str)
d=  2*pi*r/l
n=round(d,2)
print ('n= ',n)

