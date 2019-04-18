import socket
import random
from _datetime import datetime
from math import pi
from math import sqrt

def ipaddress( adresa):
    try:
        return "IP Adresa e klientit eshte: "+ str(addr[0])
    except:
        return "Nuk mundemi te gjenerojme IP Addressen"
def numriportit(adresa):
    try:
        return "Klienti eshte duke perdorur portin "+ str(addr[1])
    except:
        return "Nuk mundemi te gjenerojme nr e portit"
def bashketingellore( text):
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
def printimi( testi):
    testi =  testi.strip()
    return testi

def emrikompjuterit():
    try:
        return socket.gethostname()
    except:
        return "Nuk mundemi te gjenerojme emrin e kompjuterit "
def koha():
    try:
        time = datetime.now()
        return time.strftime("%H:%M:%S-%D")
    except ConnectionAbortedError:
        print("Time could not be generated")

def loja():
    a =(random.randint(1,50) , random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),)
    return (str(a))

def fibonacci(a):
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

def konvertimi(data):
    data = data.lower()
    data = data.split(" ")
    if data[1] == "kilowatttohorsepower":
        return (float(data[2]) * 1.341)
    elif data[1] == "horsepowertokilowatt":
        return (float(data[2]) / 1.341)
    elif data[1] == "degreestoradians":
        return (float(data[2] * pi) / 180)
    elif data[1] == "radianstodegrees":
        return (float(data[2]) * 180 / pi)
    elif data[1] == "gallonstoliters":
        return (float(data[2]) * 3.785)
    elif data[1] == "literstogallons":
        return (float(data[2]) / 3.785)
    else:
        return "Ka ndodhur nje gabim"


def guessNumber( num):
    b = (random.randint(1, 5))

    if( int(num) == b):
        return "Keni gjetur numrin random"
    else:
        return "Gabim !! Numri eshte "+ str(b)
def squareRoot( num):
    b = sqrt(float(num))
    return b



host = "localhost"
port = 12000

ss= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ss.bind((host, port))
while True:
    data, addr = ss.recvfrom(128)
    print("Serveri u konektua me klientin  " + addr[0] + " ne portin " + str(addr[1]) + "\n")
    data = data.decode("utf-8").lower()
    print("Klienti " + addr[0] + " shtypi kete kerkese : " + data + "\n")

    try:

        if(data.startswith("ipaddress")):
            p = ipaddress(addr[0])
        elif data.startswith("numri i portit"):
            p = numriportit(addr[1])
        elif data.startswith("bashketingellore"):
            p = bashketingellore(data[16:])
        elif data.startswith("printimi"):
            p = printimi(data[9:])
        elif data.startswith("emri i kompjuterit"):
            p = emrikompjuterit()
        elif data.startswith("koha"):
            p = koha()
        elif data.startswith("loja"):
            p = loja()
        elif data.startswith("fibonacci"):
            p = fibonacci(data.split()[1])
        elif data.startswith("konvertimi"):
            p = konvertimi(data)
        elif data.startswith("gjeje numrin"):
            p = guessNumber(data.split()[2])
            p = guessNumber(data.split()[2])
        elif data.startswith("rrenja katrore"):
            p = squareRoot(data.split()[2])
        else :
            p = "Keni shtypur opsionin gabim! Provoni perseri!"
        p = str(p).upper()
        ss.sendto(str.encode(p),addr)
        print("Serveri i dergoi klientit " + addr[0] + " kete pergjigje " + p + "\n")


    except:
        print("Ka ndodhur nje gabim")


