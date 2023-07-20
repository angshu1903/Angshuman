import numpy
import numpy as np 
import matplotlib.pyplot as plt
inp_arr = [2,4,4,5,5,6,8,8,9,9] 
print ("Data values:\n", inp_arr) 
log_val = np.log(inp_arr) 
print ("logarithmic data values:\n", log_val)
plt.rcParams["figure.figsize"] = [7.50, 5.50]
plt.rcParams["figure.autolayout"] = True
x = [2,3,4,5,6,7,10,11,20,36]
z = [2,4,4,5,5,6,8,8,9,9]
y= log_val
plt.plot(x, z,color='red',marker='o')
plt.ylim(0,40)
plt.xlim(0,40)
plt.xlabel('number of mass points')
plt.ylabel('number of folds')
plt.title('Graph showing wrinkles pattern on varying mass distribution')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
(slope,intercept)=np.polyfit(x,y,1)
print (slope)
plt.show()
#the plot of log of number of folds vs the number of mass points
#Angshuman Bhandari
#varying the distribution of mass to observe the variation in number of folds
