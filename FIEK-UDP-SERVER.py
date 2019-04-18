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
    data= data.split(" ")
    if data[1] == "kilowatttohorsepower":
        return kwtohp(data[2])
    elif data[1] == "horsepowertokilowatt":
        return hptokw(data[2])
    elif data[1] == "degreestoradians":
        return degtorad(data[2])
    elif data[1] == "radianstodegrees":
        return radtodeg(data[2])
    elif data[1] == "gallonstoliters":
        return galtolit(data[2])
    elif data[1] == "literstogallons":
        return littogal(data[2])
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


def kwtohp(value):
    return (int(value)* 1.341)

def hptokw(value):
    return int(value)/1.341

def degtorad(value):
    return (int(value)*pi/180)

def radtodeg(value):
    return (int(value)*180/pi)

def galtolit(value):
    return (int(value)*3.785)

def littogal(value):
    return (int(value)/3.785)




host = "localhost"
port = 12000

ss= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ss.bind((host, port))
while True:
    data, addr = ss.recvfrom(1024)
    print("Serveri u konektua me klientin  " + addr[0] + " ne portin " + str(addr[1]) + "\n")
    data = data.decode("utf-8").lower()
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
        print(p)
        ss.sendto(str.encode(p),addr)

    except:
        print("Ka ndodhur nje gabim")


