import matplotlib.pyplot as plt
import numpy as np

array = np.arange(1,21)
array2 = np.arange(10,31)
plt.pie(array, labels=  array2, autopct='%.2f' )

plt.show()