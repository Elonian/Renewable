import numpy as np
import matplotlib.pyplot as plt 
  
# line 1 points 
y1 = [0.0720, 0.0870, 0.0870, 0.0890, 0.0770, 0.0690, 0.0580, 0.0490, 0.0490]
x1 = [2011,2012,2013,2014,2015,2016,2017,2018,2019] 

plt.plot(x1, y1, color='green',linestyle='dashed', marker='o',markerfacecolor='red', markersize=8)

# naming the x axis 
plt.xlabel('Year') 
# naming the y axis 
plt.ylabel('2019 USD/kWh') 
# giving a title to my graph 
plt.title('Weighted average of LOCE of wind projects 2011 - 19') 
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show()
