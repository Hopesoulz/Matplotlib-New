# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gGqelR3mkgKN-jx23E0iIT6ygAEmfImX
"""

import matplotlib.pyplot as plt
import numpy as np

y = np.array([3, 8, 1, 10])

plt.plot(y, marker='o', ms=20)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([2,3,10,5])
y= np.array([3, 8, 1, 10])
plt.plot(y, marker='o', ms=20, color='r')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x1=np.array([2,3,10,5])
y1= np.array([3, 8, 1, 10])
x2=np.array([5,4,1,5])
y2= np.array([3, 8, 5, 10])
plt.plot(x1,y1,x2,y2)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([2,3,6,10])
y= np.array([14, 16, 23, 28])
plt.plot(y,x,marker='o', ms=20, color='r')
plt.xlabel("overs")
plt.ylabel("runs")
plt.show()

import matplotlib.pyplot as plt
import numpy as np
#plt1
x1=np.array([2,3,4,6])
y1= np.array([3, 8, 1, 10])
plt.subplot(2,1,2)
plt.plot(x1,y1)
plt.show()
#plt2
x2=np.array([0,1,2,3])
y2= np.array([4,1,5,6])
plt.subplot(2,1,2)
plt.plot(x2,y2)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
#plt1
x1=np.array([2,3,4,6])
y1= np.array([3, 8, 1, 10])

plt.scatter(x1,y1,color='r')

#plt2
x2=np.array([0,1,2,3])
y2= np.array([4,1,5,6])

plt.scatter(x2,y2,color='g')

import matplotlib.pyplot as plt
import numpy as np
#plt1
x=np.array([2,3,4,6])
y= np.array([3, 8, 1, 10])
plt.scatter(x,y,color='r')

import matplotlib.pyplot as plt
import numpy as np
x=np.array(['A','B','C','D'])
y=np.array([3, 8, 1, 10])
plt.bar(x,y)
plt.show()