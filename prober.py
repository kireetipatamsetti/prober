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
