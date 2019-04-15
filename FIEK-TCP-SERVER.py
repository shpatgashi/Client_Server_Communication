import socket
import threading
import random
import datetime
from math import pi


class ThreadedServer(object):
    def __init__(self):
        host = "localhost"
        port = 12000
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ss.bind((host, port))

    def listen(self):
        self.ss.listen(5)
        while True:
            conns, addr = self.ss.accept()
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
                print("Soketi u mbyll")
                conns.close()
                return False


    def datastartswith(self, data):
        data = data.lower()
        if data.startswith("ipaddress"):
            return self.ipaddress(self.ss.addr)
        elif data.startswith("numriiportit"):
            return self.numriportit(self.ss.addr)
        elif data.startswith("bashketingellore"):
            data.replace("bashketingellore", "")
            return self.bashketingellore(data[16:])
        elif data.startswith("printimi"):
            data.replace("printimi", "")
            return self.printimi(data[8:])
        elif data.startswith("emriikompjuterit"):
            return self.emrikompjuterit()
        elif data.startswith("koha"):
            return self.koha()
        elif data.startswith("loja"):
            return self.loja()
        elif data.startswith("fibonacci"):
            return self.fibonacci(data.split()[1])
        elif data.startswith("konvertimi"):
             return self.konvertimi(data)

    def ipaddress(self, address):
        try:
            return address()[0]
        except:
            return "Nuk mundemi te gjenerojme IP Addressen"
    def numriportit(self,addr):
        try:
            return addr()[1]
        except:
            return "Nuk mundemi te gjenerojme nr e portit"
    def emrikompjuterit(self):
        try:
            return socket.gethostname()
        except:
            return "Nuk mundemi te gjenerojme emrin e kompjuterit "
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
    def loja(self):
        for i in range (1,8):
            a =(random.randint(1,50))
            b =(random.randint(1,50))
            c =(random.randint(1,50))
            d =(random.randint(1,50))
            e = (random.randint(1, 50))
        return (a,b,c,d,e)

    def printimi(self, testi):
        testi =  testi.strip()
        return testi

    def koha(self):
        try:
            time = datetime.datetime().strftime('%H:%M:%S-%D')
            return time
        except ConnectionAbortedError:
            print("Time could not be generated")
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
            return "Ka ndodhur nje gabim rip"



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





ThreadedServer().listen()
