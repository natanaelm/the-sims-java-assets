import struct
import animdata

fl = open('../ts3wa/map_macromap.bin', 'rb')
hdr = struct.unpack('>BBBBB', fl.read(5))
mWidth = hdr[1]
mHeight = hdr[2]
mLength = mWidth * mHeight
byteMap = fl.read(mLength) #readbytemap
print(f'{mWidth}:{mHeight}')

def readPos(current, count):
	index = 0
	var5 = []
	for i in range(count * 3):
		var8 = struct.unpack('>h', fl.read(2))[0]
		if (i % 3 == 0):
			if(input() == 'q'): exit(1)
			var5.append(current[var8]) #qual animacao colocar no mapa
			print(f'\n{current[var8]}:')
		else:
			var5.append(var8) #coordenadas
			print(f'{var8},')

count1 = fl.read(1)[0]
print(count1,'<<<')
if count1 > 0: readPos(animdata.wa['a'], count1)
count2 = fl.read(1)[0]
print(count2,'>>>')
if count2 > 0: readPos(animdata.wa['b'], count2)

fl.close()
