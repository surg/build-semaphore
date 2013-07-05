import serial
import time
CMD_RED = 'Vkl__Krasnyj]'
CMD_YELLOW = 'Vkl__Sinij__]'
CMD_GREEN = 'Vkl__Zelenyj]'
CMD_OFF = 'Vykl_Vse____]'

class Arduino(object):
	def __init__(self, port):
		self.port = port
		self.current = ''
		self.ser = serial.Serial(self.port, 9600)

	def update(self, statuses):
		red = False
		yellow = False
		for v in statuses.values():
			red = red or v.startswith('red')
			yellow = yellow or v.startswith('yellow')

		cmd = CMD_GREEN	
		if red: 
			cmd = CMD_RED
		elif yellow:
			cmd = CMD_YELLOW

		if self.current != cmd:
			print 'arduino: Updating to %s, port: %s' % (cmd, self.port)
			ser = self.ser
			response = ser.write(CMD_OFF)
			response = ser.write(cmd)
			self.current = cmd
			print 'arduino response:', response
		else:
			print 'arduino: Status not changed, nothing to do'