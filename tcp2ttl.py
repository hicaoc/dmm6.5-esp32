import network
import socket
import time
from machine import UART,Pin

led=Pin(2,Pin.OUT) 
SSID="XXXXX"
PASSWORD="password"
port=10000
wlan=None
listenSocket=None
conn=None
uart=UART(2, 115200)
uart.init(115200, bits=8, parity=None, stop=1)

def accept_handler (sck:socket.socket):
 
    global conn
    conn, addr = sck.accept ()
    conn.setsockopt(socket.SOL_SOCKET, 20, process_handler)
    # set a readable callback

def process_handler (sck:socket.socket):

    global uart
    # recv the data and send it bcak.
    data = sck.recv (1024)
    print("CMD: ",data)    
    uart.write(data)

def connectWifi(ssid,passwd):
  global wlan
  wlan=network.WLAN(network.STA_IF)         #create a wlan object
  wlan.active(True)                         #Activate the network interface
  wlan.disconnect()                         #Disconnect the last connected WiFi
  wlan.connect(ssid,passwd)                 #connect wifi
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
  return True

#Catch exceptions,stop program if interrupted accidentally in the 'try'
try:
  connectWifi(SSID,PASSWORD)
  ip=wlan.ifconfig()[0]                     #get ip addr
  listenSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)            #create socket
  listenSocket.bind((ip,port))              #bind ip and port
  listenSocket.listen(5)                    #listen message
  listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  listenSocket.setsockopt(socket.SOL_SOCKET, 20, accept_handler) #Set the value of the given socket option  
  led.value(1)

  while True:
      if uart.any():
        led.value(1)
        bin_data=uart.readline()
        print("RSP:",bin_data)
        if conn == None:
            print("conn is None, sleep 1")
            time.sleep(1)
            continue
        conn.send(bin_data)   
      else:
        #print("Uart not have data, sleep 1")
        led.value(0)
        time.sleep(0.2)
        led.value(1)
except:
  if(listenSocket):
    listenSocket.close()
  wlan.disconnect()
  wlan.active(False)

