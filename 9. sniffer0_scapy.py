from scapy.all import *

sniff(prn=lambda x: print(x), count=1)