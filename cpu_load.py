import psutil
import Pids
import Memory
import send_email
#import email
#config values

while(True):

	cpu_load_warning = 10 #70   #value for cpu warning message
	cpu_interval = 3      #intval for cpu_percant_reequest
	cpu_loadinglevel = False

	def cpu_load():
		count = psutil.cpu_count()
		condition_cpu_loop = True
		mem = Memory.Free_Space()
		if mem < 200:
			print "Achtung! Dein Speicher ist kleiner als 200 MB! Bitte sorge dafuer, dass mehr Speicher zur Verfuegung steht."
		while (condition_cpu_loop):
			cpu_load = psutil.cpu_percent(interval=cpu_interval)
			print(cpu_load)
			if(cpu_load > cpu_load_warning):
				condition_cpu_loop = False
				print("Warning Warning")
				print Pids.Pi(count)  
				return(cpu_load)
			
			
			
		
		


	print(cpu_load())
	if (cpu_load >= 10) & (cpu_loadinglevel == False):
		send_email.main("DANGER DANGER! Ihr Pi ist zu 85% ausgelastet - sofern sie es nicht willentlich tun, untersuchen sie ihn auf Schadsoftware.")
		ccpu_loadinglevel = True
	if (cpu_load >= 15) & (cpu_loadinglevel == True):
		send_email.main("DANGER DANGER DANGER! Ihr Pi ist bereits zu 95% ausgelastet, er wird sich bald abschalten! Sichern sie ihre Daten, sonst koennte es 			zu Datenverlusten kommen!") 
		cpu_loadinglevel = False
	
