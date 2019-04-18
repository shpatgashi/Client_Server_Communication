import  socket

serverName = '10.1.13.81'
port = 12001


s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect((serverName, port))

print("Zgjedheni njeren nga metodat e dhena (Kujdesuni qe te jepni tekstin pa gabime dhe ne formatin e duhur): \nIPADDRESS \nNUMRI I PORTIT \nBASHKETINGELLORE(hapsire)Teksti \n"
      +"PRINTIMI(hapsire)Teksti \nEMRI I KOMPJUTERIT\nKOHA\nLOJA\nFIBONACCI(hapsire)Numer\nKONVERTIMI(hapsire)Lloji i konvertimit(hapsire) Numer\nGJEJE NUMRIN (hapsire) Numer\nRRENJA KATRORE (hapsire) Numer ")
while True:

        var = input("Shkruani opsionin (Shtypni P per te perfunduar): ")
        var = var.upper()
        if(var == "P"):
            s.close()
            break
        else:
            s.send(str.encode(var))
            r = s.recv(1024).decode("utf-8")
            print(r)









