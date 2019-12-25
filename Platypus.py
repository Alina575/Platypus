import pandas
import numpy as np
import matplotlib.pyplot as plt
import h5py
from datetime import *

f = h5py.File("dataTest1.h5", 'w')

a = pandas.read_csv("test0.txt")
cancelFlag = np.array(a['CancelFlag'])
nItems = np.array(a['OrderCnt'])
channel = np.array(a['ChannelID'])
prepay = np.array(a['prepay'])
nEdit  = np.array(a['count_edit'])

f['cancelFlag'] = cancelFlag
f['nItems']  = nItems
f['channel']  = channel
f['prepay']  = prepay
f['nEdit']  = nEdit

print("!!!!!!!!!!!!!!!!!!!!!!!!!!")

intervals=[]
for inter in a['Interval']:
   s,fin = inter.split('-')
   intervals.append([float(s), float(fin)])
intervals = np.array(intervals)

f['intervals']  = intervals

print('aaaa')

dateOrders=[]
dateOrdersH5 = []
for d in a['Date']:
    day, month, year = d.split('/')
    dateOrders.append(date(year=int(year), day=int(day), month=int(month)))
    dateOrdersH5.append([int(year), int(day), int(month)])
dateOrdersH5 = np.array(dateOrdersH5)

dateDeliv=[]
dateDelivH5=[]
for d in a['OrderDate']:
    day, month, year = d.split('/')
    dateDelivH5.append([int(year), int(day), int(month)])
dateDelivH5=np.array(dateDelivH5)

f['dateDeliv']  = dateDelivH5
f['dateOrder']  = dateOrdersH5

deliveryType=np.zeros(len(a['DeliveryType']))
for i in range(len(a['DeliveryType'])):
    deliveryType[i] = 1 if len(a['DeliveryType'][i]) == 16 else 0

f['deliveryType'] = deliveryType
print('qqqqqqqqqqq')
f.close()

#
#f = h5py.File('data.h5', 'r')
#intervals = f['intervals']

#plt.scatter(intervals[:,0], intervals[:,1])
