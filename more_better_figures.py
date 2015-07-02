import numpy as np
import matplotlib.pyplot as plt

# data:
N = 5
menMeans = (20, 35, 30, 35, 27)
menStd   = ( 2,  3,  4,  1,  2)

womenMeans = (25, 32, 34, 20, 25)
womenStd   = ( 3,  5,  2,  3,  3)

ind = np.arange(N) # the x locations for the groups  
width=0.3333       # the width of the bars

orangecol = "#F9A65A"
bluecol   = "#599AD3"


rects1 = plt.bar(ind, menMeans, width, yerr=menStd,
  error_kw={"ecolor":orangecol,"lw":4, 
    "capsize":8,"capthick":3},
  color=orangecol, lw=0, alpha=0.5)

rects2 = plt.bar(ind-width, womenMeans, width, yerr=womenStd,
  error_kw={"ecolor":bluecol,"lw":4, 
    "capsize":8,"capthick":3},
  color=bluecol, lw=0, alpha=0.5)

plt.title('Scores by group and gender', fontsize= 24)

plt.xlabel("Group", fontsize = 18)
plt.ylabel('Scores', fontsize = 18)
plt.xticks(ind, ('1', '2', '3', '4', '5') )

plt.legend( (rects1[0], rects2[0]), ('Men', 'Women'), 
    fontsize=18, frameon=False )

# add space to left and right:
plt.xlim([0-2*width,4+2*width])

plt.show()
