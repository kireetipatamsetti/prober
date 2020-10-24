from easysnmp import Session
import sys
import time
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

while (sample_number < sample_size):
    request_time = time.time()
    latest_probes = session.get(oids)
    response_time = time.time()
    
                
                
    
    