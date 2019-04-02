from socket import *
import os

def recvData(sock):
	data = ''
	try:
		data = sock.recvfrom(65565)
	except timeout:
		data = ''
		
	return data[0]
	

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
	
	count = 1
	try:
		while True:
			data = recvData(sniffer)
			print ('SNIFFED [%d] %s\n' %(count, data[:20]))
			count += 1
	except KeyboardInterrupt:  # Ctrl-C key input
		if os.name == 'nt':
			sniffer.ioctl(SIO_RCVALL, RCVALL_OFF)
	
def main():
	host = gethostbyname(gethostname())
	print('START SNIFFING at [%s]' %host)
	sniffing(host)
	
	
if __name__ == '__main__':
	main()