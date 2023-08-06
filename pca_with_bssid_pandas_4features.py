import numpy as np
import pandas as pd
import csv
import re
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from extract_bssid import extract_bssid
from extract_bssid import merge
import seaborn as sns
import matplotlib.cm as cm

# want to count in radio but need to start from bssid because the return data always with bssid but not always with radio
# name can be bssid or radio
def extract(feature, time, name):
  x = []  
  f = open(feature+'/'+feature+'_'+str(time)+'.csv', 'r')
  for row in csv.reader(f):
    for bssid_or_radio in range(len(name)):
      if str(row).find(name[bssid_or_radio])>0:
        x.append(int(re.split('[::,:,\',\s,\.]',str(row))[-2]))   
  f.close()
  return x

def func(feature, time, name):
  if feature in ['wlanAPStatsTotCtrlBytes', 'wlanAPStatsTotDataBytes', 'wlanAPStatsTotMgmtBytes','apBSSTxBytes','apBSSRxBytes']:
    x = []
    for i in range(1,time):
      x.append(sum(extract(feature, i+1, name))-sum(extract(feature, i, name))) 
    return x

  elif feature in ['wlanAPNumClients', 'apBSSBwRate']:
    x = []
    for i in range(1,time):
      x.append(sum(extract(feature, i, name)))  
    return x

  elif feature in ['staSignalToNoiseRatio']:
    x = []
    for i in range(1,time):
      if len(extract(feature,i,name)) >0:
        x.append(sum(extract(feature, i, name))/len(extract(feature,i,name)))
      else:
        x.append(0)   
    return x  
    
  else:
    x = []
    for i in range(1,time):
      x.append(extract(feature, i, name)[0])
    return x

def gen_feature_pandas(feature, time, AP_bssid): 
  radio_num = len(AP_bssid)
  feature_num = len(feature)
  x = np.vstack((func(feature[0], time, AP_bssid[0]),func(feature[1], time, AP_bssid[0])))
  x = np.vstack((x,func(feature[2], time, AP_bssid[0])))
  x = np.vstack((x,func(feature[3], time, AP_bssid[0])))
  for i in range(1,radio_num):
    y = np.vstack((func(feature[0], time, AP_bssid[i]),func(feature[1], time, AP_bssid[i])))
    for j in range(2,feature_num):
      y = np.vstack((y,func(feature[j], time, AP_bssid[i])))
    x = np.hstack((x,y))
    y = np.array([]) 
  x = np.transpose(x) 
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

AP_bssid = merge(extract_bssid())[:2]
feature = ['wlanAPStatsTotDataBytes','wlanAPNumClients','wlanAPChannelThroughput','staSignalToNoiseRatio']
#finalDf = gen_final_pandas(gen_feature_pandas(feature,180,AP_bssid), 180, AP_bssid)
x = np.vstack((func(feature[0], 20, AP_bssid[0]),func(feature[1], 20, AP_bssid[0])))
x = np.vstack((x,func(feature[2], 20, AP_bssid[0])))
x = np.vstack((x,func(feature[3], 20, AP_bssid[0])))
print x



'''
finalDf = gen_feature_pandas(feature,35,AP_bssid)

targets = []
for i in range(len(AP_bssid)):
  targets.append(i)



fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)

colors = cm.rainbow(np.linspace(0, 1, len(AP_bssid)))
for target, colors in zip(targets,colors):
    indicesToKeep = finalDf['target'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = colors
               , s = 50)

ax.grid()

plt.savefig("20radio35time4fe.png")
'''