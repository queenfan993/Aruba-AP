END=300

features=('wlanAPChRxUtilization' 'wlanAPChTxUtilization' 'wlanAPChUtilization' 'wlanAPStatsTotMgmtBytes' 'wlanAPStatsTotCtrlBytes' 'wlanAPStatsTotDataBytes' 
		'wlanAPChannelThroughput' 'apBSSBwRate' 'apTransmitRate' 'apRecieveRate' 'wlanAPNumClients' 'apBSSTxBytes' 'apBSSRxBytes' 'staSignalToNoiseRatio' 'wlanAPCurrentChannel'
		'apChannelBwRate' 'nUserApBSSID' 'wlanAPFrameBandwidthRate' 'wlanStaFrameBandwidthRate' 'staBwRate')
mkdir -p ${features[*]}

for i in $(seq 1 $END);
do
	date +%c;
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.5.3.1.6.1.35 > wlanAPChRxUtilization/wlanAPChRxUtilization_${i}.csv & 
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.5.3.1.6.1.36 > wlanAPChTxUtilization/wlanAPChTxUtilization_${i}.csv & 
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.5.3.1.6.1.37 > wlanAPChUtilization/wlanAPChUtilization_${i}.csv & 
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.5.3.1.4.1.2 > wlanAPStatsTotMgmtBytes/wlanAPStatsTotMgmtBytes_${i}.csv & 
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.5.3.1.4.1.4 > wlanAPStatsTotCtrlBytes/wlanAPStatsTotCtrlBytes_${i}.csv &
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.5.3.1.4.1.6 > wlanAPStatsTotDataBytes/wlanAPStatsTotDataBytes_${i}.csv &
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.5.3.1.1.1.9 > wlanAPChannelThroughput/wlanAPChannelThroughput_${i}.csv &
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.1.3.5.1.12 > apBSSBwRate/apBSSBwRate_${i}.csv &
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.1.3.3.1.15 > apTransmitRate/apTransmitRate_${i}.csv &
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.1.3.3.1.16 > apRecieveRate/apRecieveRate_${i}.csv &
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.5.3.1.1.1.2 > wlanAPNumClients/wlanAPNumClients_${i}.csv &
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.1.3.5.1.9  > apBSSTxBytes/apBSSTxBytes_${i}.csv &
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.1.3.5.1.11  > apBSSRxBytes/apBSSRxBytes_${i}.csv &
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.1.2.2.1.7 > staSignalToNoiseRatio/staSignalToNoiseRatio_${i}.csv & 
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.5.3.1.1.1.1 > wlanAPCurrentChannel/wlanAPCurrentChannel_${i}.csv & 
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.1.3.5.1.2 > apChannelBwRate/apChannelBwRate_{i}.csv &
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.4.1.2.1.11 > nUserApBSSID/nUserApBSSID_{i}.csv &
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.5.3.1.1.1.14 > wlanAPFrameBandwidthRate/wlanAPFrameBandwidthRate_{i}.csv &
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.5.3.2.1.1.20 > wlanStaFrameBandwidthRate/wlanStaFrameBandwidthRate_{i}.csv &
	snmpwalk -v 2c -c  140.112.25.114 1.3.6.1.4.1.14823.2.2.1.1.2.3.1.5 > staBwRate/staBwRate_{i}.csv &
	sleep 60;
done

