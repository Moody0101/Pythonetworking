import socket
from dataclasses import dataclass


@dataclass
class PortScanner:
	TARGET: str = '127.0.0.1'
	PORTS: range | int | None = None
	s: socket.socket = socket.socket(socket.AF_INET, SOCK_STREAM)
	
	def scanHTTP(self) -> bool:
		return self.scanPORT(80)

	def scanPORT(self, p: int) -> bool:
		try:
			self.s.connect((self.TARGET, p))
			return True
		except:
			return False

	def scan(self):
		for i in self.PORTS:
			if self.scanPORT(i): print(f"{i} is OPEN \nService: {self.s.getservbyport(i, 'tcp')}")
			else: print(f'{i} is Closed')
