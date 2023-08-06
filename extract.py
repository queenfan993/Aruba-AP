import numpy as np
import csv
import re

#when generating csv, we need to check if the data can be extract from radio or just can be extract in bssid 
#feature only can obtain from bssid need to use the extract1 and func1

def extract(feature, time, name):
  x = []  
  f = open(feature+'/'+feature+'_'+str(time)+'.csv', 'r')
  for row in csv.reader(f):
    if str(row).find(name) > 0:
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
      if len(extract(feature,i,name)) > 0:
        x.append(float(sum(extract(feature, i, name)))/float(len(extract(feature,i,name))))
      else:
        x.append(0)   
    return x  
    
  else:
    x = []
    for i in range(1,time):
      x.append(sum(extract(feature, i, name)))
    return x

def extract1(feature, time, name):
  x = []  
  f = open(feature+'/'+feature+'_'+str(time)+'.csv', 'r')
  for row in csv.reader(f):
    for bssid_or_radio in range(len(name)):
      if str(row).find(name[bssid_or_radio])>0:
        x.append(int(re.split('[::,:,\',\s,\.]',str(row))[-2]))   
  f.close()
  return x

def func1(feature, time, name):
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
      if len(extract1(feature,i,name)) >0:
        x.append(sum(extract1(feature, i, name))/len(extract1(feature,i,name)))
      else:
        x.append(0)   
    return x  
    
  else:
    x = []
    for i in range(1,time):
      x.append(extract(feature, i, name)[0])
    return x
 
  





