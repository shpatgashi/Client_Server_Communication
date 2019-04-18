import  socket

serverName = 'localhost'
port = 12000

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect((serverName, port))

mbyllja = ""

while True:
        var =input("Zgjedheni njeren nga metodat : \nIP Address(1)\nNumri i Portit(2)\nBashketingellore(3)\nPrintimi(4)\nEmri i kompjuterit(5)\nKoha(6)\nLoja(7)"
                   "\nFibonacci(8)\nKonveritmi(9)\nMetoda1(10)\nMetoda2(11) ")

        s.sendall(str.encode(var))

        r = s.recv(1024).decode("utf-8")
        print(r)






        s.close()



