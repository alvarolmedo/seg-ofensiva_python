from scapy.all import *
import argparse

cerrado = 0

def ping(direccion):
	try:
		ping = sr1(IP(dst=direccion)/ICMP())
		print('Host arriba')
		return True
	except:
		print('Host abajo')
		return False


def scannerSYN(direccion, puerto):
	try:
		s_port = random.randint(9,1000)
		SYNACK = None
		SYNACK = sr1(IP(dst=direccion)/TCP(sport=s_port, dport=puerto, flags='S'), verbose=0, timeout=1)
		if SYNACK is None:
			print(f'+Puerto {str(puerto)} filtrado.')
		elif str(SYNACK[TCP].flags) == 'SA':
			print(f'+Puerto {str(puerto)} abierto.')
			RST = IP(dst=direccion)/TCP(sport=s_port, dport=puerto,flags = 'R')
			send(RST, verbose = 0)
		elif str(SYNACK[TCP].flags) == 'RA':
			print(f'+Puerto {str(puerto)} cerrado.')
			global cerrado
			cerrado += 1
	except Exception:
		# Si salta cualquier fallo: cerramos conexion 
		RST = IP(dst=direccion)/TCP(sport=s_port, dport=puerto,flags = 'R')
		send(RST)
		print(f'No he podido escanear {d_addr} en el puerto {str(puerto)}')


def parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('ip')
	parser.add_argument('minport', type=int)
	parser.add_argument('maxport', type=int)
	args = parser.parse_args()
	return args


def main():
	args = parser()
	#ping(args.ip)
	for port in range(args.minport, args.maxport, 1):
		scannerSYN(args.ip, port)
	global cerrado
	print(f'Puertos cerrados: {str(cerrado)}')


if __name__ == '__main__':
	main()