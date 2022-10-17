import numpy as np
from matplotlib import pyplot as plt

x=np.arange(1,11)
print(x)
y=[3,5,7,8,10,12,15,18,22,28]
print(y)
plt.scatter(x,y,color="r")
plt.title("Line Plot")
plt.xlabel("Age")
plt.ylabel("Year")
plt.grid(True)
plt.show()
