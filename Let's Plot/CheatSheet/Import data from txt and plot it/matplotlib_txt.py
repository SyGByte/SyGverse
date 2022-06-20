# importing required packages
import numpy as np
import matplotlib.pyplot as plt

# importing file
#path of file
file = 'Let's Plot/CheatSheet/Import data from txt and plot it/plot_txt.txt' 
# making empty lists
roll = []
phy_score = []
maths_score = []

# importing data form .txt file

for line in open(file,'r'):
    lines = [i for i in line.split()]
    roll.append(float(lines[0]))
    phy_score.append(float(lines[1]))
    maths_score.append(float(lines[2]))
    
# Let's Plot

plt.plot(roll,phy_marks,'ro-', markersize=2, label="Physics")
plt.plot(roll,maths_marks,'bd-', markersize=2, label="Maths")
plt.legend()
plt.xlabel("Roll")
plt.ylabel('Marks')
plt.grid(True)
# plt.savefig('marks.png',dpi=100)
plt.show()
