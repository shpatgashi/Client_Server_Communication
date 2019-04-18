import socket
import threading
import random
from _datetime import datetime
from math import pi
from math import sqrt

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ss.bind((host, port))

    def listen(self):
        self.ss.listen(5)
        while True:

            conns, addr = self.ss.accept()
            print("Serveri u konektua me klientin  " + addr[0] + " ne portin " +  str(addr[1]) + "\n")
            conns.settimeout(60)
            threading.Thread(target=self.listenToConns, args=(conns, addr)).start()
    
    def listenToConns(self, conns, addr):
        size = 1024
        while True:
            try:
                data = conns.recv(size)
                data = data.decode("utf-8")
                p = self.datastartswith(data)
                p = str(p)
                conns.send(str.encode(p))

            except :
                conns.close()
                return False


    def datastartswith(self, data):
        data = data.lower()
        if data.startswith("ipaddress"):
            return self.ipaddress(self.addr)
        elif data.startswith("numri i portit"):
            return self.numriportit(self.addr)
        elif data.startswith("bashketingellore"):
            data.replace("bashketingellore", "")
            return self.bashketingellore(data[16:])
        elif data.startswith("printimi"):
            data.replace("printimi", "")
            return self.printimi(data[8:])
        elif data.startswith("emri i kompjuterit"):
            return self.emrikompjuterit()
        elif data.startswith("koha"):
            return self.koha()
        elif data.startswith("loja"):
            return self.loja()
        elif data.startswith("fibonacci"):
            return self.fibonacci(data.split()[1])
        elif data.startswith("konvertimi"):
             return self.konvertimi(data)
        elif data.startswith("gjeje numrin"):
                return self.guessNumber(data.split()[2])
        elif data.startswith("rrenja katrore"):
                return self.squareRoot(data.split()[2])
        else:
            return "Keni shtypur opsionin gabim! Provoni perseri."
    def ipaddress(self, adresa):
        try:
            return adresa[0]
        except:
            return "Nuk mundemi te gjenerojme IP Addressen"
    def numriportit(self,adresa):
        try:
            return adresa[1]
        except:
            return "Nuk mundemi te gjenerojme nr e portit"
    def fibonacci(self, a):
        i = 1
        x = 0
        y = 1
        sum = 0

        while i < int(a):
            sum = x + y
            x = y
            y = sum
            i += 1
        return sum
    def bashketingellore(self, text):
        i = 0
        X= 0
        text = text.lower()
        try:
            for i in text:
                 if i in "qwrtpsdfghjklzxcvbnm" :
                     X += 1

            return X
        except:
            return "Nuk mundemi te i numrojme bashketingelloret"
    def printimi(self, testi):
        testi =  testi.strip()
        return testi

    def emrikompjuterit(self):
        try:
            return socket.gethostname()
        except:
            return "Nuk mundemi te gjenerojme emrin e kompjuterit "
    def koha(self):
        try:
            time = datetime.now()
            return time.strftime("%H:%M:%S-%D")
        except ConnectionAbortedError:
            print("Time could not be generated")

    def loja(self):
        a =(random.randint(1,50) , random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),)
        return (str(a))


    def konvertimi(self,data):
        data = data.lower()
        data= data.split(" ")
        if data[1] == "kilowatttohorsepower":
            return self.kwtohp(data[2])
        elif data[1] == "horsepowertokilowatt":
            return self.hptokw(data[2])
        elif data[1] == "degreestoradians":
            return self.degtorad(data[2])
        elif data[1] == "radianstodegrees":
            return self.radtodeg(data[2])
        elif data[1] == "gallonstoliters":
            return self.galtolit(data[2])
        elif data[1] == "literstogallons":
            return self.littogal(data[2])
        else:
            return "Ka ndodhur nje gabim"

    def guessNumber(self, num):
        b = (random.randint(1, 10))

        if( int(num) == b):
            return "Keni gjetur numrin random"
        else:
            return "Gabim !!"
    def squareRoot(self, num):
        b = sqrt(float(num))
        return b


    def kwtohp(self,value):
        return (int(value)* 1.341)

    def hptokw(self,value):
        return int(value)/1.341

    def degtorad(self,value):
        return (int(value)*pi/180)

    def radtodeg(self,value):
        return (int(value)*180/pi)

    def galtolit(self,value):
        return (int(value)*3.785)

    def littogal(self,value):
        return (int(value)/3.785)






ThreadedServer('localhost', 12001).listen()
