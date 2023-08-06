import numpy as np
import pandas as pd
import csv
import re
from merge import *
from extract import *

def gen_feature_pandas(feature, time, AP_radio, AP_bssid): 
  radio_num = len(AP_bssid)
  feature_num = len(feature)
  x = np.vstack((func1(feature[0], time, AP_bssid[0]),func(feature[1], time, AP_radio[0])))
  x = np.vstack((x,func(feature[2], time, AP_radio[0])))
  x = np.vstack((x,func(feature[3], time, AP_radio[0])))
  x = np.vstack((x,func(feature[4], time, AP_radio[0])))
  x = np.vstack((x,func(feature[5], time, AP_radio[0])))
  x = np.vstack((x,func(feature[6], time, AP_radio[0])))
  for i in range(1,radio_num):
    y = np.vstack((func1(feature[0], time, AP_bssid[i]),func(feature[1], time, AP_radio[i])))
    for j in range(2,feature_num):
      y = np.vstack((y,func(feature[j], time, AP_radio[i])))
    x = np.hstack((x,y))
    y = np.array([]) 
  x = np.transpose(x) 

  gg = np.ones((time-1)*radio_num)
  for i in range(1,radio_num):
    for j in range(time-1):
      gg[(time-1)*i+j] = gg[(time-1)*i+j]+i
  df1 = pd.DataFrame(x,columns =feature)     
  df2 = pd.DataFrame(gg,columns =['target']) 
  finalDf = pd.concat([df1, df2[['target']]], axis = 1)
  return finalDf

AP_radio = merge_radio(extract_radio())
AP_bssid = merge_bssid(extract_bssid())
feature = ['staSignalToNoiseRatio','wlanAPNumClients','wlanAPStatsTotDataBytes','wlanAPChannelThroughput','wlanAPChRxUtilization','wlanAPChTxUtilization','wlanAPChUtilization']
finalDf = gen_feature_pandas(feature,300,AP_radio,AP_bssid)
finalDf.to_csv('out.csv')
