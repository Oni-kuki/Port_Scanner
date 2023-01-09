import socket 
import time

def scan_port(ip, port):
  s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  result = s.connect_ex((ip, port))

  if result == 0:
    print(f"Le port {port} est ouvert")
    with open(".\portcommun.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if str(port) in line:
                print("{}".format(line))
  else:
    print(f"Le port {port} est fermé")
  s.close()

IPtest = input("quel hote: ")
i= int(input("range du premier :  "))
range2 = int(input("range 2 : "))

start = time.time()

while i <= range2:
    scan_port(IPtest,i)
    i= i+1
end = time.time()
diff= end - start
print("résolu en :", diff)
