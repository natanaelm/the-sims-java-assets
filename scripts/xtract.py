import json
import lnames
import struct
import aux

ts3 = {'folder': "ts3", 'size': 1416, 'img': 1,'anims': 707}
ts3a = {'folder': "ts3a", 'size': 1955, 'img': 2, 'anims': 798}
ts3wa = {'folder': "ts3wa", 'size': 1692, 'img':3, 'anims': 819}

streams = {} # {'imageid': [{}]}

def toName(index, s):
	if s == 1:
		return lnames.ts3Names[ lnames.ts3image[index] ]
	elif s == 2:
		return lnames.ts3aNames[ lnames.ts3aimage[index] ]
	elif s == 3:
		return lnames.ts3waNames[ lnames.ts3waimage[index] ]

def readSprite(fid):
	try:
		srcf = open(f"{fid.get('folder')}/image.bin","rb")
		destf = open(f"{fid.get('folder')}/image.json", 'w')
	except:
		print('Erro em image.*')
		return
	index = 0
	destf.write('[')
	while index < fid.get('size'):
		try:
			tp = struct.unpack(">Bhhhh", srcf.read(9)) #image_index, x, y, w, h
			destf.write(json.dumps(tp))
			if index != (fid.get('size') - 1): destf.write(',')
		except:
			break
		index+=1
	destf.write(']')
	destf.close()
	srcf.close()
	'''
	mykey = toName(tp[0], fid['img'])
		if mykey not in streams:
			streams[mykey] = []
			streams[mykey].append({'index': index, 'img': tp[0], \
		 'x':tp[1], 'y':tp[2], 'width':tp[3], 'height':tp[4]})
		else:
			streams[mykey].append({'index': index, \
		 'x':tp[1], 'y':tp[2], 'width':tp[3], 'height':tp[4]})
		index+=1
	for key in streams:
		doc = open(f"{fid.get('folder')}/texture_atlas/{key.split('.')[0]}.json", "w")
		json.dump(streams[key], doc)
		doc.close()
		print(key)
		#for kv in streams[key]:
		#	print(kv)
	'''

#readSprite(ts3wa)
#readSprite(ts3wa)
readSprite(ts3)
def dprint(s):
	debug = True
	if debug: print(s)

def readAnims(fid):
	try:
		fq = open(f"{fid.get('folder')}/animdata.bin", 'rb')
	except:
		dprint("File no exists!")
		return
	count = fid.get('anims')
	index = 0
	ft = open(fid['folder']+'/animdata.json', 'w')
	ft.write('[')
	maior = 0
	while index < count:# and input() != 'q':
		var5 = aux.readUnsignedByte(fq)
		if (var5 >maior): maior = var5
		animation = {#'length': var5,
		'frames': []}
		for var6 in range(0, var5): #add frames
			t = aux.readShort(fq)
			l = aux.readUnsignedByte(fq)
			frame = {'time': t, #'length': l,
			'objects': []}
			for var8 in range(0, l):#add objects
				ftype = aux.readUnsignedByte(fq) #data type / size equiv
				match ftype:
					case 0 | 11:# 0: draw sprite, 11: draw inverted
						mne = struct.unpack(">hhh", fq.read(6)) #sprite, x, y
					case 1 | 2 | 3 | 4 | 5 | 6 | 8:
						#4: fillRect 8:drawLine?
						mne = struct.unpack(">hhhh", fq.read(8)) #draw line x,y,x,y?
					case 7:
						mne = struct.unpack(">hh", fq.read(4)) # translate x,y?
					case 10:
						mne = struct.unpack(">b", fq.read(1)) #set color?
					case _:
						mne = ()
				frame['objects'].append((ftype,) + mne)
			animation['frames'].append(frame)
		result = json.dumps(animation)
		#dprint(result)
		ft.write(result)
		if index != count-1: ft.write(',')
		index+=1
	#dprint(f'{index},{maior}')
	fq.close()
	ft.write(']')
	ft.close()
#readAnims(ts3a)

def readColors(fid):
	try:
		srcf = open(fid['folder']+'/color.bin', 'rb')
		destf = open(fid['folder']+'/color.json', 'w')
	except:
		return
	data = srcf.read()
	destf.write('[')
	size = int(len(data) / 3)
	for color in range(0,size):
		pos = color * 3
		r = data[pos]
		g = data[pos + 1]
		b = data[pos + 2]
		destf.write(f'\"#{r:0^2x}{g:0^2x}{b:0^2x}\"')
		if color != size -1: destf.write(',')
	
	destf.write(']')
	destf.close()
	srcf.close()
#readColors(ts3)
def generateNames(fid):
	match fid.get('img'):
		case 1:
			ln = lnames.ts3Names
			li = lnames.ts3image
		case 2:
			ln = lnames.ts3aNames
			li = lnames.ts3aimage
		case 3:
			ln = lnames.ts3waNames
			li = lnames.ts3waimage
	try:
		fq = open(fid['folder']+'/spritesheets.json','w')
		arr = []
		for n in li:
			arr.append(ln[n])
		json.dump(arr, fq)
		fq.close()
	except:
		print('ERROR!')
#generateNames(ts3wa)