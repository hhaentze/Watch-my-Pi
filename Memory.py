import psutil

def Free_Space():
	space = []
	draw = 0
	mem = psutil.virtual_memory()
	for thing in mem:
		#space.append(thing)
		if draw == 1:
			thing = float(thing) / 1024
			#print thing
			print "Noch %d MB frei" % (thing)
			return thing		
		draw = draw + 1
	
	


