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

n = 1000000
cancelFlag=cancelFlag[:n]
dtO=[]
for i in range(n):
    year, day, month = dateOrder[i,:]
    dtO.append(date(year=int(year), day=int(day), month=int(month)))

dDv=[]
for i in range(n):
    year, day, month = dateDeliv[i,:]
    dDv.append(date(year=int(year), day=int(day), month=int(month)))

#print(np.sum(prepay))
#isPrepay = np.sum((prepay)*cancelFlag)
#isnPrepay = np.sum((1-prepay)*cancelFlag)
#plt.pie([isPrepay, isnPrepay], labels=['Prepay', 'No prepay'],autopct='%1.1f%%' )
#plt.title('Cancel')
#plt.show()

ddiff = []
for (dd,do) in zip(dtO, dDv):
    ddiff.append((dd - do).days)
ddiff = np.array(ddiff)

print(np.amax(ddiff))
print(np.amin(ddiff))

a = np.sum(cancelFlag*(ddiff==1))
b = np.sum((1-cancelFlag)*(ddiff==1))
plt.pie([a,b], labels=['Cancel', 'No Cancel'], autopct='%1.1f%%' )
plt.title('1 day diff')
plt.show()

days=2
a = np.sum(cancelFlag*(ddiff==days))
b = np.sum((1-cancelFlag)*(ddiff==days))
plt.pie([a,b], labels=['Cancel', 'No Cancel'], autopct='%1.1f%%' )
plt.title('2 day diff')
plt.show()

days=3
a = np.sum(cancelFlag*(ddiff==days))
b = np.sum((1-cancelFlag)*(ddiff==days))
plt.pie([a,b], labels=['Cancel', 'No Cancel'], autopct='%1.1f%%' )
plt.title('3 day diff')
plt.show()

a = np.sum(cancelFlag*(ddiff>days))
b = np.sum((1-cancelFlag)*(ddiff>days))
plt.pie([a,b], labels=['Cancel', 'No Cancel'], autopct='%1.1f%%' )
plt.title('3+ day diff')
plt.show()
