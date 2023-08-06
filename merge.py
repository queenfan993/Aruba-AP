import numpy as np
import pandas as pd
import csv
import re

def extract_radio():
  x = []  
  crt = 0
  f = open('wlanAPNumClients/wlanAPNumClients_1.csv', 'r')
  for row in csv.reader(f):
    if crt%3 == 0:
      x.append(re.split('[.]',str(row))[16:16+7])
    crt = crt+1    
  f.close()
  return x

def extract_bssid():
  x = []  
  f = open('wlanAPNumClients/wlanAPNumClients_1.csv', 'r')
  for row in csv.reader(f):
        x.append(re.split('[.,=]',str(row))[16+7:16+7+6])   
  f.close()
  return x  

def merge_bssid(x):
 	y = []
	temp = '.'
	for i in range(len(x)):
		y.append(temp.join(x[i]))
		temp = '.'
	z = [y[i:i+3] for i in range(0,len(y),3)]
	return z

def merge_radio(x):
  y = []
  temp = '.'
  for i in range(len(x)):
    y.append(temp.join(x[i]))
    temp = '.'
  z = [y[i] for i in range(0,len(y))]
  return z  
 
  





