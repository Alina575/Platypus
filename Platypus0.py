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
f.close()

print(dateDeliv.shape)

#dtO=[]
#for i in range(dateDeliv.shape[0]):
#    year, day, month = dateOrder[i,:]
#    dtO.append(date(year=int(year), day=int(day), month=int(month)))
#
#dDv=[]
#for d in a['OrderDate']:
#    year, day, month = dateDeliv[i,:]
#    dDv.append(date(year=int(year), day=int(day), month=int(month)))


X = np.zeros((5,prepay.shape[0]))
#X = np.zeros((3,prepay.shape[0]))
X[0,:] = prepay
X[1,:] = nEdit
X[2,:] = deliveryType
X[3,:] = intervals[:,0]
X[4,:] = intervals[:,1]
#X[5,:] = nItems
#
#enc = OneHotEncoder(handle_unknown='ignore')
#ch0 = channel.reshape(-1,1)
#enc.fit(ch0)
#print(enc.categories_)
#X[6:6+enc.categories_[0].shape[0],:] = np.transpose(enc.transform(ch0).toarray())
y = cancelFlag

border = 1000000
X0 = X[:,border:]
y0 = y[border:]
X  = X[:,:border]
y  = y[:border]

X = np.transpose(X)
X0 = np.transpose(X0)

print(X.shape)


clf = RandomForestClassifier(max_depth=7, n_estimators=30)
clf.fit(X, y)
print(clf.feature_importances_)
score = clf.score(X0,y0)

print('score:', score)

minimum = np.sum(cancelFlag)/np.shape(cancelFlag)
print(score + minimum)

#
#f = h5py.File('data.h5', 'r')
#intervals = f['intervals']

#plt.scatter(intervals[:,0], intervals[:,1])
