from easysnmp import Session
import sys
import time

import easysnmp
args = sys.argv[1].split(':')
ipaddress = args[0]
port = args[1]
community = args[2]
sample_frequency = float(sys.argv[2])
sample_interval = 1/sample_frequency
sample_size = int(sys.argv[4:])
oids = ['1.3.6.1.2.1.1.3.0']
oids += sys.argv[4:]
sample_number = 0
old_probes = []
latest_probes = []
session = Session(hostname=ipaddress, remote_port=port,community=community,version=2)
old_time = 0
rates = []
timeouts = 0
while (sample_number < sample_size):
    request_time = time.time()
    try:
       latest_probes = session.get(oids)
    except easysnmp.EasySNMPTimeoutError:
        sample_number += 1
        timeouts += 1
        continue
    response_time = time.time()
    if (len(old_probes) == len(latest_probes)):
        if sample_frequency>1:
            time_difference = request_time - old_time
        else:
            time_difference = request_time - old_time
        
            if time_difference != 0:
                time_difference = int(time_difference)
            else:
                time_difference = int(sample_interval)
        for i in range(1, len(oids)):
            if latest_probes[i].snmp_type!="NOSUCHINSTANCE" and old_probes[i].snmp_type!="NOSUCHINSTANCE":
                latest_value = int(latest_probes[i].value)
                old_value = int(old_probes[i].value)
                if latest_value >= old_value:
                    rate = (latest_value - old_value) / time_difference
                    rates += [rate]

                else:
                    if latest_probes[i].snmp_type == "COUNTER" and old_probes[i].snmp_type == "COUNTER":
                        rate = ((2**32 + latest_value) - old_value) / time_difference
                        rates += [rate]
                    elif latest_probes[i].snmp_type == "COUNTER64" and old_probes[i].snmp_type == "COUNTER64":
                        rate = ((2**64 + latest_value) - old_value) / time_difference
                        rates += [rate]
            else:
                rates += [latest_probes[i].value]
        
        print(int(request_time, '| '+' | '.join(map(str, rates))))
        sample_number += 1
    
    rates = []
    old_probes = latest_probes.copy
    old_time = request_time
    if sample_interval > time.time() - request_time:
        time.sleep(sample_interval - time.time() + request_time)
    
    
    
    
                
    
    