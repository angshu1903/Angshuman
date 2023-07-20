import matplotlib.pyplot as plt
import numpy as np
x = [2,3,4,5,7,10,11,20,36]
y = [2,3.4,4,5,6,8,8,9,9]
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('NUMBER OF MASS POINTS (log scale)')
ax.set_ylabel('NUMBER OF FOLDS (log scale)')
(slope,intercept)=np.polyfit(np.log(x),np.log(y),1)
print(slope)
plt.show()
