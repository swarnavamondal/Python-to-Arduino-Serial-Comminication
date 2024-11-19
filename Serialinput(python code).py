import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portList = []

for one in ports:
    portList.append(str(one))
    print(str(one))

com = input("select com port")

for i in range(len(portList)):
    if portList[i].startswith("COM" + str(com)):
        use = "COM" + str(com)
        print(use)
serialInst.baudrate=9600
serialInst.port= use
serialInst.open()
while True:
    command = input("enter a string :")
    serialInst.write(command.encode('UTF-8'))
    #if serialInst.in_waiting > 0:  
    response = serialInst.readline().decode('UTF-8').strip()  
    print("Arduino has received:", response)

    exit()
