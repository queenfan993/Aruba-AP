import numpy as np
import pandas as pd
import csv
import re
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.cm as cm
from merge import *
from extract import *
from gen_feature_pandas import *


def gen_feature_pandas(feature, time, AP_bssid): 
  radio_num = len(AP_bssid)
  feature_num = len(feature)
  features = []
  x = np.zeros([(time-1)*radio_num,feature_num])
  for i in range(radio_num):
    for j in range(feature_num):
      for k in range(time-1):  
        x[k+((time-1)*i)][j] = func(feature[j], time, AP_bssid[i])[k]
      
  
  x = StandardScaler().fit_transform(x)
  pca = PCA(n_components=2)
  principalComponents = pca.fit_transform(x)
  principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])     

  gg = np.ones((time-1)*radio_num)
  for i in range(1,radio_num):
    for j in range(time-1):
      gg[(time-1)*i+j] = gg[(time-1)*i+j]+i
  df = pd.DataFrame(gg,columns =['target']) 
  finalDf = pd.concat([principalDf, df[['target']]], axis = 1)
  return finalDf

''' 
def gen_final_pandas(principleDf, time, AP_bssid):
  radio_num = len(AP_bssid)
  gg = np.ones((time-1)*radio_num)
  for i in range(1,radio_num):
    for j in range(time-1):
      gg[(time-1)*i+j] = gg[(time-1)*i+j]+i
  df = pd.DataFrame(gg,columns =['target'])
  return pd.concat([principleDf, df[['target']]], axis = 1)    
'''

AP_radio = merge(extract_radio())[:20]
feature = ['wlanAPStatsTotDataBytes','wlanAPNumClients','wlanAPChannelThroughput','staSignalToNoiseRatio','wlanAPChRxUtilization','wlanAPChTxUtilization','wlanAPChUtilization']
#finalDf = gen_final_pandas(gen_feature_pandas(feature,180,AP_bssid), 180, AP_bssid)
finalDf = gen_feature_pandas(feature,30,AP_radio)

targets = []
for i in range(len(AP_radio)):
  targets.append(i)

'''
fig = sns.FacetGrid(data=finalDf, hue='target', hue_order=targets)
fig.map(plt.scatter, 'principle component 1', 'principle component 2')
'''

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)

colors = cm.rainbow(np.linspace(0, 1, len(AP_radio)))
for target, colors in zip(targets,colors):
    indicesToKeep = finalDf['target'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = colors
               , s = 50)

#ax.legend(targets)
ax.grid()

plt.savefig("7fe20ap30time.png")
