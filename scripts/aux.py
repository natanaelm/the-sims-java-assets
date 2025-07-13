import struct
def readUnsignedInt(f):
	return struct.unpack(">I", f.read(4))[0]
def readInt(f):
	return struct.unpack(">i", f.read(4))[0]
	
def readUnsignedShort(f):
	return struct.unpack(">H",f.read(2))[0]
def readShort(f):
	return struct.unpack(">h",f.read(2))[0]

def readUnsignedByte(f):
	return struct.unpack(">B", f.read(1))[0]
def readByte(f):
	return struct.unpack(">b", f.read(1))[0]
