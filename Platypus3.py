import pandas
import numpy as np
import matplotlib.pyplot as plt
import h5py
from datetime import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder

f = h5py.File("data1.h5", 'r')
intervals    = f['intervals'][()]
cancelFlag   = f['cancelFlag'][()]
dateDeliv    = f['dateDeliv'][()]
dateOrder    = f['dateOrder'][()]
nItems       = f['nItems'][()]
channel      = f['channel'][()]
prepay       = f['prepay'][()]
nEdit        = f['nEdit'][()]
deliveryType = f['deliveryType'][()]

dtO=[]
wd=[]
n=1000000
cancelFlag = cancelFlag[:n]
for i in range(n):
    year, day, month = dateDeliv[i,:]
    curDate = date(year=int(year), day=int(day), month=int(month))
    dtO.append(curDate)
    wd.append(curDate.weekday())
wd = np.array(wd)

d=[]
d.append(np.sum(cancelFlag*(wd==0)))
d.append(np.sum(cancelFlag*(wd==1)))
d.append(np.sum(cancelFlag*(wd==2)))
d.append(np.sum(cancelFlag*(wd==3)))
d.append(np.sum(cancelFlag*(wd==4)))
d.append(np.sum(cancelFlag*(wd==5)))
d.append(np.sum(cancelFlag*(wd==6)))

plt.pie(d, labels=['Sunday', 'Monday', 'Tuesday', 'Wendesday', 'Thursday', 'Friday', 'Saturday'], autopct='%1.1f%%' )
plt.title('Days of week cancel')
plt.show()

