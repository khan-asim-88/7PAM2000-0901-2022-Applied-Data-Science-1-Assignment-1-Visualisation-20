# Applied Data Science 1 Assignment No. 1 (Visualisation)
# Student Name: Asim Muhammad Salim.
# Student ID: 21031789


import pandas as pd
import matplotlib.pyplot as plt

    
data = pd.DataFrame({
   'Goats': [20, 18, 489, 675, 1776],
   'Horses': [4, 25, 281, 600, 1900]
   }, index=[1990, 1997, 2003, 2009, 2014])

data.plot.line()
plt.show()


data = pd.DataFrame({
   'Goats': [20, 18, 489, 675, 1776],
   'Horses': [4, 25, 281, 600, 1900]
   }, index=[1990, 1997, 2003, 2009, 2014])

data.plot.bar()
plt.show()


data = pd.DataFrame({'Mass': [40, 200],
                   'Height': [4, 7]},
                  index=['Goats', 'Horses'])

data.plot.pie(y='Mass', figsize=(5, 5))
plt.show()