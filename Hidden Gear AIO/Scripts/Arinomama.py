from tcpgecko import TCPGecko
from binascii import hexlify
import os, sys, time

if os.path.isfile("./SAV_IP") == True:
    sav_ip = (open("./SAV_IP", "r").read())
    print ("\nEnter you Wii U IP Address: (Or keep it blank to use your saved one.)")
else:
    print ("\nEnter you Wii U IP Address:")

ip = raw_input(">> ") or sav_ip

tcp = TCPGecko(ip)

save = open("./SAV_IP", "w")
save.write(ip)
save.close()

diff = 0x0
if hexlify(tcp.readmem(0x12CDADA0, 4)) == "000003f2": #Loadiine and Geckiine
    diff = 0x0;
elif hexlify(tcp.readmem(0x12CDCDA0, 4)) == '000003f2': #Elf TCPGecko w/o codehandler
    diff = 0x2000;
elif hexlify(tcp.readmem(0x12CE2DA0, 4)) == '000003f2': #Something, it's there but I'm not sure
    diff = 0x8000;
elif hexlify(tcp.readmem(0x12CE3DA0, 4)) == '000003f2': #Codehandler
    diff = 0x9000;
    print("codehandler")
    
tcp.pokemem(0x12BB9BC0, 0x00000004)
tcp.pokemem(0x12BD2820, 0x00000004)
tcp.pokemem(0x12BA0F60, 0x00000004)
tcp.pokemem(0x12CD70B0, 0x00000000)
tcp.pokemem(0x12CD3EA0, 0x00000000)
tcp.pokemem(0x12CD8BB0, 0x00000000)
tcp.pokemem(0x12CD1D80, 0x00000000)
tcp.pokemem(0x12CD1D84, 0x00000000)
tcp.pokemem(0x12CD1D88, 0x00000000)

tcp.s.close()
print("Testfire Gear Poke Complete.")

import os
os.system('tool.bat')
