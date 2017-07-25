import sys
import struct
from struct import pack
import os
from util import *

#This is a python version of RTB bms script with more visuals

bfres = open(sys.argv[1], "rb+")
dds = str(sys.argv[2])
texID = int(sys.argv[3])

FTEXARRAY = []
NAMEARRAY = []

bfres.seek(0x24)
FILEJUMP = bfres.tell()
FILEOFFSET = readu32be(bfres)
FILEJUMP = FILEJUMP + FILEOFFSET

bfres.seek(FILEJUMP)
HEADERSIZE = readu32be(bfres)
FILETOTAL = readu32be(bfres)
bfres.seek(0x10,1)

for i in range(FILETOTAL):
    bfres.seek(8,1)
    NAMEOFFSETPLUS = bfres.tell()
    NAMEOFFSET = (readu32be(bfres) + NAMEOFFSETPLUS)
    FTEXOFFSETPLUS = bfres.tell()
    FTEXOFFSET = (readu32be(bfres) + FTEXOFFSETPLUS)
    FTEXARRAY.append(FTEXOFFSET)

    BACKTOLIST = bfres.tell()
    bfres.seek(NAMEOFFSET)
    NAME = getString(bfres)
    NAMEARRAY.append(NAME)
    bfres.seek(BACKTOLIST)

bfres.seek(0xD070)

for i in range(FILETOTAL):
    bfres.seek(FTEXARRAY[i])
    FTEX = readu32be(bfres)
    VERSION = readu32be(bfres)
    WIDTH = readu32be(bfres)
    HEIGHT = readu32be(bfres)
    bfres.seek(4,1)
    MIPCOUNT = readu32be(bfres)
    bfres.seek(2,1)
    #bfres.seek(10,1)
    WRITECHUNK = bfres.tell()
    FORMAT1 = readByte(bfres)
    FORMAT2 = readByte(bfres)
    if FORMAT2 == 0x31 or 0x33:
        FORMAT1 = 0
    bfres.seek(8,1)
    LENGTH = readu32be(bfres)
    bfres.seek(0x12,1)
    SWIZZING = readByte(bfres)
    bfres.seek(0x75,1)
    DATAOFFSETPLUS = bfres.tell()
    DATAOFFSET = (readu32be(bfres) + DATAOFFSETPLUS)
    MIPOFFSET = readu32be(bfres)
    print("%s ID:%d Has %s Mips %s Swizzing" % (NAMEARRAY[i],int(i),MIPCOUNT,hex(SWIZZING)))
    if i == texID:
        os.system("TexConv2.exe -i %s -o tmp.gtx -swizzle %s -minmip %s" %(dds,int(SWIZZING),int(MIPCOUNT)))
        GTX = open("tmp.gtx", 'rb')
        GTX.seek(0x56)
        bfres.seek(WRITECHUNK)
        bfres.write(GTX.read(2))
        GTX.seek(0x74)
        bfres.seek(WRITECHUNK + 0x1E)
        bfres.write(GTX.read(4))
        GTX.seek(0xFC)
        magic = 0
        while magic != 0x424C4B7B00000020:
            magic = readu64be(GTX)
        GTX.seek(-8,1)
        texOffset = (GTX.tell() - 0xFC)
        texEnd = (os.path.getsize("tmp.gtx") - 0x11C)
        texSec = (texEnd - (texOffset + 0x20))
        GTX.seek(0xFC)
        bfres.seek(DATAOFFSET)
        print(hex(texOffset))
        print(hex(texEnd))
        print(hex(texSec))
        bfres.write(GTX.read(texOffset))
        if texEnd != texOffset:
            GTX.seek(0x20,1)
            bfres.write(GTX.read(texSec))
GTX.close()
bfres.close()
