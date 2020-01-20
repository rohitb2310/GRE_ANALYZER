#Name : Piyush Rajendra Chaudhari
#Year/Div : 2019-2020/TE-C
#Roll No : TECOC311
#Assignment No.3 : Plot the Graph by loading any DataSet (Analysis)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
table = pd.read_csv('abc.csv')
#table.head()
#Each value is the hex code for the team's colours, in order of our chart
studentColours = ['#034694','#001C58','#5CBFEB','#D00027',
              '#EF0107','#DA020E','#274488','#ED1A3B',
               '#000000','#091453','#60223B']
#plt.style.use('ggplot')
plt.bar(x=np.arange(1,11),height=table['Total'],color = studentColours)
#Label bars, axes and the chart as before
plt.title("Unit Test Marks (CN + TOC + ISEE)")
plt.xticks(np.arange(1,11), table['Name'], rotation=90)
plt.xlabel("Name")
plt.ylabel("Total")
plt.show()
