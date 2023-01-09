import socket 
import time
import threading
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
threads = []
while i <= range2:
  t = threading.Thread(target=scan_port,args=(IPtest,i))
  threads.append(t)
  t.start()
  i= i+1
for t in threads:
  t.join()
end = time.time()
diff= end - start
print("résolu en :", diff)
