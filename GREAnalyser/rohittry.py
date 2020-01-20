#Name : Piyush Rajendra Chaudhari
#Year/Div : 2019-2020/TE-C
#Roll No : TECOC311
#Assignment No.3 : Plot the Graph by loading any DataSet (Analysis)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# table = pd.read_csv('1.csv') #csv file
# #table.head()
# #Each value is the hex code for the team's colours, in order of our chart
# studentColours = ['#034694','#001C58','#5CBFEB','#D00027',
#               '#EF0107','#DA020E','#274488','#ED1A3B',
#                '#000000','#091453','#60223B']
# #plt.style.use('ggplot')
# plt.bar(x=np.arange(1,4),height=table['totalad'],color = studentColours, width=0.3)
# #Label bars, axes and the chart as before
# j = 'MIT'
# g = f'GRE Analyzer : prediction -> {j}'
#
# plt.title(g)
# plt.xticks(np.arange(1,4), table['Pref'], rotation=90)
# plt.xlabel("Pereferences")
# plt.ylabel("Admissions")
# # r4 =
#
# label = [18, 12, 8, 48]
#
# plt.show()

# table = pd.read_csv('1.csv') #csv file
#table.head()
#Each value is the hex code for the team's colours, in order of our chart
studentColours = ['#034694','#001C58','#5CBFEB','#D00027',
              '#EF0107','#DA020E','#274488','#ED1A3B',
               '#000000','#091453','#60223B']
#plt.style.use('ggplot')
l1 = [12, 12, 12]
xl1 = ['mit', 'vit', 'xxx']
plt.bar(x=np.arange(1,4),height=l1,color = studentColours, width=0.3)
#Label bars, axes and the chart as before
j = 'MIT'
g = f'GRE Analyzer : prediction -> {j}'

plt.title(g)
plt.xticks(np.arange(1,4), xl1, rotation=0)
plt.xlabel("Pereferences")
plt.ylabel("Admissions")
# r4 =
hy = []
hy = list(zip(l1, xl1))
hy.sort()
print(hy)
print(hy[0][1])
plt.show()