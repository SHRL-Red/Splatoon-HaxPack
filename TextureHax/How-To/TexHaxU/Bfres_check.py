import sys
import struct
from struct import pack
import os
from util import *

#This is a python version of RTB bms script with more visuals

bfres = open(sys.argv[1], "rb+")

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
    print("%s ID:%d Has %s Mips" % (NAMEARRAY[i],int(i),MIPCOUNT))
    bfres.seek(8,1)
    outfile = open("Convert" + "/" + str(int(i)) + ".gtx", "wb")
    outfile.write("\x47\x66\x78\x32\x00\x00\x00\x20\x00\x00\x00\x07\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x42\x4C\x4B\x7B\x00\x00\x00\x20\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x0B\x00\x00\x00\x9C\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00\x00\x0A\x00\x00")
    bfres.seek(WRITECHUNK)
    outfile.write(bfres.read(0x86))
    outfile.write("\x42\x4C\x4B\x7B\x00\x00\x00\x20\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x0C\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    bfres.seek(DATAOFFSET)
    outfile.write(bfres.read(LENGTH))
    outfile.write("\x42\x4C\x4B\x7B\x00\x00\x00\x20\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    outfile.seek(0x44)
    outfile.write(struct.pack(">I",WIDTH))
    outfile.write(struct.pack(">I",HEIGHT))
    outfile.seek(0x50)
    outfile.write(struct.pack(">I",1))
    outfile.seek(0xF0)
    outfile.write(struct.pack(">I",LENGTH))
    outfile.close()
bfres.close()
