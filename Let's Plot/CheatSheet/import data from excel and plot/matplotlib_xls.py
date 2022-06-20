#path of file: "Let's Plot/CheatSheet/import data from excel and plot/plot_excel.xlsx"

# importing numpy as np.array takes less space than list
import numpy as np
# pandas will be used in import the excel file
import pandas as pd
# matplotlib.pyplot as versatile library used for plotting
import matplotlib.pyplot as plt

# importing the excel file

df = pd.read_excel("Let's Plot/CheatSheet/import data from excel and plot/plot_excel.xlsx")

# convert the datasets into numpy array

Number=np.array(df.Number)
Square=np.array(df.Square)
Cube=np.array(df.Cube)

# Let's plot
plt.plot(Number, Square,'bo-', markersize=2, label="Square")
plt.plot(Number, Cube,'ro-', markersize=2, label="Cube")
plt.xlabel("Number")
plt.ylabel("F")
plt.legend()
plt.title("Function")

#plt.savefig("bare_CS.png",dpi=100)
plt.show()
