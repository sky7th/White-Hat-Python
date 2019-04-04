from scapy.all import *

def showPacket(packet):
	print(packet.show())
	
def main(filter):
	sniff(filter=filter, prn=showPacket, count=1)
	
if __name__ == '__main__':
	filter = 'ip'
	main(filter)