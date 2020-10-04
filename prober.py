#! /usr/bin/env python
from easysnmp import Session, exceptions
from time import time,sleep
import sys
args = sys.argv[1].split(':')
ip_addr = args[0]
port = int(args[1])
community = args[2]
frequency = float(sys.argv[2])
interval = 1/frequency
sample_size = int(sys.argv[3])
oids = ['1.3.6.1.2.1.1.3.0']
oids.append(sys.argv[4:])
