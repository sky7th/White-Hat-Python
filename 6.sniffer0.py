from socket import *
import os

def sniffing(host):
	if os.name == 'nt':
		sock_protocol = IPPROTO_IP
	else:
		sock_protocol = IPPROTO_ICMP
		
	sniffer = socket(AF_INET, SOCK_RAW, sock_protocol)
	sniffer.bind((host, 0))
	sniffer.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
	
	if os.name == 'nt':
		sniffer.ioctl(SIO_RCVALL, RCVALL_ON)
		
	print (sniffer.recvfrom(10000))
	
	if os.name == 'nt':
		sniffer.ioctl(SIO_RCVALL, RCVALL_OFF)	


def main():
	host = gethostbyname(gethostname())
	print('START SNIFFING at [%s]' %host)
	sniffing(host)
	
	
if __name__ == '__main__':
	main()

