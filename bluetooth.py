import serial


ser = serial.Serial('COM8',9600,timeout=1)
def writedata(a):
	ser.write(a.encode())
while True:
	i = input("what data to send")
	writedata(i)
	if i=='q':
		break