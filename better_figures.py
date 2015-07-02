import numpy as np
import matplotlib.pyplot as plt

# data:
N = 5
menMeans = (20, 35, 30, 35, 27)
menStd   = ( 2,  3,  4,  1,  2)

womenMeans = (25, 32, 34, 20, 25)
womenStd   = ( 3,  5,  2,  3,  3)


ind = np.arange(N) # the x locations for the groups
width = 0.3        # the width of the bars

rects1 = plt.bar(ind,       menMeans,   width, yerr=menStd,   color='r')
rects2 = plt.bar(ind+width, womenMeans, width, yerr=womenStd, color='b')

plt.legend( (rects1[0], rects2[0]), ('Men', 'Women') )
plt.show()
