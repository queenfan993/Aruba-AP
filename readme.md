## Project Description
- Fetch the NTU wireless data with the SNMP portocol with Aruba AP MIBs number to get the raw data
- Extract the features from the data and analysis the correlations between the features 

## installtions
- snmpwalk

## monitor.sh :
The password of the APs are hidden
The contents in the folder are the remaining raw data. 

[features] can be :
* staSignalToNoiseRatio
* wlanAPNumClients
* wlanAPStatsTotDataBytes
* wlanAPChUtilization
* wlanAPChTxUtilization
* ...


### aruba-wlan.my
- The mibs numbers we can used in snmp to fetch the features
- In order to maintain confidentiality, some aruba.my files has been concealed. 

### extract.py
- After we ran the monitor.sh, extract the features from the raw data 
- Extract the featrues by radio or bssid for the different types of Aruba APs

### merge.py
- To merge the radio or the bssid raw data

### PrincipalComponentAnalysis.py
- Use the PCA algorithm to find out the correlation of target features


### LocallyLinearEmbedding.py
- Use Locally Linear Embedding algorithm to preserve the local linear relationships between data points


### gen_pandas.py
- An experiment to generate a matrix and verify the results using CSV.












