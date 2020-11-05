# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# Choose the height of the bars
height = [3, 12, 5, 18, 45]
 
# Choose the names of the bars
bars = ('group1', 'group2', 'group3', 'group4', 'group5')
y_pos = np.arange(len(bars))
 
# Create bars
plt.bar(y_pos, height,width=[0.5,0.6,0.8,0.9,1.0])
 
# Create names on the x-axis
plt.xticks(y_pos, bars, color='orange')
plt.yticks(color='orange')
 
# Show graphic
plt.show()
