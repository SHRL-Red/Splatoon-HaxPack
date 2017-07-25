import struct
 
 
def readByte(file):
    return struct.unpack("B", file.read(1))[0]
 
def readu16be(file):
    return struct.unpack(">H", file.read(2))[0]
 
def readu16le(file):
    return struct.unpack("<H", file.read(2))[0]

def readu32be(file):
    return struct.unpack(">I", file.read(4))[0]
 
def readu32le(file):
    return struct.unpack("<I", file.read(4))[0]

def readu64be(file):
    return struct.unpack(">q", file.read(8))[0]
 
def readfloatbe(file):
    return struct.unpack(">f", file.read(4))[0]
 
def readfloatle(file):
    return struct.unpack("<f", file.read(4))[0]
 
 
   
def getString(file):
    result = ""
    tmpChar = file.read(1)
    while ord(tmpChar) != 0:
        result += tmpChar
        tmpChar =file.read(1)
    return result
