import numpy as np
import matplotlib.pyplot as plt 
  
# line 1 points 
y1 = [26.8,32.3,34.1,35.6,37.7] 
x1 = [2016,2017,2018,2019,2020] 
y2 = [60, 60, 60, 60, 60]
plt.plot(x1, y1, label="installed", color='green',linestyle='dashed', marker='o',markerfacecolor='red', markersize=8)
plt.plot(x1, y2, label="target", color='blue',linestyle='dashed', marker='o',markerfacecolor='red', markersize=8)

# naming the x axis 
plt.xlabel('Year') 
# naming the y axis 
plt.ylabel('Gigawatt') 
# giving a title to my graph 
plt.title('Installed capacity in India') 
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show()
