import numpy as np
import pandas as pd
import csv
import re
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import matplotlib.cm as cm
from sklearn import manifold
from merge import *
from extract import *


def gen_feature_pandas(feature, time, AP_bssid): 
  radio_num = len(AP_bssid)
  feature_num = len(feature)
  x = np.vstack((func(feature[0], time, AP_bssid[0]),func(feature[1], time, AP_bssid[0])))
  x = np.vstack((x,func(feature[2], time, AP_bssid[0])))
  x = np.vstack((x,func(feature[3], time, AP_bssid[0])))
  x = np.vstack((x,func(feature[4], time, AP_bssid[0])))
  x = np.vstack((x,func(feature[5], time, AP_bssid[0])))
  x = np.vstack((x,func(feature[6], time, AP_bssid[0])))
  for i in range(1,radio_num):
    y = np.vstack((func(feature[0], time, AP_bssid[i]),func(feature[1], time, AP_bssid[i])))
    for j in range(2,feature_num):
      y = np.vstack((y,func(feature[j], time, AP_bssid[i])))
    x = np.hstack((x,y))
    y = np.array([]) 
  x = np.transpose(x)
  x = StandardScaler().fit_transform(x) 
  return x



AP_radio = merge_radio(extract_radio())[:30]
feature = ['wlanAPStatsTotDataBytes','wlanAPNumClients','wlanAPChannelThroughput','staSignalToNoiseRatio','wlanAPChRxUtilization','wlanAPChTxUtilization','wlanAPChUtilization']
colors = cm.rainbow(np.linspace(0, 1, len(AP_radio)))
train_data = gen_feature_pandas(feature,30,AP_radio)

trans_data = manifold.LocallyLinearEmbedding(n_neighbors =20, n_components = 2,
                                method='standard').fit_transform(train_data)
plt.scatter(trans_data[:, 0], trans_data[:, 1], marker='o', c=colors)

plt.savefig("lle_10radio20time7fe.png")
