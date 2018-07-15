import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from properties import colors
master=pd.read_excel('Master.xlsx')
category=input("Enter the Category: ")
file_name=(master[master.Name==category])
#print(file_name)
fikle_name=file_name.iloc[0,1]
#print(fikle_name)
#sub_cat=np.array(file_name)[0][1]  // another way of accessing file name .xlsx for subcategory
slave=pd.read_excel(fikle_name)
sub_category=input("Enter the sub category:  ")
row_info=(slave[slave.Description==sub_category])
refine=row_info.iloc[:,2:]
np_x= np.array(refine.columns.values.tolist())
#print(np_x)
#print(type(np_x))
np_y=np.array(refine)[0]
#print(np_y)
#print(type(np_y))
plt.scatter(np_x,np_y,s=np_y*10,alpha=0.5,c=colors)
plt.title("Tax Variations Of 15 years for "+sub_category)
plt.xlabel(" Time(In years)")
plt.ylabel("Tax Rate(%)")
plt.xticks(np.arange(min(np_x)-1, max(np_x)+1, 1.0),rotation='vertical')
plt.yticks(np.arange(min(np_y)-2, max(np_y)+2, 1))
plt.margins(0.1)
for i in range(len(np_x)):
    plt.text(np_x[i],np_y[i],str(np_y[i])+"%")
#plt.fill_between(np_x,np_y,min(np_y),color="blue")
plt.grid(True)
plt.show()




